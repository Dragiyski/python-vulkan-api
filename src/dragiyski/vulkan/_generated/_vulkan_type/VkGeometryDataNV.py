import ctypes

class VkGeometryDataNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkGeometryAABBNV',
        'VkGeometryTrianglesNV',
    }
    _included_in_ = {
        'VkGeometryNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'triangles': 'triangles',
        'aabbs': 'aabbs',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkGeometryAABBNV import VkGeometryAABBNV
from .VkGeometryTrianglesNV import VkGeometryTrianglesNV

VkGeometryDataNV._fields_ = [
    ('triangles', VkGeometryTrianglesNV),
    ('aabbs', VkGeometryAABBNV),
]

VkGeometryDataNV._type_ = {
    'triangles': VkGeometryTrianglesNV,
    'aabbs': VkGeometryAABBNV,
}
