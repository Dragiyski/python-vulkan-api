from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMutableDescriptorTypeCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'mutableDescriptorTypeListCount', 'pMutableDescriptorTypeLists']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MUTABLE_DESCRIPTOR_TYPE_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'mutableDescriptorTypeListCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pMutableDescriptorTypeLists': {
        'type': CPointerType(CComplexType('VkMutableDescriptorTypeListEXT')),
        'type_name': 'VkMutableDescriptorTypeListEXT',
        'structure': 'VkMutableDescriptorTypeListEXT',
        'length': [['mutableDescriptorTypeListCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkDescriptorPoolCreateInfo',
    'VkDescriptorSetLayoutCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkMutableDescriptorTypeListEXT',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
