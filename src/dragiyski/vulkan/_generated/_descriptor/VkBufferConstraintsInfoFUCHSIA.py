from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferConstraintsInfoFUCHSIA'
_member_list_ = ['sType', 'pNext', 'createInfo', 'requiredFormatFeatures', 'bufferCollectionConstraints']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_CONSTRAINTS_INFO_FUCHSIA',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'createInfo': {
        'type': CComplexType('VkBufferCreateInfo'),
        'type_name': 'VkBufferCreateInfo',
        'structure': 'VkBufferCreateInfo',
        'is_string': False,
    },
    'requiredFormatFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFormatFeatureFlags',
        'enum': 'VkFormatFeatureFlags',
        'is_string': False,
    },
    'bufferCollectionConstraints': {
        'type': CComplexType('VkBufferCollectionConstraintsInfoFUCHSIA'),
        'type_name': 'VkBufferCollectionConstraintsInfoFUCHSIA',
        'structure': 'VkBufferCollectionConstraintsInfoFUCHSIA',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkBufferCollectionConstraintsInfoFUCHSIA',
    'VkBufferCreateInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkSetBufferCollectionBufferConstraintsFUCHSIA',
}
_output_of_ = set()
