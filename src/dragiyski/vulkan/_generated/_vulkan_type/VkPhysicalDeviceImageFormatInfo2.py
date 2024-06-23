import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('format', ctypes.c_int),
        ('type', ctypes.c_int),
        ('tiling', ctypes.c_int),
        ('usage', ctypes.c_uint32),
        ('flags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkImageCompressionControlEXT',
        'VkImageFormatListCreateInfo',
        'VkImageStencilUsageCreateInfo',
        'VkOpticalFlowImageFormatInfoNV',
        'VkPhysicalDeviceExternalImageFormatInfo',
        'VkPhysicalDeviceImageDrmFormatModifierInfoEXT',
        'VkPhysicalDeviceImageViewImageFormatInfoEXT',
        'VkVideoProfileListInfoKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPhysicalDeviceImageFormatProperties2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_FORMAT_INFO_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'type': {'python_name': ['type'], 'type': 'VkImageType'},
        'tiling': {'python_name': ['tiling'], 'type': 'VkImageTiling'},
        'usage': {'python_name': ['usage'], 'type': 'VkImageUsageFlags'},
        'flags': {'python_name': ['flags'], 'type': 'VkImageCreateFlags'},
    }
}
