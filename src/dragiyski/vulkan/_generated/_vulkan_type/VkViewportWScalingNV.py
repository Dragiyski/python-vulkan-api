import ctypes

class VkViewportWScalingNV(ctypes.Structure):
    _fields_ = [
        ('xcoeff', ctypes.c_float),
        ('ycoeff', ctypes.c_float),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineViewportWScalingStateCreateInfoNV',
    }
    _input_of_ = {
        'vkCmdSetViewportWScalingNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'xcoeff': 'xcoeff',
        'ycoeff': 'ycoeff',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_clip_space_w_scaling',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkViewportWScalingNV._type_ = {
    'xcoeff': ctypes.c_float,
    'ycoeff': ctypes.c_float,
}
