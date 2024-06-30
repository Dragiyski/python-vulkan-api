from ..._ctypes import *

_category_ = 'callback'
_name_ = 'vkDebugReportCallbackEXT'
_constructor_ = 'VKAPI_PTR'
_argument_list_ = ['flags', 'objectType', 'object', 'location', 'messageCode', 'pLayerPrefix', 'pMessage', 'pUserData']
_argument_info_ = {
    'flags': {
        'type': CIntType('c_uint32'),
    },
    'objectType': {
        'type': CIntType('c_int'),
    },
    'object': {
        'type': CIntType('c_uint64'),
    },
    'location': {
        'type': CIntType('c_size_t'),
    },
    'messageCode': {
        'type': CIntType('c_int32'),
    },
    'pLayerPrefix': {
        'type': CStringType('c_char_p'),
    },
    'pMessage': {
        'type': CStringType('c_char_p'),
    },
    'pUserData': {
        'type': CIntType('c_void_p'),
    },
}
_return_type_ = CIntType('c_uint32')
