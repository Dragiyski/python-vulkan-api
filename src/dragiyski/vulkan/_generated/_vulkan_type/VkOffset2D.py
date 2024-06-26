import ctypes

class VkOffset2D(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDisplayPlaneCapabilitiesKHR',
        'VkImageViewSampleWeightCreateInfoQCOM',
        'VkRect2D',
        'VkRectLayerKHR',
        'VkSubpassFragmentDensityMapOffsetEndInfoQCOM',
        'VkTilePropertiesQCOM',
        'VkVideoDecodeH264CapabilitiesKHR',
        'VkVideoPictureResourceInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'x': 'x',
        'y': 'y',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkOffset2D._type_ = {
    'x': ctypes.c_int32,
    'y': ctypes.c_int32,
}
