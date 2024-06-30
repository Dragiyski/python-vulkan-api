from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceMemoryProperties'
_member_list_ = ['memoryTypeCount', 'memoryTypes', 'memoryHeapCount', 'memoryHeaps']
_member_info_ = {
    'memoryTypeCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'memoryTypes': {
        'type': CArrayType(CComplexType('VkMemoryType'), 32),
        'type_name': 'VkMemoryType',
        'structure': 'VkMemoryType',
        'length': [['memoryTypeCount']],
        'is_string': False,
    },
    'memoryHeapCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'memoryHeaps': {
        'type': CArrayType(CComplexType('VkMemoryHeap'), 16),
        'type_name': 'VkMemoryHeap',
        'structure': 'VkMemoryHeap',
        'length': [['memoryHeapCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkMemoryHeap',
    'VkMemoryType',
}
_included_in_ = {
    'VkPhysicalDeviceMemoryProperties2',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceMemoryProperties',
}
