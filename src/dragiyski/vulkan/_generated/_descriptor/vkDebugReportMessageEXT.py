from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkDebugReportMessageEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'flags', 'objectType', 'object', 'location', 'messageCode', 'pLayerPrefix', 'pMessage']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'objectType': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'object': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'location': {
        'type': CIntType('c_size_t'),
        'is_string': False,
        'output': False,
    },
    'messageCode': {
        'type': CIntType('c_int32'),
        'is_string': False,
        'output': False,
    },
    'pLayerPrefix': {
        'type': CStringType('c_char_p'),
        'is_string': True,
        'length': [],
        'output': False,
    },
    'pMessage': {
        'type': CStringType('c_char_p'),
        'is_string': True,
        'length': [],
        'output': False,
    },
}
_return_type_ = CVoidType()
