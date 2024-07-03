from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetFrontFace'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'frontFace']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'frontFace': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
