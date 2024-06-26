import ctypes

class VkPhysicalDeviceLineRasterizationFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rectangularLines', ctypes.c_uint32),
        ('bresenhamLines', ctypes.c_uint32),
        ('smoothLines', ctypes.c_uint32),
        ('stippledRectangularLines', ctypes.c_uint32),
        ('stippledBresenhamLines', ctypes.c_uint32),
        ('stippledSmoothLines', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'rectangularLines': 'rectangular_lines',
        'bresenhamLines': 'bresenham_lines',
        'smoothLines': 'smooth_lines',
        'stippledRectangularLines': 'stippled_rectangular_lines',
        'stippledBresenhamLines': 'stippled_bresenham_lines',
        'stippledSmoothLines': 'stippled_smooth_lines',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_line_rasterization',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_FEATURES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_FEATURES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceLineRasterizationFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rectangularLines': ctypes.c_uint32,
    'bresenhamLines': ctypes.c_uint32,
    'smoothLines': ctypes.c_uint32,
    'stippledRectangularLines': ctypes.c_uint32,
    'stippledBresenhamLines': ctypes.c_uint32,
    'stippledSmoothLines': ctypes.c_uint32,
}
