from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdClearAttachments'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'attachmentCount', 'pAttachments', 'rectCount', 'pRects']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'attachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pAttachments': {
        'type': CPointerType(CComplexType('VkClearAttachment')),
        'is_string': False,
        'length': [['attachmentCount']],
    },
    'rectCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pRects': {
        'type': CPointerType(CComplexType('VkClearRect')),
        'is_string': False,
        'length': [['rectCount']],
    },
}
_return_type_ = CVoidType()
