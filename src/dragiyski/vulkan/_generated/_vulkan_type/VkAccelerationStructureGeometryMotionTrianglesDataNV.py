import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexData', VkDeviceOrHostAddressConstKHR),
]

descriptor = {
    'extends': {
        'VkAccelerationStructureGeometryTrianglesDataKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkDeviceOrHostAddressConstKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_MOTION_TRIANGLES_DATA_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'vertexData': {'python_name': ['vertex', 'data'], 'type': 'VkDeviceOrHostAddressConstKHR'},
    }
}
