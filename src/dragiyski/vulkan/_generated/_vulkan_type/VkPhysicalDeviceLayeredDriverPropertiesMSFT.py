import ctypes

class VkPhysicalDeviceLayeredDriverPropertiesMSFT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('underlyingAPI', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'underlyingAPI': 'underlying_api',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_MSFT_layered_driver',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'underlyingAPI': 'VkLayeredDriverUnderlyingApiMSFT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_DRIVER_PROPERTIES_MSFT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_DRIVER_PROPERTIES_MSFT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceLayeredDriverPropertiesMSFT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'underlyingAPI': ctypes.c_int,
}
