from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetColorWriteEnableEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'attachmentCount', 'pColorWriteEnables']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'attachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pColorWriteEnables': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['attachmentCount']],
    },
}
_return_type_ = CVoidType()
