import ctypes

class VkSurfacePresentModeCompatibilityEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentModeCount', ctypes.c_uint32),
        ('pPresentModes', ctypes.POINTER(ctypes.c_int)),
    ]

    _init_ = []
    _extends_ = {
        'VkSurfaceCapabilities2KHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'presentModeCount': 'present_mode_count',
        'pPresentModes': 'present_modes',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_surface_maintenance1',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pPresentModes': 'VkPresentModeKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SURFACE_PRESENT_MODE_COMPATIBILITY_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_PRESENT_MODE_COMPATIBILITY_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkSurfacePresentModeCompatibilityEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentModeCount': ctypes.c_uint32,
    'pPresentModes': ctypes.POINTER(ctypes.c_int),
}
