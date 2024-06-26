import ctypes

class VkPhysicalDeviceSparseImageFormatInfo2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('format', ctypes.c_int),
        ('type', ctypes.c_int),
        ('samples', ctypes.c_uint32),
        ('usage', ctypes.c_uint32),
        ('tiling', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkGetPhysicalDeviceSparseImageFormatProperties2',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'format': 'format',
        'type': 'type',
        'samples': 'samples',
        'usage': 'usage',
        'tiling': 'tiling',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'format': 'VkFormat',
        'type': 'VkImageType',
        'usage': 'VkImageUsageFlags',
        'tiling': 'VkImageTiling',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SPARSE_IMAGE_FORMAT_INFO_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SPARSE_IMAGE_FORMAT_INFO_2
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceSparseImageFormatInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'format': ctypes.c_int,
    'type': ctypes.c_int,
    'samples': ctypes.c_uint32,
    'usage': ctypes.c_uint32,
    'tiling': ctypes.c_int,
}
