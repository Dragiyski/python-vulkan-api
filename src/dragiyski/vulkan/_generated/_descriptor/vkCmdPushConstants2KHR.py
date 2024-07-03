from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdPushConstants2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pPushConstantsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pPushConstantsInfo': {
        'type': CPointerType(CComplexType('VkPushConstantsInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
