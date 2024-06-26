import ctypes

class VkXYColorEXT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkHdrMetadataEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'x': 'x',
        'y': 'y',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_hdr_metadata',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkXYColorEXT._type_ = {
    'x': ctypes.c_float,
    'y': ctypes.c_float,
}
