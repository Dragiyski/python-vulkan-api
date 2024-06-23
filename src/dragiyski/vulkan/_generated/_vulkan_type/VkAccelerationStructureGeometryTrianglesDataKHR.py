import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkAccelerationStructureGeometryMotionTrianglesDataNV',
        'VkAccelerationStructureTrianglesDisplacementMicromapNV',
        'VkAccelerationStructureTrianglesOpacityMicromapEXT',
    },
    'includes': {
        'VkDeviceOrHostAddressConstKHR',
    },
    'included_in': {
        'VkAccelerationStructureGeometryDataKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_TRIANGLES_DATA_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'vertexFormat': {'python_name': ['vertex', 'format'], 'type': 'VkFormat'},
        'vertexData': {'python_name': ['vertex', 'data'], 'type': 'VkDeviceOrHostAddressConstKHR'},
        'vertexStride': {'python_name': ['vertex', 'stride']},
        'maxVertex': {'python_name': ['max', 'vertex']},
        'indexType': {'python_name': ['index', 'type'], 'type': 'VkIndexType'},
        'indexData': {'python_name': ['index', 'data'], 'type': 'VkDeviceOrHostAddressConstKHR'},
        'transformData': {'python_name': ['transform', 'data'], 'type': 'VkDeviceOrHostAddressConstKHR'},
    }
}
