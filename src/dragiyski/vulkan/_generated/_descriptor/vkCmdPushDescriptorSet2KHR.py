from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdPushDescriptorSet2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pPushDescriptorSetInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPushDescriptorSetInfo': {
        'type': CPointerType(CComplexType('VkPushDescriptorSetInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
