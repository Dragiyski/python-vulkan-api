from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDescriptorSetLayoutHostMappingInfoVALVE'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pBindingReference', 'pHostMapping']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pBindingReference': {
        'type': CPointerType(CComplexType('VkDescriptorSetBindingReferenceVALVE')),
        'is_string': False,
    },
    'pHostMapping': {
        'type': CPointerType(CComplexType('VkDescriptorSetLayoutHostMappingInfoVALVE')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
