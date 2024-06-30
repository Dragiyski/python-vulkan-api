from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetColorBlendEquationEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstAttachment', 'attachmentCount', 'pColorBlendEquations']
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
    'pColorBlendEquations': {
        'type': CPointerType(CComplexType('VkColorBlendEquationEXT')),
        'is_string': False,
        'length': [['attachmentCount']],
    },
}
_return_type_ = CVoidType()
