from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSparseImageMemoryRequirements2'
_member_list_ = ['sType', 'pNext', 'memoryRequirements']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SPARSE_IMAGE_MEMORY_REQUIREMENTS_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryRequirements': {
        'type': CComplexType('VkSparseImageMemoryRequirements'),
        'type_name': 'VkSparseImageMemoryRequirements',
        'structure': 'VkSparseImageMemoryRequirements',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkSparseImageMemoryRequirements',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetDeviceImageSparseMemoryRequirements',
    'vkGetImageSparseMemoryRequirements2',
}
