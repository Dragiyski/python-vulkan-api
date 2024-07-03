import pkgutil, importlib
from collections import OrderedDict
from .._ctypes import *

def __init__():
    source_package = importlib.import_module('.._generated._descriptor', __package__)
    source = {}
    target = OrderedDict()

    def get_desriptor(name):
        if name not in source:
            source[name] = importlib.import_module('.._generated._descriptor.%s' % name, __package__)
        return source[name]
    
    def iterate_descriptor_modules():
        nonlocal iterator
        for module_info in pkgutil.iter_modules(source_package.__spec__.submodule_search_locations):
            if not module_info.ispkg:
                yield from collect_descriptor(module_info.name)
        iterator = iterate_collection

    def iterate_collection():
        yield from target.values()

    def collect_descriptor(name):
        nonlocal source, target
        if name in target:
            return
        descriptor = get_desriptor(name)
        target[name] = descriptor
        if descriptor._category_ in ['structure', 'union']:
            yield from collect_complex_descriptor(descriptor)
        elif descriptor._category_ in ['callback', 'function']:
            yield from collect_function_descriptor(descriptor)
        target.move_to_end(name)
        yield descriptor

    def collect_complex_descriptor(descriptor):
        for member_name in descriptor._member_list_:
            member_info = descriptor._member_info_[member_name]
            yield from collect_from_ctype(member_info['type'])
    
    def collect_function_descriptor(descriptor):
        yield from collect_from_ctype(descriptor._return_type_)
        for ctype in [x['type'] for x in descriptor._argument_info_.values()]:
            yield from collect_from_ctype(ctype)

    def collect_from_ctype(ctype):
        if isinstance(ctype, (CFunctionType, CComplexType)):
            yield from collect_descriptor(ctype.name)
        elif isinstance(ctype, (CArrayType, CPointerType)):
            yield from collect_from_ctype(ctype.type)

    def __iter__():
        yield from iterator()

    iterator = iterate_descriptor_modules
    return __iter__
    

iterator = __init__()
del __init__
