from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorSetLayoutBindingFlagsCreateInfo'
_member_list_ = ['sType', 'pNext', 'bindingCount', 'pBindingFlags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_BINDING_FLAGS_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'bindingCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBindingFlags': {
        'type': CPointerType(CIntType('c_uint32')),
        'type_name': 'VkDescriptorBindingFlags',
        'enum': 'VkDescriptorBindingFlags',
        'length': [['bindingCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkDescriptorSetLayoutCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
