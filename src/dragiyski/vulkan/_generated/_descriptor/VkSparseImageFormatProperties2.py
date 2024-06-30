from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSparseImageFormatProperties2'
_member_list_ = ['sType', 'pNext', 'properties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SPARSE_IMAGE_FORMAT_PROPERTIES_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'properties': {
        'type': CComplexType('VkSparseImageFormatProperties'),
        'type_name': 'VkSparseImageFormatProperties',
        'structure': 'VkSparseImageFormatProperties',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkSparseImageFormatProperties',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceSparseImageFormatProperties2',
}
