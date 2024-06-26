import ctypes

class VkCoarseSampleLocationNV(ctypes.Structure):
    _fields_ = [
        ('pixelX', ctypes.c_uint32),
        ('pixelY', ctypes.c_uint32),
        ('sample', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkCoarseSampleOrderCustomNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'pixelX': 'pixel_x',
        'pixelY': 'pixel_y',
        'sample': 'sample',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_shading_rate_image',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkCoarseSampleLocationNV._type_ = {
    'pixelX': ctypes.c_uint32,
    'pixelY': ctypes.c_uint32,
    'sample': ctypes.c_uint32,
}
