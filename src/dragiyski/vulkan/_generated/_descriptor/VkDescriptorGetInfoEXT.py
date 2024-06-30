from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorGetInfoEXT'
_member_list_ = ['sType', 'pNext', 'type', 'data']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_GET_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkDescriptorType',
        'enum': 'VkDescriptorType',
        'is_string': False,
    },
    'data': {
        'type': CComplexType('VkDescriptorDataEXT'),
        'type_name': 'VkDescriptorDataEXT',
        'union': 'VkDescriptorDataEXT',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDescriptorDataEXT',
}
_included_in_ = set()
_input_of_ = {
    'vkGetDescriptorEXT',
}
_output_of_ = set()
