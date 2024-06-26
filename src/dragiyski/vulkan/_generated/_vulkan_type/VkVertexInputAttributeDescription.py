import ctypes

class VkVertexInputAttributeDescription(ctypes.Structure):
    _fields_ = [
        ('location', ctypes.c_uint32),
        ('binding', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineVertexInputStateCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'location': 'location',
        'binding': 'binding',
        'format': 'format',
        'offset': 'offset',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'format': 'VkFormat',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkVertexInputAttributeDescription._type_ = {
    'location': ctypes.c_uint32,
    'binding': ctypes.c_uint32,
    'format': ctypes.c_int,
    'offset': ctypes.c_uint32,
}
