from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorSetBindingReferenceVALVE'
_member_list_ = ['sType', 'pNext', 'descriptorSetLayout', 'binding']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_BINDING_REFERENCE_VALVE',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorSetLayout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'binding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetDescriptorSetLayoutHostMappingInfoVALVE',
}
_output_of_ = set()
