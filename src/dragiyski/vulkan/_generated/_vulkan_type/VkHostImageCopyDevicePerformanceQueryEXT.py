import ctypes

class VkHostImageCopyDevicePerformanceQueryEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('optimalDeviceAccess', ctypes.c_uint32),
        ('identicalMemoryLayout', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkImageFormatProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'optimalDeviceAccess': 'optimal_device_access',
        'identicalMemoryLayout': 'identical_memory_layout',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_host_image_copy',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_HOST_IMAGE_COPY_DEVICE_PERFORMANCE_QUERY_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_HOST_IMAGE_COPY_DEVICE_PERFORMANCE_QUERY_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkHostImageCopyDevicePerformanceQueryEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'optimalDeviceAccess': ctypes.c_uint32,
    'identicalMemoryLayout': ctypes.c_uint32,
}
