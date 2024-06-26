import ctypes

class VkAccelerationStructureBuildGeometryInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkAccelerationStructureGeometryKHR',
        'VkDeviceOrHostAddressKHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkBuildAccelerationStructuresKHR',
        'vkCmdBuildAccelerationStructuresIndirectKHR',
        'vkCmdBuildAccelerationStructuresKHR',
        'vkGetAccelerationStructureBuildSizesKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'type': 'type',
        'flags': 'flags',
        'mode': 'mode',
        'srcAccelerationStructure': 'src_acceleration_structure',
        'dstAccelerationStructure': 'dst_acceleration_structure',
        'geometryCount': 'geometry_count',
        'pGeometries': 'geometries',
        'ppGeometries': 'geometries',
        'scratchData': 'scratch_data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'type': 'VkAccelerationStructureTypeKHR',
        'flags': 'VkBuildAccelerationStructureFlagsKHR',
        'mode': 'VkBuildAccelerationStructureModeKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_GEOMETRY_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_GEOMETRY_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAccelerationStructureGeometryKHR import VkAccelerationStructureGeometryKHR
from .VkDeviceOrHostAddressKHR import VkDeviceOrHostAddressKHR

VkAccelerationStructureBuildGeometryInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('mode', ctypes.c_int),
    ('srcAccelerationStructure', ctypes.c_void_p),
    ('dstAccelerationStructure', ctypes.c_void_p),
    ('geometryCount', ctypes.c_uint32),
    ('pGeometries', ctypes.POINTER(VkAccelerationStructureGeometryKHR)),
    ('ppGeometries', ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureGeometryKHR))),
    ('scratchData', VkDeviceOrHostAddressKHR),
]

VkAccelerationStructureBuildGeometryInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'type': ctypes.c_int,
    'flags': ctypes.c_uint32,
    'mode': ctypes.c_int,
    'srcAccelerationStructure': ctypes.c_void_p,
    'dstAccelerationStructure': ctypes.c_void_p,
    'geometryCount': ctypes.c_uint32,
    'pGeometries': ctypes.POINTER(VkAccelerationStructureGeometryKHR),
    'ppGeometries': ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureGeometryKHR)),
    'scratchData': VkDeviceOrHostAddressKHR,
}
