import ctypes

class VkDisplayProperties2KHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDisplayPropertiesKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceDisplayProperties2KHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'displayProperties': 'display_properties',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_get_display_properties2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DISPLAY_PROPERTIES_2_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_PROPERTIES_2_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDisplayPropertiesKHR import VkDisplayPropertiesKHR

VkDisplayProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayProperties', VkDisplayPropertiesKHR),
]

VkDisplayProperties2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'displayProperties': VkDisplayPropertiesKHR,
}
