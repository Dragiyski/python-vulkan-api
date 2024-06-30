from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceImageMemoryRequirements'
_member_list_ = ['sType', 'pNext', 'pCreateInfo', 'planeAspect']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_IMAGE_MEMORY_REQUIREMENTS',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkImageCreateInfo')),
        'type_name': 'VkImageCreateInfo',
        'structure': 'VkImageCreateInfo',
        'is_string': False,
    },
    'planeAspect': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageAspectFlagBits',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkImageCreateInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkGetDeviceImageMemoryRequirements',
    'vkGetDeviceImageSparseMemoryRequirements',
}
_output_of_ = set()
