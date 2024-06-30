from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryType'
_member_list_ = ['propertyFlags', 'heapIndex']
_member_info_ = {
    'propertyFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkMemoryPropertyFlags',
        'enum': 'VkMemoryPropertyFlags',
        'is_string': False,
    },
    'heapIndex': {
        'type': CIntType('c_uint32'),
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
