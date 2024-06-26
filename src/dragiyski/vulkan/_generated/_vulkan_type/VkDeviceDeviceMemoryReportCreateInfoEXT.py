import ctypes

class VkDeviceDeviceMemoryReportCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
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
        'pfnUserCallback': 'pfn_user_callback',
        'pUserData': 'user_data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_device_memory_report',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDeviceMemoryReportFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_DEVICE_MEMORY_REPORT_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_DEVICE_MEMORY_REPORT_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .._vulkan_callback.vkDeviceMemoryReportCallbackEXT import vkDeviceMemoryReportCallbackEXT

VkDeviceDeviceMemoryReportCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnUserCallback', vkDeviceMemoryReportCallbackEXT),
    ('pUserData', ctypes.c_void_p),
]

VkDeviceDeviceMemoryReportCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pfnUserCallback': vkDeviceMemoryReportCallbackEXT,
    'pUserData': ctypes.c_void_p,
}
