from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetRasterizerDiscardEnable'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'rasterizerDiscardEnable']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'rasterizerDiscardEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
