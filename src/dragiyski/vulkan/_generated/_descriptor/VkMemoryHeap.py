from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryHeap'
_member_list_ = ['size', 'flags']
_member_info_ = {
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkMemoryHeapFlags',
        'enum': 'VkMemoryHeapFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPhysicalDeviceMemoryProperties',
}
_input_of_ = set()
_output_of_ = set()
