import ctypes

class VkPastPresentationTimingGOOGLE(ctypes.Structure):
    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
        ('actualPresentTime', ctypes.c_uint64),
        ('earliestPresentTime', ctypes.c_uint64),
        ('presentMargin', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPastPresentationTimingGOOGLE',
    }
    _python_name_ = {
        'presentID': 'present_id',
        'desiredPresentTime': 'desired_present_time',
        'actualPresentTime': 'actual_present_time',
        'earliestPresentTime': 'earliest_present_time',
        'presentMargin': 'present_margin',
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

VkPastPresentationTimingGOOGLE._type_ = {
    'presentID': ctypes.c_uint32,
    'desiredPresentTime': ctypes.c_uint64,
    'actualPresentTime': ctypes.c_uint64,
    'earliestPresentTime': ctypes.c_uint64,
    'presentMargin': ctypes.c_uint64,
}
