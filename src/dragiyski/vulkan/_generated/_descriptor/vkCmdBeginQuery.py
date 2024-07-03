from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBeginQuery'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'queryPool', 'query', 'flags']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'query': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
