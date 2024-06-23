import ctypes

class CType(ctypes.Structure):
    pass

from .VkLatencyTimingsFrameReportNV import CType as VkLatencyTimingsFrameReportNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('timingCount', ctypes.c_uint32),
    ('pTimings', ctypes.POINTER(VkLatencyTimingsFrameReportNV)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkLatencyTimingsFrameReportNV',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetLatencyTimingsNV',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_GET_LATENCY_MARKER_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'timingCount': {'python_name': ['timing', 'count']},
        'pTimings': {'python_name': ['p', 'timings'], 'len': [['timingCount']], 'type': 'VkLatencyTimingsFrameReportNV'},
    }
}
