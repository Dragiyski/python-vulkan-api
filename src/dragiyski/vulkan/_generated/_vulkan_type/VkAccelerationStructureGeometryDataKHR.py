import ctypes

class VkAccelerationStructureGeometryDataKHR(ctypes.Union):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkAccelerationStructureGeometryAabbsDataKHR',
        'VkAccelerationStructureGeometryInstancesDataKHR',
        'VkAccelerationStructureGeometryTrianglesDataKHR',
    }
    _included_in_ = {
        'VkAccelerationStructureGeometryKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'triangles': 'triangles',
        'aabbs': 'aabbs',
        'instances': 'instances',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAccelerationStructureGeometryAabbsDataKHR import VkAccelerationStructureGeometryAabbsDataKHR
from .VkAccelerationStructureGeometryInstancesDataKHR import VkAccelerationStructureGeometryInstancesDataKHR
from .VkAccelerationStructureGeometryTrianglesDataKHR import VkAccelerationStructureGeometryTrianglesDataKHR

VkAccelerationStructureGeometryDataKHR._fields_ = [
    ('triangles', VkAccelerationStructureGeometryTrianglesDataKHR),
    ('aabbs', VkAccelerationStructureGeometryAabbsDataKHR),
    ('instances', VkAccelerationStructureGeometryInstancesDataKHR),
]

VkAccelerationStructureGeometryDataKHR._type_ = {
    'triangles': VkAccelerationStructureGeometryTrianglesDataKHR,
    'aabbs': VkAccelerationStructureGeometryAabbsDataKHR,
    'instances': VkAccelerationStructureGeometryInstancesDataKHR,
}
