import ctypes

class VkPhysicalDeviceOpacityMicromapPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxOpacity2StateSubdivisionLevel', ctypes.c_uint32),
        ('maxOpacity4StateSubdivisionLevel', ctypes.c_uint32),
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
        'maxOpacity2StateSubdivisionLevel': 'max_opacity2_state_subdivision_level',
        'maxOpacity4StateSubdivisionLevel': 'max_opacity4_state_subdivision_level',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_opacity_micromap',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPACITY_MICROMAP_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPACITY_MICROMAP_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceOpacityMicromapPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxOpacity2StateSubdivisionLevel': ctypes.c_uint32,
    'maxOpacity4StateSubdivisionLevel': ctypes.c_uint32,
}
