from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdEndQueryIndexedEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'queryPool', 'query', 'index']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'query': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'index': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
