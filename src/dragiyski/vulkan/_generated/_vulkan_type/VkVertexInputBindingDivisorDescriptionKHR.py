import ctypes

class VkVertexInputBindingDivisorDescriptionKHR(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('divisor', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineVertexInputDivisorStateCreateInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'binding': 'binding',
        'divisor': 'divisor',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_vertex_attribute_divisor',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkVertexInputBindingDivisorDescriptionKHR._type_ = {
    'binding': ctypes.c_uint32,
    'divisor': ctypes.c_uint32,
}
