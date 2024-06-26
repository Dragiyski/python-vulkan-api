import ctypes

class VkAccelerationStructureGeometryTrianglesDataKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkAccelerationStructureGeometryMotionTrianglesDataNV',
        'VkAccelerationStructureTrianglesDisplacementMicromapNV',
        'VkAccelerationStructureTrianglesOpacityMicromapEXT',
    }
    _includes_ = {
        'VkDeviceOrHostAddressConstKHR',
    }
    _included_in_ = {
        'VkAccelerationStructureGeometryDataKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'vertexFormat': 'vertex_format',
        'vertexData': 'vertex_data',
        'vertexStride': 'vertex_stride',
        'maxVertex': 'max_vertex',
        'indexType': 'index_type',
        'indexData': 'index_data',
        'transformData': 'transform_data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'vertexFormat': 'VkFormat',
        'indexType': 'VkIndexType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_TRIANGLES_DATA_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_TRIANGLES_DATA_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryTrianglesDataKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexFormat', ctypes.c_int),
    ('vertexData', VkDeviceOrHostAddressConstKHR),
    ('vertexStride', ctypes.c_uint64),
    ('maxVertex', ctypes.c_uint32),
    ('indexType', ctypes.c_int),
    ('indexData', VkDeviceOrHostAddressConstKHR),
    ('transformData', VkDeviceOrHostAddressConstKHR),
]

VkAccelerationStructureGeometryTrianglesDataKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vertexFormat': ctypes.c_int,
    'vertexData': VkDeviceOrHostAddressConstKHR,
    'vertexStride': ctypes.c_uint64,
    'maxVertex': ctypes.c_uint32,
    'indexType': ctypes.c_int,
    'indexData': VkDeviceOrHostAddressConstKHR,
    'transformData': VkDeviceOrHostAddressConstKHR,
}
