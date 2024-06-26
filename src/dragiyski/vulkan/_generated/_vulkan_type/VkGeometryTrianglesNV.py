import ctypes

class VkGeometryTrianglesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vertexData', ctypes.c_void_p),
        ('vertexOffset', ctypes.c_uint64),
        ('vertexCount', ctypes.c_uint32),
        ('vertexStride', ctypes.c_uint64),
        ('vertexFormat', ctypes.c_int),
        ('indexData', ctypes.c_void_p),
        ('indexOffset', ctypes.c_uint64),
        ('indexCount', ctypes.c_uint32),
        ('indexType', ctypes.c_int),
        ('transformData', ctypes.c_void_p),
        ('transformOffset', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkGeometryDataNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'vertexData': 'vertex_data',
        'vertexOffset': 'vertex_offset',
        'vertexCount': 'vertex_count',
        'vertexStride': 'vertex_stride',
        'vertexFormat': 'vertex_format',
        'indexData': 'index_data',
        'indexOffset': 'index_offset',
        'indexCount': 'index_count',
        'indexType': 'index_type',
        'transformData': 'transform_data',
        'transformOffset': 'transform_offset',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'vertexFormat': 'VkFormat',
        'indexType': 'VkIndexType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_GEOMETRY_TRIANGLES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_GEOMETRY_TRIANGLES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkGeometryTrianglesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vertexData': ctypes.c_void_p,
    'vertexOffset': ctypes.c_uint64,
    'vertexCount': ctypes.c_uint32,
    'vertexStride': ctypes.c_uint64,
    'vertexFormat': ctypes.c_int,
    'indexData': ctypes.c_void_p,
    'indexOffset': ctypes.c_uint64,
    'indexCount': ctypes.c_uint32,
    'indexType': ctypes.c_int,
    'transformData': ctypes.c_void_p,
    'transformOffset': ctypes.c_uint64,
}
