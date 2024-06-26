import ctypes

class VkLatencySleepModeInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('lowLatencyMode', ctypes.c_uint32),
        ('lowLatencyBoost', ctypes.c_uint32),
        ('minimumIntervalUs', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkSetLatencySleepModeNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'lowLatencyMode': 'low_latency_mode',
        'lowLatencyBoost': 'low_latency_boost',
        'minimumIntervalUs': 'minimum_interval_us',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_low_latency2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_LATENCY_SLEEP_MODE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_LATENCY_SLEEP_MODE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkLatencySleepModeInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'lowLatencyMode': ctypes.c_uint32,
    'lowLatencyBoost': ctypes.c_uint32,
    'minimumIntervalUs': ctypes.c_uint32,
}
