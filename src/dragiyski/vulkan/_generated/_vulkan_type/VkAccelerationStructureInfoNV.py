import ctypes

class VkAccelerationStructureInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkGeometryNV',
    }
    _included_in_ = {
        'VkAccelerationStructureCreateInfoNV',
    }
    _input_of_ = {
        'vkCmdBuildAccelerationStructureNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'type': 'type',
        'flags': 'flags',
        'instanceCount': 'instance_count',
        'geometryCount': 'geometry_count',
        'pGeometries': 'geometries',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'type': 'VkAccelerationStructureTypeKHR',
        'flags': 'VkBuildAccelerationStructureFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkGeometryNV import VkGeometryNV

VkAccelerationStructureInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('instanceCount', ctypes.c_uint32),
    ('geometryCount', ctypes.c_uint32),
    ('pGeometries', ctypes.POINTER(VkGeometryNV)),
]

VkAccelerationStructureInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'type': ctypes.c_int,
    'flags': ctypes.c_uint32,
    'instanceCount': ctypes.c_uint32,
    'geometryCount': ctypes.c_uint32,
    'pGeometries': ctypes.POINTER(VkGeometryNV),
}
