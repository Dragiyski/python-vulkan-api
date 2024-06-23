import ctypes

class CType(ctypes.Structure):
    pass

from .VkAccelerationStructureGeometryKHR import CType as VkAccelerationStructureGeometryKHR
from .VkDeviceOrHostAddressKHR import CType as VkDeviceOrHostAddressKHR

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkAccelerationStructureGeometryKHR',
        'VkDeviceOrHostAddressKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkBuildAccelerationStructuresKHR',
        'vkCmdBuildAccelerationStructuresIndirectKHR',
        'vkCmdBuildAccelerationStructuresKHR',
        'vkGetAccelerationStructureBuildSizesKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_GEOMETRY_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'type': {'python_name': ['type'], 'type': 'VkAccelerationStructureTypeKHR'},
        'flags': {'python_name': ['flags'], 'type': 'VkBuildAccelerationStructureFlagsKHR'},
        'mode': {'python_name': ['mode'], 'type': 'VkBuildAccelerationStructureModeKHR'},
        'srcAccelerationStructure': {'python_name': ['src', 'acceleration', 'structure']},
        'dstAccelerationStructure': {'python_name': ['dst', 'acceleration', 'structure']},
        'geometryCount': {'python_name': ['geometry', 'count']},
        'pGeometries': {'python_name': ['p', 'geometries'], 'len': [['geometryCount']], 'type': 'VkAccelerationStructureGeometryKHR'},
        'ppGeometries': {'python_name': ['pp', 'geometries'], 'len': [['geometryCount'], ['1']], 'type': 'VkAccelerationStructureGeometryKHR'},
        'scratchData': {'python_name': ['scratch', 'data'], 'type': 'VkDeviceOrHostAddressKHR'},
    }
}
