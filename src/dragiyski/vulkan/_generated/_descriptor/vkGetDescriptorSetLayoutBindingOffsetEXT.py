from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDescriptorSetLayoutBindingOffsetEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'layout', 'binding', 'pOffset']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'binding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pOffset': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
