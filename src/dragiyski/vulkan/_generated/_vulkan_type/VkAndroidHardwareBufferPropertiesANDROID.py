import ctypes

class VkAndroidHardwareBufferPropertiesANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('allocationSize', ctypes.c_uint64),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkAndroidHardwareBufferFormatProperties2ANDROID',
        'VkAndroidHardwareBufferFormatPropertiesANDROID',
        'VkAndroidHardwareBufferFormatResolvePropertiesANDROID',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetAndroidHardwareBufferPropertiesANDROID',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'allocationSize': 'allocation_size',
        'memoryTypeBits': 'memory_type_bits',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ANDROID_external_memory_android_hardware_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_PROPERTIES_ANDROID'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_PROPERTIES_ANDROID
        for function in self._init_:
            function(self, *args, **kwargs)

VkAndroidHardwareBufferPropertiesANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'allocationSize': ctypes.c_uint64,
    'memoryTypeBits': ctypes.c_uint32,
}
