import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR
from .VkMicromapUsageEXT import CType as VkMicromapUsageEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displacementBiasAndScaleFormat', ctypes.c_int),
    ('displacementVectorFormat', ctypes.c_int),
    ('displacementBiasAndScaleBuffer', VkDeviceOrHostAddressConstKHR),
    ('displacementBiasAndScaleStride', ctypes.c_uint64),
    ('displacementVectorBuffer', VkDeviceOrHostAddressConstKHR),
    ('displacementVectorStride', ctypes.c_uint64),
    ('displacedMicromapPrimitiveFlags', VkDeviceOrHostAddressConstKHR),
    ('displacedMicromapPrimitiveFlagsStride', ctypes.c_uint64),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_TRIANGLES_DISPLACEMENT_MICROMAP_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'displacementBiasAndScaleFormat': {'python_name': ['displacement', 'bias', 'and', 'scale', 'format'], 'type': 'VkFormat'},
        'displacementVectorFormat': {'python_name': ['displacement', 'vector', 'format'], 'type': 'VkFormat'},
        'displacementBiasAndScaleBuffer': {'python_name': ['displacement', 'bias', 'and', 'scale', 'buffer'], 'type': 'VkDeviceOrHostAddressConstKHR'},
        'displacementBiasAndScaleStride': {'python_name': ['displacement', 'bias', 'and', 'scale', 'stride']},
        'displacementVectorBuffer': {'python_name': ['displacement', 'vector', 'buffer'], 'type': 'VkDeviceOrHostAddressConstKHR'},
        'displacementVectorStride': {'python_name': ['displacement', 'vector', 'stride']},
        'displacedMicromapPrimitiveFlags': {'python_name': ['displaced', 'micromap', 'primitive', 'flags'], 'type': 'VkDeviceOrHostAddressConstKHR'},
        'displacedMicromapPrimitiveFlagsStride': {'python_name': ['displaced', 'micromap', 'primitive', 'flags', 'stride']},
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
