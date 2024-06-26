import ctypes

class VkPresentTimeGOOGLE(ctypes.Structure):
    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPresentTimesInfoGOOGLE',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'presentID': 'present_id',
        'desiredPresentTime': 'desired_present_time',
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

VkPresentTimeGOOGLE._type_ = {
    'presentID': ctypes.c_uint32,
    'desiredPresentTime': ctypes.c_uint64,
}
