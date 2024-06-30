from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSparseMemoryBind'
_member_list_ = ['resourceOffset', 'size', 'memory', 'memoryOffset', 'flags']
_member_info_ = {
    'resourceOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
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
_includes_ = set()
_included_in_ = {
    'VkSparseBufferMemoryBindInfo',
    'VkSparseImageOpaqueMemoryBindInfo',
}
_input_of_ = set()
_output_of_ = set()
