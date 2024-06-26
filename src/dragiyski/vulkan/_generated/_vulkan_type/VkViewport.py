import ctypes

class VkViewport(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
        ('width', ctypes.c_float),
        ('height', ctypes.c_float),
        ('minDepth', ctypes.c_float),
        ('maxDepth', ctypes.c_float),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkCommandBufferInheritanceViewportScissorInfoNV',
        'VkPipelineViewportStateCreateInfo',
    }
    _input_of_ = {
        'vkCmdSetViewport',
        'vkCmdSetViewportWithCount',
    }
    _output_of_ = set()
    _python_name_ = {
        'x': 'x',
        'y': 'y',
        'width': 'width',
        'height': 'height',
        'minDepth': 'min_depth',
        'maxDepth': 'max_depth',
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

VkViewport._type_ = {
    'x': ctypes.c_float,
    'y': ctypes.c_float,
    'width': ctypes.c_float,
    'height': ctypes.c_float,
    'minDepth': ctypes.c_float,
    'maxDepth': ctypes.c_float,
}
