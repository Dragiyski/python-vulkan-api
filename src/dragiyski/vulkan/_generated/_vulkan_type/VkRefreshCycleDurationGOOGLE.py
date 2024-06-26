import ctypes

class VkRefreshCycleDurationGOOGLE(ctypes.Structure):
    _fields_ = [
        ('refreshDuration', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetRefreshCycleDurationGOOGLE',
    }
    _python_name_ = {
        'refreshDuration': 'refresh_duration',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_GOOGLE_display_timing',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkRefreshCycleDurationGOOGLE._type_ = {
    'refreshDuration': ctypes.c_uint64,
}
