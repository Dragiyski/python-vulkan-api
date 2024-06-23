import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR
from .VkDeviceOrHostAddressKHR import CType as VkDeviceOrHostAddressKHR
from .VkMicromapUsageEXT import CType as VkMicromapUsageEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('mode', ctypes.c_int),
    ('dstMicromap', ctypes.c_void_p),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('data', VkDeviceOrHostAddressConstKHR),
    ('scratchData', VkDeviceOrHostAddressKHR),
    ('triangleArray', VkDeviceOrHostAddressConstKHR),
    ('triangleArrayStride', ctypes.c_uint64),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDeviceOrHostAddressConstKHR',
        'VkDeviceOrHostAddressKHR',
        'VkMicromapUsageEXT',
    },
    'included_in': set(),
    'input_of': {
        'vkBuildMicromapsEXT',
        'vkCmdBuildMicromapsEXT',
        'vkGetMicromapBuildSizesEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MICROMAP_BUILD_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'type': {'python_name': ['type'], 'type': 'VkMicromapTypeEXT'},
        'flags': {'python_name': ['flags'], 'type': 'VkBuildMicromapFlagsEXT'},
        'mode': {'python_name': ['mode'], 'type': 'VkBuildMicromapModeEXT'},
        'dstMicromap': {'python_name': ['dst', 'micromap']},
        'usageCountsCount': {'python_name': ['usage', 'counts', 'count']},
        'pUsageCounts': {'python_name': ['p', 'usage', 'counts'], 'len': [['usageCountsCount']], 'type': 'VkMicromapUsageEXT'},
        'ppUsageCounts': {'python_name': ['pp', 'usage', 'counts'], 'len': [['usageCountsCount'], ['1']], 'type': 'VkMicromapUsageEXT'},
        'data': {'python_name': ['data'], 'type': 'VkDeviceOrHostAddressConstKHR'},
        'scratchData': {'python_name': ['scratch', 'data'], 'type': 'VkDeviceOrHostAddressKHR'},
        'triangleArray': {'python_name': ['triangle', 'array'], 'type': 'VkDeviceOrHostAddressConstKHR'},
        'triangleArrayStride': {'python_name': ['triangle', 'array', 'stride']},
    }
}
