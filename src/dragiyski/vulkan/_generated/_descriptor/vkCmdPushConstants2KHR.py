from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdPushConstants2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pPushConstantsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPushConstantsInfo': {
        'type': CPointerType(CComplexType('VkPushConstantsInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
