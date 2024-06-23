import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('deviceIndexCount', ctypes.c_uint32),
    ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ('splitInstanceBindRegionCount', ctypes.c_uint32),
    ('pSplitInstanceBindRegions', ctypes.POINTER(VkRect2D)),
]

descriptor = {
    'extends': {
        'VkBindImageMemoryInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_DEVICE_GROUP_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'deviceIndexCount': {'python_name': ['device', 'index', 'count']},
        'pDeviceIndices': {'python_name': ['p', 'device', 'indices'], 'len': [['deviceIndexCount']]},
        'splitInstanceBindRegionCount': {'python_name': ['split', 'instance', 'bind', 'region', 'count']},
        'pSplitInstanceBindRegions': {'python_name': ['p', 'split', 'instance', 'bind', 'regions'], 'len': [['splitInstanceBindRegionCount']], 'type': 'VkRect2D'},
    }
}
