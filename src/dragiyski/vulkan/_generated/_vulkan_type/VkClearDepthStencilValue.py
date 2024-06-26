import ctypes

class VkClearDepthStencilValue(ctypes.Structure):
    _fields_ = [
        ('depth', ctypes.c_float),
        ('stencil', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkClearValue',
    }
    _input_of_ = {
        'vkCmdClearDepthStencilImage',
    }
    _output_of_ = set()
    _python_name_ = {
        'depth': 'depth',
        'stencil': 'stencil',
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

VkClearDepthStencilValue._type_ = {
    'depth': ctypes.c_float,
    'stencil': ctypes.c_uint32,
}
