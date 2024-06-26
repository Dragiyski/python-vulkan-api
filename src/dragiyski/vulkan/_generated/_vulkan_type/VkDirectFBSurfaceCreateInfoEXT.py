import ctypes

class VkDirectFBSurfaceCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('dfb', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateDirectFBSurfaceEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'dfb': 'dfb',
        'surface': 'surface',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_directfb_surface',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDirectFBSurfaceCreateFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DIRECTFB_SURFACE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DIRECTFB_SURFACE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDirectFBSurfaceCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'dfb': ctypes.c_void_p,
    'surface': ctypes.c_void_p,
}
