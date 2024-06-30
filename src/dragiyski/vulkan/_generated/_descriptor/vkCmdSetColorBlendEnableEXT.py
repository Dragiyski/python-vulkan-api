from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetColorBlendEnableEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstAttachment', 'attachmentCount', 'pColorBlendEnables']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstAttachment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'attachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pColorBlendEnables': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['attachmentCount']],
    },
}
_return_type_ = CVoidType()
