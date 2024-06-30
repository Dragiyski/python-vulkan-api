import ctypes

class VkPhysicalDeviceLayeredApiPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('layeredAPI', ctypes.c_int),
        ('deviceName', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPhysicalDeviceLayeredApiVulkanPropertiesKHR',
    }
    _includes_ = set()
    _included_in_ = {
        'VkPhysicalDeviceLayeredApiPropertiesListKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'vendorID': 'vendor_id',
        'deviceID': 'device_id',
        'layeredAPI': 'layered_api',
        'deviceName': 'device_name',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance7',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'layeredAPI': 'VkPhysicalDeviceLayeredApiKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_API_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_API_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceLayeredApiPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vendorID': ctypes.c_uint32,
    'deviceID': ctypes.c_uint32,
    'layeredAPI': ctypes.c_int,
    'deviceName': ctypes.ARRAY(ctypes.c_char, 256),
}
