def __init__():
    import importlib, pkgutil, sys, ctypes, types
    from collections import OrderedDict
    from collections.abc import Iterable, Mapping
    from warnings import warn
    from .._ctypes import CComplexType, CPointerType, CArrayType, CFunctionType, ctypes_map, VKAPI_CALL,VKAPI_PTR
    from .._util import make_python_name
    from .._generated._vulkan_enum.VkStructureType import VkStructureType
    from .._view import ArrayView


    module = sys.modules[__name__]

    def collect_complex_descriptor(name):
        nonlocal descriptors
        descriptor = descriptors[name]
        for member_name in descriptor._member_list_:
            member_info = descriptor._member_info_[member_name]
            dependency = None
            if 'structure' in member_info:
                dependency = member_info['structure']
            elif 'union' in member_info:
                dependency = member_info['union']
            elif 'callback' in member_info:
                dependency = member_info['callback']
            if dependency is not None and dependency != name:
                collect_descriptor(dependency)

    def collect_from_ctype(ctype):
        if isinstance(ctype, (CFunctionType, CComplexType)):
            collect_descriptor(ctype.name)
        elif isinstance(ctype, (CArrayType, CPointerType)):
            collect_from_ctype(ctype.type)

    def collect_function_descriptor(name):
        nonlocal descriptors
        descriptor = descriptors[name]
        collect_from_ctype(descriptor._return_type_)
        for ctype in [x['type'] for x in descriptor._argument_info_.values()]:
            collect_from_ctype(ctype)

    def collect_descriptor(name):
        nonlocal descriptor_jobs, descriptors
        if name in descriptor_jobs:
            return
        descriptor = descriptors[name]
        descriptor_jobs[name] = descriptor
        if descriptor._category_ in ['structure', 'union']:
            collect_complex_descriptor(name)
        elif descriptor._category_ in ['callback', 'function']:
            collect_function_descriptor(name)
        else:
            pass
        descriptor_jobs.move_to_end(name)
        pass

    def extend_namespace(*args, **kwargs):
        def class_body(namespace):
            for arg in args:
                if not isinstance(arg, Mapping):
                    raise TypeError('Expected every positional arguments to be a mapping')
                namespace.update(arg)
            namespace.update(kwargs)
            namespace['__dict__'] = namespace
        return class_body
    
    class ComplexProxy:
        def __init__(self, target, base_class, descriptor):
            object.__setattr__(self, '_ComplexProxy__target', target)
            object.__setattr__(self, '_ComplexProxy__base_class', base_class)
            object.__setattr__(self, '_ComplexProxy__descriptor', descriptor)
            object.__setattr__(self, '_initialized_', set())

        def __getattr__(self, name):
            if name in self.__descriptor._member_info_:
                return self.__base_class.__getattribute__(self.__target, name)
            raise AttributeError(name, name=name, obj=self.__target)
        
        def __setattr__(self, name, value):
            if name in self.__descriptor._member_info_:
                self.__base_class.__setattr__(self.__target, name, value)
                self._initialized_.add(name)
            else:
                object.__setattr__(self, name, value)
    
    def complex_init(descriptor, base_class, property_map, extension):
        structure_type = descriptor._member_info_.get('sType', None)
        if structure_type is not None and structure_type.get('enum', None) == 'VkStructureType' and hasattr(VkStructureType, structure_type.get('value', '')):
            structure_type = getattr(VkStructureType, structure_type['value'])
        else:
            structure_type = None
        def __init__(self, *args, **kwargs):
            base_class.__init__(self)
            unexpected = list(k for k in kwargs if k not in property_map)
            if len(unexpected) > 1:
                raise TypeError('%s() got an unexpected keyword argument %r' % (__init__.__qualname__, unexpected[0]))
            if structure_type is not None:
                base_class.__setattr__(self, 'sType', structure_type)
            for property_name, property_descriptor in property_map.items():
                if property_name in kwargs:
                    property_descriptor['set'](self, kwargs[property_name])
        __init__.__qualname__ = '%s.%s.%s' % (__package__, descriptor._name_, __init__.__name__)
        return __init__

    def length_chain_get_field(field_name):
        def this_chain_length(next_set_length):
            def chain_length(self, *args, **kwargs):
                return next_set_length(type(self).__base__.__getattr__(self, field_name), *args, **kwargs)
            return chain_length
        return this_chain_length
    
    def length_chain_unwrap_pointer():
        def this_chain_length(next_set_length):
            def chain_length(self, *args, **kwargs):
                return next_set_length(self.contents, *args, **kwargs)
            return chain_length
        return this_chain_length
    
    def length_get_field(field_name):
        def get_length(self):
            return type(self).__base__.__getattribute__(self, field_name)
        return get_length
    
    def length_set_field(field_name):
        def set_length(self, value):
            return type(self).__base__.__setattr__(self, field_name, value)
        return set_length
    
    def length_chain_function(*chain):
        chain = list(chain)
        root = chain.pop()
        while len(chain) > 0:
            wrapper = chain.pop()
            root = wrapper(root)
        return root
    
    def make_length_chain(descriptor, length_path, length_tail):
        chain = []
        length_descriptor = descriptor
        match descriptor._category_:
            case 'structure' | 'union':
                info_name = '_member_info_'
            case 'function' | 'callback':
                info_name = '_argument_info_'
            case _:
                raise ValueError('In %s: Invalid descriptor %r: length processing is only supported for complex and function types.' % (descriptor._name_, descriptor._category_))
        for length_name in length_path[:-1]:
            chain.append(length_chain_get_field(length_name))
            length_ctype = getattr(length_descriptor, info_name)[length_name]['type']
            while isinstance(length_ctype, CPointerType):
                length_ctype = length_ctype.type
                chain.append(length_chain_unwrap_pointer())
            if not isinstance(length_ctype, CComplexType):
                raise TypeError('In %s: length_path struct entry "%s" is not a complex type.' % (descriptor._name_, length_name))
            length_descriptor = descriptor_jobs[length_ctype.name]
        length_ctype = getattr(length_descriptor, info_name)[length_path[-1]]['type']
        while isinstance(length_ctype, CPointerType):
            length_ctype = length_ctype.type
            chain.append(length_chain_unwrap_pointer())
        chain.append(length_tail(length_path[-1]))
        return length_chain_function(*chain)
        
    def make_sparse_c_array_getter(descriptor, base_class, property_name, length_descriptor, contiguous_field_name, sparse_field_name, extension):
        def __get__(self):
            pass
        __get__.__qualname__ = '%s.%s.%s.%s' % (__package__, descriptor._name_, property_name, __get__.__name__)
        return __get__

    def make_sparse_c_array_setter(descriptor, base_class, property_name, length_descriptor, contiguous_field_name, sparse_field_name, extension):
        contiguous_field_desc = descriptor._member_info_[contiguous_field_name]
        sparse_field_desc = descriptor._member_info_[sparse_field_name]
        contiguous_field_ctype = contiguous_field_desc['type']
        sparse_field_ctype = sparse_field_desc['type']
        def __set__(self, value):
            pass
        __set__.__qualname__ = '%s.%s.%s.%s' % (__package__, descriptor._name_, property_name, __set__.__name__)
        return __set__

    def make_c_array_getter(descriptor, base_class, property_name, length_path, field_name, extension):
        field_desc = descriptor._member_info_[field_name]
        field_ctype = field_desc['type']
        if not isinstance(field_ctype, CPointerType):
            raise TypeError('In %s: expected pointer-type field "%s", got %r' % (descriptor._name_, field_name, field_ctype))
        inner_ctype = field_ctype.type
        is_str_convert_required = field_desc.get('is_string', False) and inner_ctype.get_python_type() is bytes
        is_complex_type_pointer = isinstance(field_ctype, CPointerType) and isinstance(field_ctype.type, CComplexType)
        get_length = make_length_chain(descriptor, length_path, length_get_field)

        def get_item(array, index):
            value = array[index]
            if is_str_convert_required and isinstance(value, bytes):
                value = value.decode()
            if is_complex_type_pointer and isinstance(value, field_ctype.get_c_type()):
                value = value.contents if value else None
            return value

        def set_item(array, index, value):
            if is_str_convert_required and isinstance(value, str):
                value = value.encode()
            if is_complex_type_pointer and isinstance(value, field_ctype.type.get_c_type()):
                value = ctypes.pointer(value)
            array[index] = value

        def __get__(self):
            value = base_class.__getattribute__(self, field_name)
            if not value:
                return []
            length = get_length(self)
            array = (field_ctype.type.get_c_type() * length).from_address(ctypes.cast(value, ctypes.c_void_p).value)
            value = ArrayView(array, get_item, set_item)
            return value
        __get__.__qualname__ = '%s.%s.%s.%s' % (__package__, descriptor._name_, property_name, __get__.__name__)
        return __get__

    def make_c_array_setter(descriptor, base_class, property_name, length_path, field_name, extension):
        field_desc = descriptor._member_info_[field_name]
        field_ctype = field_desc['type']
        if not isinstance(field_ctype, CPointerType):
            raise TypeError('In %s: expected pointer-type field "%s", got %r' % (descriptor._name_, field_name, field_ctype))
        inner_ctype = field_ctype.type
        is_str_convert_required = field_desc.get('is_string', False) and inner_ctype.get_python_type() is bytes

        set_length = make_length_chain(descriptor, length_path, length_set_field)
        
        def __set__(self, value):
            if isinstance(value, ctypes.Array):
                if value._type_ is not inner_ctype.get_c_type():
                    raise TypeError('Wrong array item type: expected %r, got %r' % (inner_ctype.get_c_type(), value._type_))
                length = len(value)
            else:
                if is_str_convert_required:
                    value = list(item.encode() if isinstance(item, str) else item for item in value)
                else:
                    value = list(value)
                length = len(value)
                array = (inner_ctype.get_c_type() * length)()
                array[:] = value
                value = array
            base_class.__setattr__(self, field_name, ctypes.cast(value, field_ctype.get_c_type()))
            set_length(self, length)

        __set__.__qualname__ = '%s.%s.%s.%s' % (__package__, descriptor._name_, property_name, __set__.__name__)
        return __set__

    def make_field_getter(descriptor, base_class, property_name, field_name, extension):
        field_desc = descriptor._member_info_[field_name]
        field_ctype = field_desc['type']
        is_str_convert_required = field_desc.get('is_string', False) and field_ctype.get_python_type() is bytes
        is_complex_type_pointer = isinstance(field_ctype, CPointerType) and isinstance(field_ctype.type, CComplexType)
        enum_class = None
        if 'enum' in field_desc:
            enum_module = importlib.import_module('.._generated.vulkan_enum', __package__)
            enum_class = getattr(enum_module, field_desc['enum'], None)
            if enum_class is None:
                raise ReferenceError('Reference to non-existing enum: %s' % field_desc['enum'])
        def __get__(self):
            value = base_class.__getattribute__(self, field_name)
            if is_str_convert_required and isinstance(value, bytes):
                value = value.decode()
            if is_complex_type_pointer and isinstance(value, field_ctype.get_c_type()):
                value = value.contents if value else None
            if enum_class is not None:
                try:
                    value = enum_class(value)
                except ValueError:
                    pass
            return value
        __get__.__qualname__ = '%s.%s.%s.%s' % (__package__, descriptor._name_, property_name, __get__.__name__)
        return __get__

    def make_field_setter(descriptor, base_class, property_name, field_name, extension):
        field_desc = descriptor._member_info_[field_name]
        field_ctype = field_desc['type']
        is_str_convert_required = field_desc.get('is_string', False) and field_ctype.get_python_type() is bytes
        is_complex_type_pointer = isinstance(field_ctype, CPointerType) and isinstance(field_ctype.type, CComplexType)
        def __set__(self, value):
            if is_str_convert_required and isinstance(value, str):
                value = value.encode()
            if is_complex_type_pointer and isinstance(value, field_ctype.type.get_c_type()):
                value = ctypes.pointer(value)
            base_class.__setattr__(self, field_name, value)
        __set__.__qualname__ = '%s.%s.%s.%s' % (__package__, descriptor._name_, property_name, __set__.__name__)
        return __set__

    def compile_property_map(descriptor, base_class, extension):
        nonlocal ctypes_map
        property_name_map = { field_name: make_python_name(field_name, p = True, s = True) for field_name in descriptor._member_info_ }
        property_map = {}
        duplicate_properties = set()
        duplicate_properties_detection = {}
        length_map = {}
        hide_fields = set()
        for member_name in descriptor._member_list_:
            member_info = descriptor._member_info_[member_name]
            property_name = property_name_map[member_name]
            if property_name not in duplicate_properties_detection:
                duplicate_properties_detection[property_name] = member_name
            else:
                duplicate_properties.add(property_name)
            if 'length' in member_info:
                if property_name not in length_map:
                    length_map[property_name] = {}
                if len(member_info['length']) == 1 or len(member_info['length']) == 2 and member_info['length'][1] == 1:
                    length_map[property_name][member_name] = member_info['length']
        del duplicate_properties_detection
        for property_name, field_length_map in length_map.items():
            if len(field_length_map) == 2:
                contiguous_field_name = None
                sparse_field_name = None
                for field_name, length_desc in field_length_map.items():
                    match len(length_desc):
                        case 1:
                            contiguous_field_name = field_name
                        case 2:
                            sparse_field_name = field_name
                if contiguous_field_name is None or sparse_field_name is None:
                    continue
                if tuple(field_length_map[contiguous_field_name][0]) != tuple(field_length_map[sparse_field_name][0]):
                    continue
                if not isinstance(descriptor._member_info_[contiguous_field_name]['type'], CPointerType) or descriptor._member_info_[contiguous_field_name]['type'].pointer() is not descriptor._member_info_[sparse_field_name]['type']:
                    continue
                property_map[property_name] = {
                    'priority': -20,
                    'get': make_sparse_c_array_getter(descriptor, base_class, property_name, field_length_map[sparse_field_name][0], contiguous_field_name, sparse_field_name, extension),
                    'set': make_sparse_c_array_setter(descriptor, base_class, property_name, field_length_map[sparse_field_name][0], contiguous_field_name, sparse_field_name, extension)
                }
                if len(length_desc[0]) == 1:
                    hide_fields.add(length_desc[0][0])
                duplicate_properties.discard(property_name)
            elif len(field_length_map) == 1:
                field_name, length_desc = next(iter(field_length_map.items()))
                if not isinstance(descriptor._member_info_[field_name]['type'], CPointerType):
                    continue
                property_map[property_name] = {
                    'priority': -20,
                    'get': make_c_array_getter(descriptor, base_class, property_name, length_desc[0], field_name, extension),
                    'set': make_c_array_setter(descriptor, base_class, property_name, length_desc[0], field_name, extension)
                }
                if len(length_desc[0]) == 1:
                    hide_fields.add(length_desc[0][0])
                duplicate_properties.discard(property_name)
        for property_name in duplicate_properties:
            field_name_list = [k for k, v in property_name_map.items() if v == property_name]
            if len(field_name_list) < 2:
                continue
            for field_name in field_name_list:
                property_name_map[field_name] = make_python_name(field_name, p = False, s = False)
        for field_name, property_name in property_name_map.items():
            if field_name in hide_fields:
                continue
            if property_name in property_map:
                continue
            property_map[property_name] = {
                'priority': 0,
                'get': make_field_getter(descriptor, base_class, property_name, field_name, extension),
                'set': make_field_setter(descriptor, base_class, property_name, field_name, extension)
            }
        for property_name in property_map:
            value = getattr(extension, 'extend_property_get_%s' % property_name, None)
            if callable(value):
                value = value(descriptor, base_class, property_map[property_name]['get'], property_name, property_map)
                if not callable(value):
                    raise TypeError('Extension %s.%s did not returned a callback object')
                property_map[property_name]['get'] = value
            value = getattr(extension, 'extend_property_set_%s' % property_name, None)
            if callable(value):
                value = value(descriptor, base_class, property_map[property_name]['set'], property_name, property_map)
                if not callable(value):
                    raise TypeError('Extension %s.%s did not returned a callback object')
                property_map[property_name]['set'] = value
        property_ordered_names = sorted(property_map, key = lambda key: property_map[key]['priority'], reverse = True)
        property_ordered_map = OrderedDict((k, property_map[k]) for k in property_ordered_names)
        return property_ordered_map
    
    def complex_getattribute(descriptor, base_class, property_map):
        def __getattribute__(self, name):
            if name in property_map:
                if name not in self.__dict__:
                    self.__dict__[name] = property_map[name]['get'](self)
                return self.__dict__[name]
            if name not in descriptor._member_info_:
                return base_class.__getattribute__(self, name)
            raise AttributeError(name, name=name, obj=self)
        __getattribute__.__qualname__ = '%s.%s.%s' % (__package__, descriptor._name_, __getattribute__.__name__)
        return __getattribute__
    
    def complex_setattr(descriptor, base_class, property_map):
        def __setattr__(self, name, value):
            if name in property_map:
                self.__dict__.pop(name, None)
                return property_map[name]['set'](self, value)
            if name in descriptor._member_info_:
                raise AttributeError('%r object has no attribute %r' % (self.__class__.__name__, name))
            return base_class.__setattr__(self, name, value)
        __setattr__.__qualname__ = '%s.%s.%s' % (__package__, descriptor._name_, __setattr__.__name__)
        return __setattr__
    
    def complex_dir(descriptor, base_class, property_map):
        def __dir__(self):
            return list(set(dir(base_class)).difference(descriptor._member_list_).union(property_map.keys()))
        __dir__.__qualname__ = '%s.%s.%s' % (__package__, descriptor._name_, __dir__.__name__)
        return __dir__
    
    resolve_complex_fields = []

    def compile_complex_type(descriptor):
        nonlocal ctypes_map
        base_class = {'structure': ctypes.Structure, 'union': ctypes.Union}[descriptor._category_]
        try:
            class_extensions = importlib.import_module('._build.%s' % descriptor._name_, __package__)
        except ModuleNotFoundError:
            class_extensions = object()
        resolve_complex_fields.append(descriptor._name_)
        property_map = compile_property_map(descriptor, base_class, class_extensions)
        complex_type = ctypes_map[descriptor._name_] = types.new_class(descriptor._name_, (base_class,), None, extend_namespace(
            base_class.__dict__,
            __module__ = '%s.binding' % __package__,
            __init__ = complex_init(descriptor, base_class, property_map, class_extensions),
            __getattribute__ = complex_getattribute(descriptor, base_class, property_map),
            __setattr__ = complex_setattr(descriptor, base_class, property_map),
            __dir__ = complex_dir(descriptor, base_class, property_map),
            __vulkan_descriptor__ = descriptor,
            __doc__ = 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/%s.html' % descriptor._name_
        ))
        setattr(module, descriptor._name_, complex_type)
        __all__.add(descriptor._name_)


    def link_complex_type(name):
        descriptor = descriptor_jobs[name]
        fields = []
        for field_name in descriptor._member_list_:
            field_info = descriptor._member_info_[field_name]
            if 'bitsize' in field_info:
                field = (field_name, field_info['type'].get_c_type(), field_info['bitsize'])
            else:
                field = (field_name, field_info['type'].get_c_type())
            fields.append(field)
        ctypes_map[descriptor._name_]._fields_ = fields
        ctypes_map[descriptor._name_]._type_ = { name: ctype for name, ctype, *_ in fields }

    def make_singleton_callback(descriptor, ctype):
        def __init__(self):
            pass

    def compile_callback_type(descriptor):
        constructor = {'VKAPI_CALL': VKAPI_CALL, 'VKAPI_PTR': VKAPI_PTR}[descriptor._constructor_]
        base_args = [descriptor._return_type_.get_c_type()]
        for arg_name in descriptor._argument_list_:
            base_args.append(descriptor._argument_info_[arg_name]['type'].get_c_type())
        base_type = constructor(*base_args)
        # if 'pUserData' not in descriptor._argument_list_:
        callback_type = ctypes_map[descriptor._name_] = types.new_class(descriptor._name_, (base_type,), None, extend_namespace(
            base_type.__dict__,
            __module__ = '%s.binding' % __package__,
            __vulkan_descriptor__ = descriptor,
            __doc__ = 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/PFN_%s.html' % descriptor._name_
        ))
        setattr(module, descriptor._name_, callback_type)
        __all__.add(descriptor._name_)
    
    def compile_function_type(descriptor):
        constructor = {'VKAPI_CALL': VKAPI_CALL, 'VKAPI_PTR': VKAPI_PTR}[descriptor._constructor_]
        base_args = [descriptor._return_type_.get_c_type()]
        for arg_name in descriptor._argument_list_:
            base_args.append(descriptor._argument_info_[arg_name]['type'].get_c_type())
        base_type = constructor(*base_args)
        function_type = ctypes_map[descriptor._name_] = types.new_class(descriptor._name_, (base_type,), None, extend_namespace(
            base_type.__dict__,
            __module__ = '%s.binding' % __package__,
            __vulkan_descriptor__ = descriptor,
            __doc__ = 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/PFN_%s.html' % descriptor._name_
        ))
        setattr(module, descriptor._name_, function_type)
        __all__.add(descriptor._name_)
        pass

    def compile_descriptor(name):
        nonlocal descriptor_jobs, module
        descriptor = descriptor_jobs[name]
        if descriptor._category_ in ['structure', 'union']:
            compile_complex_type(descriptor)
        elif descriptor._category_ == 'function':
            compile_function_type(descriptor)
        elif descriptor._category_ == 'callback':
            compile_callback_type(descriptor)

    descriptor_namespace = importlib.import_module('.._generated._descriptor', __package__)
    descriptors = {}
    descriptor_jobs = OrderedDict()
    for module_info in pkgutil.iter_modules(descriptor_namespace.__spec__.submodule_search_locations, descriptor_namespace.__spec__.name + '.'):
        if not module_info.ispkg:
            descriptors[module_info.name.split('.')[-1]] = importlib.import_module(module_info.name, __package__)
            pass
    for name in descriptors:
        collect_descriptor(name)
    del descriptors
    for name in descriptor_jobs:
        compile_descriptor(name)
    for name in resolve_complex_fields:
        link_complex_type(name)
    pass

__all__ = set()

__init__()
del __init__

__all__ = list(__all__)
