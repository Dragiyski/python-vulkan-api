import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('arrayOfPointers', ctypes.c_uint32),
    ('data', VkDeviceOrHostAddressConstKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDeviceOrHostAddressConstKHR',
    },
    'included_in': {
        'VkAccelerationStructureGeometryDataKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_INSTANCES_DATA_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'arrayOfPointers': {'python_name': ['array', 'of', 'pointers']},
        'data': {'python_name': ['data'], 'type': 'VkDeviceOrHostAddressConstKHR'},
    }
}
