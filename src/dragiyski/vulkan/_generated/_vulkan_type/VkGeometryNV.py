import ctypes

class VkGeometryNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkGeometryDataNV',
    }
    _included_in_ = {
        'VkAccelerationStructureInfoNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'geometryType': 'geometry_type',
        'geometry': 'geometry',
        'flags': 'flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'geometryType': 'VkGeometryTypeKHR',
        'flags': 'VkGeometryFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_GEOMETRY_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_GEOMETRY_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkGeometryDataNV import VkGeometryDataNV

VkGeometryNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkGeometryDataNV),
    ('flags', ctypes.c_uint32),
]

VkGeometryNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'geometryType': ctypes.c_int,
    'geometry': VkGeometryDataNV,
    'flags': ctypes.c_uint32,
}
