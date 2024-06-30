from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdNextSubpass2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pSubpassBeginInfo', 'pSubpassEndInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pSubpassBeginInfo': {
        'type': CPointerType(CComplexType('VkSubpassBeginInfo')),
        'is_string': False,
    },
    'pSubpassEndInfo': {
        'type': CPointerType(CComplexType('VkSubpassEndInfo')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
