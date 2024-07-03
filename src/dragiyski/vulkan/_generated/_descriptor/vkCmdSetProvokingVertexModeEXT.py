from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetProvokingVertexModeEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'provokingVertexMode']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'provokingVertexMode': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
