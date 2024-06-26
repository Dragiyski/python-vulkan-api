import ctypes

class VkImageCompressionControlEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('compressionControlPlaneCount', ctypes.c_uint32),
        ('pFixedRateFlags', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = {
        'VkImageCreateInfo',
        'VkPhysicalDeviceImageFormatInfo2',
        'VkSwapchainCreateInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'compressionControlPlaneCount': 'compression_control_plane_count',
        'pFixedRateFlags': 'fixed_rate_flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_image_compression_control',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkImageCompressionFlagsEXT',
        'pFixedRateFlags': 'VkImageCompressionFixedRateFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_CONTROL_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_CONTROL_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkImageCompressionControlEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'compressionControlPlaneCount': ctypes.c_uint32,
    'pFixedRateFlags': ctypes.POINTER(ctypes.c_uint32),
}
