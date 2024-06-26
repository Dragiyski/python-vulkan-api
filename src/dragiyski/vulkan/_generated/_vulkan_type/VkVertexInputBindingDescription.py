import ctypes

class VkVertexInputBindingDescription(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('inputRate', ctypes.c_int),
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
        'binding': 'binding',
        'stride': 'stride',
        'inputRate': 'input_rate',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'inputRate': 'VkVertexInputRate',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkVertexInputBindingDescription._type_ = {
    'binding': ctypes.c_uint32,
    'stride': ctypes.c_uint32,
    'inputRate': ctypes.c_int,
}
