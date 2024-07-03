from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdPushDescriptorSetWithTemplate2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pPushDescriptorSetWithTemplateInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pPushDescriptorSetWithTemplateInfo': {
        'type': CPointerType(CComplexType('VkPushDescriptorSetWithTemplateInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
