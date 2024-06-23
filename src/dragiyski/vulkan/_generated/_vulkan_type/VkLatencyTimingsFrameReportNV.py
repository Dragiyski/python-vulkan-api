import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentID', ctypes.c_uint64),
        ('inputSampleTimeUs', ctypes.c_uint64),
        ('simStartTimeUs', ctypes.c_uint64),
        ('simEndTimeUs', ctypes.c_uint64),
        ('renderSubmitStartTimeUs', ctypes.c_uint64),
        ('renderSubmitEndTimeUs', ctypes.c_uint64),
        ('presentStartTimeUs', ctypes.c_uint64),
        ('presentEndTimeUs', ctypes.c_uint64),
        ('driverStartTimeUs', ctypes.c_uint64),
        ('driverEndTimeUs', ctypes.c_uint64),
        ('osRenderQueueStartTimeUs', ctypes.c_uint64),
        ('osRenderQueueEndTimeUs', ctypes.c_uint64),
        ('gpuRenderStartTimeUs', ctypes.c_uint64),
        ('gpuRenderEndTimeUs', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkGetLatencyMarkerInfoNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_LATENCY_TIMINGS_FRAME_REPORT_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'presentID': {'python_name': ['present', 'id']},
        'inputSampleTimeUs': {'python_name': ['input', 'sample', 'time', 'us']},
        'simStartTimeUs': {'python_name': ['sim', 'start', 'time', 'us']},
        'simEndTimeUs': {'python_name': ['sim', 'end', 'time', 'us']},
        'renderSubmitStartTimeUs': {'python_name': ['render', 'submit', 'start', 'time', 'us']},
        'renderSubmitEndTimeUs': {'python_name': ['render', 'submit', 'end', 'time', 'us']},
        'presentStartTimeUs': {'python_name': ['present', 'start', 'time', 'us']},
        'presentEndTimeUs': {'python_name': ['present', 'end', 'time', 'us']},
        'driverStartTimeUs': {'python_name': ['driver', 'start', 'time', 'us']},
        'driverEndTimeUs': {'python_name': ['driver', 'end', 'time', 'us']},
        'osRenderQueueStartTimeUs': {'python_name': ['os', 'render', 'queue', 'start', 'time', 'us']},
        'osRenderQueueEndTimeUs': {'python_name': ['os', 'render', 'queue', 'end', 'time', 'us']},
        'gpuRenderStartTimeUs': {'python_name': ['gpu', 'render', 'start', 'time', 'us']},
        'gpuRenderEndTimeUs': {'python_name': ['gpu', 'render', 'end', 'time', 'us']},
    }
}
