from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDescriptorSetLayoutHostMappingInfoVALVE'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pBindingReference', 'pHostMapping']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pBindingReference': {
        'type': CPointerType(CComplexType('VkDescriptorSetBindingReferenceVALVE')),
        'is_string': False,
        'output': False,
    },
    'pHostMapping': {
        'type': CPointerType(CComplexType('VkDescriptorSetLayoutHostMappingInfoVALVE')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
