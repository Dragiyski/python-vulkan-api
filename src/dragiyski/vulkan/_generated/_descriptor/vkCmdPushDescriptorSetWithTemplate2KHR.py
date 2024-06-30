from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdPushDescriptorSetWithTemplate2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pPushDescriptorSetWithTemplateInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPushDescriptorSetWithTemplateInfo': {
        'type': CPointerType(CComplexType('VkPushDescriptorSetWithTemplateInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
