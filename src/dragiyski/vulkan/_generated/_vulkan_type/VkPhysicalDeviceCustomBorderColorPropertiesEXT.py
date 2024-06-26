import ctypes

class VkPhysicalDeviceCustomBorderColorPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxCustomBorderColorSamplers', ctypes.c_uint32),
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
        'maxCustomBorderColorSamplers': 'max_custom_border_color_samplers',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_custom_border_color',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUSTOM_BORDER_COLOR_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUSTOM_BORDER_COLOR_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceCustomBorderColorPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxCustomBorderColorSamplers': ctypes.c_uint32,
}
