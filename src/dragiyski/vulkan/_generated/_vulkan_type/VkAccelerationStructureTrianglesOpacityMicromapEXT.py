import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR
from .VkMicromapUsageEXT import CType as VkMicromapUsageEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('indexType', ctypes.c_int),
    ('indexBuffer', VkDeviceOrHostAddressConstKHR),
    ('indexStride', ctypes.c_uint64),
    ('baseTriangle', ctypes.c_uint32),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('micromap', ctypes.c_void_p),
]

descriptor = {
    'extends': {
        'VkAccelerationStructureGeometryTrianglesDataKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkDeviceOrHostAddressConstKHR',
        'VkMicromapUsageEXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_TRIANGLES_OPACITY_MICROMAP_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'indexType': {'python_name': ['index', 'type'], 'type': 'VkIndexType'},
        'indexBuffer': {'python_name': ['index', 'buffer'], 'type': 'VkDeviceOrHostAddressConstKHR'},
        'indexStride': {'python_name': ['index', 'stride']},
        'baseTriangle': {'python_name': ['base', 'triangle']},
        'usageCountsCount': {'python_name': ['usage', 'counts', 'count']},
        'pUsageCounts': {'python_name': ['p', 'usage', 'counts'], 'len': [['usageCountsCount']], 'type': 'VkMicromapUsageEXT'},
        'ppUsageCounts': {'python_name': ['pp', 'usage', 'counts'], 'len': [['usageCountsCount'], ['1']], 'type': 'VkMicromapUsageEXT'},
        'micromap': {'python_name': ['micromap']},
    }
}
