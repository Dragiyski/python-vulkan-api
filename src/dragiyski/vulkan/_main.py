def __init__():
    import importlib, pkgutil, sys, ctypes, types
    from collections import OrderedDict
    from collections.abc import Iterable, Mapping
    from warnings import warn
    from ._ctypes import CComplexType, CPointerType, CArrayType, CFunctionType, ctypes_map, VKAPI_CALL,VKAPI_PTR
    from ._util import make_python_name
    from ._generated._vulkan_enum.VkStructureType import VkStructureType


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
            namespace['__dict__'] = types.MappingProxyType(namespace)
        return class_body

    def make_structure_type_init(strcture_type):
        def __init__(self, *args, **kwargs):
            if 'sType' not in self._initialized_:
                self.sType = strcture_type
        return __init__
    
    def make_structure_copy_property_init(descriptor, property_map):
        def __init__(self, *args, **kwargs):
            for field_name, property_name in property_map.items():
                if field_name not in self._initialized_ and property_name in kwargs:
                    value = kwargs[property_name]
                    member_desc = descriptor._member_info_[field_name]
                    member_type = member_desc['type']
                    if isinstance(member_type, CPointerType) and isinstance(member_type.type, CComplexType):
                        if isinstance(value, member_type.type.get_c_type()):
                            value = ctypes.pointer(value)
                        if not isinstance(value, member_type.get_c_type()):
                            raise TypeError('Initialization of `%s.%s`: invalid type of property `%s`, expected %r, got %r' % (descriptor._name_, field_name, property_name, member_type.get_c_type(), type(value)))
                    elif member_desc.get('is_string', False):
                        if isinstance(value, str):
                            value = value.encode()
                    setattr(self, field_name, value)
        return __init__
    
    def make_structure_length_processor(descriptor, property_name, field_name, length_path):
        def set_length(self, value):
            target = self
            for name in length_path[:-1]:
                target = getattr(target, name)
            setattr(target, length_path[-1], value)

        def __init__(self, *args, **kwargs):
            if field_name not in self._initialized_:
                if property_name not in kwargs:
                    setattr(self, field_name, None)
                    set_length(self, 0)
                    return
                member_desc = descriptor._member_info_[field_name]
                if member_desc.get('is_string', False):
                    values = list(value.encode() if isinstance(value, str) else value for value in kwargs[property_name])
                else:
                    values = list(kwargs[property_name])
                length = len(values)
                member_type = member_desc['type']
                array = (member_type.type.get_c_type() * length)()
                array[:] = values
                value = ctypes.cast(array, member_type.get_c_type())
                setattr(self, field_name, value)
                set_length(self, length)
        return __init__
    
    def make_structure_length_sparse_processor(descriptor, property_name, field_length_map):
        def __init__(self, *args, **kwargs):
            if property_name in kwargs:
                pass
        return __init__
    
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
    
    def complex_init(descriptor, base_class, extension):
        post_processor_list = []
        if not getattr(extension, '_no_auto_stype_', False):
            if descriptor._category_ == 'structure' and 'sType' in descriptor._member_info_ and descriptor._member_info_['sType'].get('enum', None) == 'VkStructureType' and hasattr(VkStructureType, descriptor._member_info_['sType'].get('value', '')):
                post_processor_list.append(make_structure_type_init(getattr(VkStructureType, descriptor._member_info_['sType']['value'])))
        copy_from_kwargs_map = {}
        length_descriptor_properties = {}
        for member_name in descriptor._member_list_:
            member_info = descriptor._member_info_[member_name]
            property_name = make_python_name(member_name, p = True, s = True)
            copy_from_kwargs_map[member_name] = property_name
            if 'length' in member_info:
                if member_name in getattr(extension, '_skip_length_of_', ()):
                    continue
                if property_name not in length_descriptor_properties:
                    length_descriptor_properties[property_name] = {}
                if len(member_info['length']) == 1:
                    length_descriptor_properties[property_name][member_name] = member_info['length'][0]
                elif len(member_info['length']) == 2 and member_info['length'][1] == 1:
                    length_descriptor_properties[property_name][member_name] = member_info['length'][0]
                elif len(member_info['length']) > 2:
                    warn('Skipping processing length of field `%s.%s`: No known auto processing technique. Future implementation would require to specify the field in %s._skip_length_of_ and then implement %s.__init__ to manually handle the length setting.' % (descriptor._name_, member_name, descriptor.__spec__.name, descriptor.__spec__.name))
        for property_name, member_length_map in length_descriptor_properties.items():
            for member_name in member_length_map.keys():
                if member_name in copy_from_kwargs_map:
                    del copy_from_kwargs_map[member_name]
        if len(copy_from_kwargs_map) > 0:
            post_processor_list.append(make_structure_copy_property_init(descriptor, copy_from_kwargs_map))

        for property_name, member_length_map in length_descriptor_properties.items():
            if len(member_length_map) == 2:
                post_processor_list.append(make_structure_length_sparse_processor(descriptor, property_name, member_length_map))
            elif len(member_length_map) == 1:
                post_processor_list.append(make_structure_length_processor(descriptor, property_name, *next(iter(member_length_map.items()))))
        
        def __init__(self, *args, **kwargs):
            base_class.__init__(self)
            proxy = ComplexProxy(self, base_class, descriptor)
            extension_init = getattr(extension, '_init_', None)
            if callable(extension_init):
                extension_init(proxy, *args, **kwargs)
            for processor in post_processor_list:
                processor(proxy, *args, **kwargs)
            pass
        return __init__
    
    resolve_complex_fields = []

    def compile_complex_type(descriptor):
        nonlocal ctypes_map
        base = {'structure': ctypes.Structure, 'union': ctypes.Union}[descriptor._category_]
        try:
            class_extensions = importlib.import_module('._build.%s' % descriptor._name_, __package__)
        except ModuleNotFoundError:
            class_extensions = object()
        resolve_complex_fields.append(descriptor._name_)
        complex_type = ctypes_map[descriptor._name_] = types.new_class(descriptor._name_, (base,), None, extend_namespace(
            base.__dict__,
            __module__ = '%s.binding' % __package__,
            __init__ = complex_init(descriptor, base, class_extensions),
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

    descriptor_namespace = importlib.import_module('._generated._descriptor', __package__)
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
