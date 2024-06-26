import ctypes

class VkGetLatencyMarkerInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkLatencyTimingsFrameReportNV',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetLatencyTimingsNV',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'timingCount': 'timing_count',
        'pTimings': 'timings',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_low_latency2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_GET_LATENCY_MARKER_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_GET_LATENCY_MARKER_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkLatencyTimingsFrameReportNV import VkLatencyTimingsFrameReportNV

VkGetLatencyMarkerInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('timingCount', ctypes.c_uint32),
    ('pTimings', ctypes.POINTER(VkLatencyTimingsFrameReportNV)),
]

VkGetLatencyMarkerInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'timingCount': ctypes.c_uint32,
    'pTimings': ctypes.POINTER(VkLatencyTimingsFrameReportNV),
}
