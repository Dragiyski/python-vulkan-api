import ctypes

class VkAndroidHardwareBufferUsageANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('androidHardwareBufferUsage', ctypes.c_uint64),
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
        'androidHardwareBufferUsage': 'android_hardware_buffer_usage',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ANDROID_external_memory_android_hardware_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_USAGE_ANDROID'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_USAGE_ANDROID
        for function in self._init_:
            function(self, *args, **kwargs)

VkAndroidHardwareBufferUsageANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'androidHardwareBufferUsage': ctypes.c_uint64,
}
