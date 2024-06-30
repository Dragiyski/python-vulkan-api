from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoSessionMemoryRequirementsKHR'
_member_list_ = ['sType', 'pNext', 'memoryBindIndex', 'memoryRequirements']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_SESSION_MEMORY_REQUIREMENTS_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryBindIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'memoryRequirements': {
        'type': CComplexType('VkMemoryRequirements'),
        'type_name': 'VkMemoryRequirements',
        'structure': 'VkMemoryRequirements',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkMemoryRequirements',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetVideoSessionMemoryRequirementsKHR',
}
