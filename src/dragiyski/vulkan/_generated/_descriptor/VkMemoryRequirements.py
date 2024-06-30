from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryRequirements'
_member_list_ = ['size', 'alignment', 'memoryTypeBits']
_member_info_ = {
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'alignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'memoryTypeBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkMemoryRequirements2',
    'VkVideoSessionMemoryRequirementsKHR',
}
_input_of_ = set()
_output_of_ = {
    'vkGetBufferMemoryRequirements',
    'vkGetImageMemoryRequirements',
}
