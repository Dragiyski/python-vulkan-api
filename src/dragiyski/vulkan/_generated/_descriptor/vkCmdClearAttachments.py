from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdClearAttachments'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'attachmentCount', 'pAttachments', 'rectCount', 'pRects']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'attachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pAttachments': {
        'type': CPointerType(CComplexType('VkClearAttachment')),
        'is_string': False,
        'length': [['attachmentCount']],
        'output': False,
    },
    'rectCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pRects': {
        'type': CPointerType(CComplexType('VkClearRect')),
        'is_string': False,
        'length': [['rectCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
