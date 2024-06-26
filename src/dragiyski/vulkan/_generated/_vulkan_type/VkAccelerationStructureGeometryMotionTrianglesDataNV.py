import ctypes

class VkAccelerationStructureGeometryMotionTrianglesDataNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkAccelerationStructureGeometryTrianglesDataKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceOrHostAddressConstKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'vertexData': 'vertex_data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing_motion_blur',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_MOTION_TRIANGLES_DATA_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_MOTION_TRIANGLES_DATA_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryMotionTrianglesDataNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexData', VkDeviceOrHostAddressConstKHR),
]

VkAccelerationStructureGeometryMotionTrianglesDataNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vertexData': VkDeviceOrHostAddressConstKHR,
}
