import ctypes

class VkClearColorValue(ctypes.Union):
    _fields_ = [
        ('float32', ctypes.ARRAY(ctypes.c_float, 4)),
        ('int32', ctypes.ARRAY(ctypes.c_int32, 4)),
        ('uint32', ctypes.ARRAY(ctypes.c_uint32, 4)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkClearValue',
        'VkSamplerCustomBorderColorCreateInfoEXT',
    }
    _input_of_ = {
        'vkCmdClearColorImage',
    }
    _output_of_ = set()
    _python_name_ = {
        'float32': 'float32',
        'int32': 'int32',
        'uint32': 'uint32',
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

VkClearColorValue._type_ = {
    'float32': ctypes.ARRAY(ctypes.c_float, 4),
    'int32': ctypes.ARRAY(ctypes.c_int32, 4),
    'uint32': ctypes.ARRAY(ctypes.c_uint32, 4),
}
