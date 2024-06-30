from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorSetLayoutHostMappingInfoVALVE'
_member_list_ = ['sType', 'pNext', 'descriptorOffset', 'descriptorSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_HOST_MAPPING_INFO_VALVE',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorOffset': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'descriptorSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetDescriptorSetLayoutHostMappingInfoVALVE',
}
