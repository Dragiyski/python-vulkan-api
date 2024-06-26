import ctypes

class VkStencilOpState(ctypes.Structure):
    _fields_ = [
        ('failOp', ctypes.c_int),
        ('passOp', ctypes.c_int),
        ('depthFailOp', ctypes.c_int),
        ('compareOp', ctypes.c_int),
        ('compareMask', ctypes.c_uint32),
        ('writeMask', ctypes.c_uint32),
        ('reference', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineDepthStencilStateCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'failOp': 'fail_op',
        'passOp': 'pass_op',
        'depthFailOp': 'depth_fail_op',
        'compareOp': 'compare_op',
        'compareMask': 'compare_mask',
        'writeMask': 'write_mask',
        'reference': 'reference',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'failOp': 'VkStencilOp',
        'passOp': 'VkStencilOp',
        'depthFailOp': 'VkStencilOp',
        'compareOp': 'VkCompareOp',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkStencilOpState._type_ = {
    'failOp': ctypes.c_int,
    'passOp': ctypes.c_int,
    'depthFailOp': ctypes.c_int,
    'compareOp': ctypes.c_int,
    'compareMask': ctypes.c_uint32,
    'writeMask': ctypes.c_uint32,
    'reference': ctypes.c_uint32,
}
