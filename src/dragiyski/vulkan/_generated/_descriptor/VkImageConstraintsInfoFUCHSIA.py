from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageConstraintsInfoFUCHSIA'
_member_list_ = ['sType', 'pNext', 'formatConstraintsCount', 'pFormatConstraints', 'bufferCollectionConstraints', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_CONSTRAINTS_INFO_FUCHSIA',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'formatConstraintsCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pFormatConstraints': {
        'type': CPointerType(CComplexType('VkImageFormatConstraintsInfoFUCHSIA')),
        'type_name': 'VkImageFormatConstraintsInfoFUCHSIA',
        'structure': 'VkImageFormatConstraintsInfoFUCHSIA',
        'length': [['formatConstraintsCount']],
        'is_string': False,
    },
    'bufferCollectionConstraints': {
        'type': CComplexType('VkBufferCollectionConstraintsInfoFUCHSIA'),
        'type_name': 'VkBufferCollectionConstraintsInfoFUCHSIA',
        'structure': 'VkBufferCollectionConstraintsInfoFUCHSIA',
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageConstraintsInfoFlagsFUCHSIA',
        'enum': 'VkImageConstraintsInfoFlagsFUCHSIA',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkBufferCollectionConstraintsInfoFUCHSIA',
    'VkImageFormatConstraintsInfoFUCHSIA',
}
_included_in_ = set()
_input_of_ = {
    'vkSetBufferCollectionImageConstraintsFUCHSIA',
}
_output_of_ = set()
