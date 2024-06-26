import ctypes

class VkDisplaySurfaceCreateInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateDisplayPlaneSurfaceKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'displayMode': 'display_mode',
        'planeIndex': 'plane_index',
        'planeStackIndex': 'plane_stack_index',
        'transform': 'transform',
        'globalAlpha': 'global_alpha',
        'alphaMode': 'alpha_mode',
        'imageExtent': 'image_extent',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_display',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDisplaySurfaceCreateFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DISPLAY_SURFACE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_SURFACE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkDisplaySurfaceCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('displayMode', ctypes.c_void_p),
    ('planeIndex', ctypes.c_uint32),
    ('planeStackIndex', ctypes.c_uint32),
    ('transform', ctypes.c_uint32),
    ('globalAlpha', ctypes.c_float),
    ('alphaMode', ctypes.c_uint32),
    ('imageExtent', VkExtent2D),
]

VkDisplaySurfaceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'displayMode': ctypes.c_void_p,
    'planeIndex': ctypes.c_uint32,
    'planeStackIndex': ctypes.c_uint32,
    'transform': ctypes.c_uint32,
    'globalAlpha': ctypes.c_float,
    'alphaMode': ctypes.c_uint32,
    'imageExtent': VkExtent2D,
}
