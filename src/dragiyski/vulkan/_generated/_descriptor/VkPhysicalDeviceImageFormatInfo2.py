from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceImageFormatInfo2'
_member_list_ = ['sType', 'pNext', 'format', 'type', 'tiling', 'usage', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_FORMAT_INFO_2',
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
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageType',
        'enum': 'VkImageType',
        'is_string': False,
    },
    'tiling': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageTiling',
        'enum': 'VkImageTiling',
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageUsageFlags',
        'enum': 'VkImageUsageFlags',
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageCreateFlags',
        'enum': 'VkImageCreateFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkImageCompressionControlEXT',
    'VkImageFormatListCreateInfo',
    'VkImageStencilUsageCreateInfo',
    'VkOpticalFlowImageFormatInfoNV',
    'VkPhysicalDeviceExternalImageFormatInfo',
    'VkPhysicalDeviceImageDrmFormatModifierInfoEXT',
    'VkPhysicalDeviceImageViewImageFormatInfoEXT',
    'VkVideoProfileListInfoKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetPhysicalDeviceImageFormatProperties2',
}
_output_of_ = set()
