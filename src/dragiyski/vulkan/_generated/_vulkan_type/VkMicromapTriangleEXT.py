import ctypes

class VkMicromapTriangleEXT(ctypes.Structure):
    _fields_ = [
        ('dataOffset', ctypes.c_uint32),
        ('subdivisionLevel', ctypes.c_uint16),
        ('format', ctypes.c_uint16),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'dataOffset': 'data_offset',
        'subdivisionLevel': 'subdivision_level',
        'format': 'format',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_opacity_micromap',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkMicromapTriangleEXT._type_ = {
    'dataOffset': ctypes.c_uint32,
    'subdivisionLevel': ctypes.c_uint16,
    'format': ctypes.c_uint16,
}
