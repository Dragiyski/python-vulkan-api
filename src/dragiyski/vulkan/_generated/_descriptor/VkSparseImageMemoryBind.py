from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSparseImageMemoryBind'
_member_list_ = ['subresource', 'offset', 'extent', 'memory', 'memoryOffset', 'flags']
_member_info_ = {
    'subresource': {
        'type': CComplexType('VkImageSubresource'),
        'type_name': 'VkImageSubresource',
        'structure': 'VkImageSubresource',
        'is_string': False,
    },
    'offset': {
        'type': CComplexType('VkOffset3D'),
        'type_name': 'VkOffset3D',
        'structure': 'VkOffset3D',
        'is_string': False,
    },
    'extent': {
        'type': CComplexType('VkExtent3D'),
        'type_name': 'VkExtent3D',
        'structure': 'VkExtent3D',
        'is_string': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSparseMemoryBindFlags',
        'enum': 'VkSparseMemoryBindFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent3D',
    'VkImageSubresource',
    'VkOffset3D',
}
_included_in_ = {
    'VkSparseImageMemoryBindInfo',
}
_input_of_ = set()
_output_of_ = set()
