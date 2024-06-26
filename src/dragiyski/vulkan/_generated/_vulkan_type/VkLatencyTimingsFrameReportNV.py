import ctypes

class VkLatencyTimingsFrameReportNV(ctypes.Structure):
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

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkGetLatencyMarkerInfoNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'presentID': 'present_id',
        'inputSampleTimeUs': 'input_sample_time_us',
        'simStartTimeUs': 'sim_start_time_us',
        'simEndTimeUs': 'sim_end_time_us',
        'renderSubmitStartTimeUs': 'render_submit_start_time_us',
        'renderSubmitEndTimeUs': 'render_submit_end_time_us',
        'presentStartTimeUs': 'present_start_time_us',
        'presentEndTimeUs': 'present_end_time_us',
        'driverStartTimeUs': 'driver_start_time_us',
        'driverEndTimeUs': 'driver_end_time_us',
        'osRenderQueueStartTimeUs': 'os_render_queue_start_time_us',
        'osRenderQueueEndTimeUs': 'os_render_queue_end_time_us',
        'gpuRenderStartTimeUs': 'gpu_render_start_time_us',
        'gpuRenderEndTimeUs': 'gpu_render_end_time_us',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_low_latency2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_LATENCY_TIMINGS_FRAME_REPORT_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_LATENCY_TIMINGS_FRAME_REPORT_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkLatencyTimingsFrameReportNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentID': ctypes.c_uint64,
    'inputSampleTimeUs': ctypes.c_uint64,
    'simStartTimeUs': ctypes.c_uint64,
    'simEndTimeUs': ctypes.c_uint64,
    'renderSubmitStartTimeUs': ctypes.c_uint64,
    'renderSubmitEndTimeUs': ctypes.c_uint64,
    'presentStartTimeUs': ctypes.c_uint64,
    'presentEndTimeUs': ctypes.c_uint64,
    'driverStartTimeUs': ctypes.c_uint64,
    'driverEndTimeUs': ctypes.c_uint64,
    'osRenderQueueStartTimeUs': ctypes.c_uint64,
    'osRenderQueueEndTimeUs': ctypes.c_uint64,
    'gpuRenderStartTimeUs': ctypes.c_uint64,
    'gpuRenderEndTimeUs': ctypes.c_uint64,
}
