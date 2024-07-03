from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetCullMode'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'cullMode']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'cullMode': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
