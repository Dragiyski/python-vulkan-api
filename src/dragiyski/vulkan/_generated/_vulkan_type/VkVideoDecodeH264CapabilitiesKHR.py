import ctypes

class CType(ctypes.Structure):
    pass

from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxLevelIdc', ctypes.c_int),
    ('fieldOffsetGranularity', VkOffset2D),
]

descriptor = {
    'extends': {
        'VkVideoCapabilitiesKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkOffset2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_CAPABILITIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxLevelIdc': {'python_name': ['max', 'level', 'idc'], 'type': 'StdVideoH264LevelIdc'},
        'fieldOffsetGranularity': {'python_name': ['field', 'offset', 'granularity'], 'type': 'VkOffset2D'},
    }
}
