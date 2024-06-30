from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoFormatPropertiesKHR'
_member_list_ = ['sType', 'pNext', 'format', 'componentMapping', 'imageCreateFlags', 'imageType', 'imageTiling', 'imageUsageFlags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_FORMAT_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'componentMapping': {
        'type': CComplexType('VkComponentMapping'),
        'type_name': 'VkComponentMapping',
        'structure': 'VkComponentMapping',
        'is_string': False,
    },
    'imageCreateFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageCreateFlags',
        'enum': 'VkImageCreateFlags',
        'is_string': False,
    },
    'imageType': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageType',
        'enum': 'VkImageType',
        'is_string': False,
    },
    'imageTiling': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageTiling',
        'enum': 'VkImageTiling',
        'is_string': False,
    },
    'imageUsageFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageUsageFlags',
        'enum': 'VkImageUsageFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkComponentMapping',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceVideoFormatPropertiesKHR',
}
