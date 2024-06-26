import ctypes

class VkPipelineDepthStencilStateCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkStencilOpState',
    }
    _included_in_ = {
        'VkGraphicsPipelineCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'depthTestEnable': 'depth_test_enable',
        'depthWriteEnable': 'depth_write_enable',
        'depthCompareOp': 'depth_compare_op',
        'depthBoundsTestEnable': 'depth_bounds_test_enable',
        'stencilTestEnable': 'stencil_test_enable',
        'front': 'front',
        'back': 'back',
        'minDepthBounds': 'min_depth_bounds',
        'maxDepthBounds': 'max_depth_bounds',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineDepthStencilStateCreateFlags',
        'depthCompareOp': 'VkCompareOp',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_DEPTH_STENCIL_STATE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_DEPTH_STENCIL_STATE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkStencilOpState import VkStencilOpState

VkPipelineDepthStencilStateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('depthTestEnable', ctypes.c_uint32),
    ('depthWriteEnable', ctypes.c_uint32),
    ('depthCompareOp', ctypes.c_int),
    ('depthBoundsTestEnable', ctypes.c_uint32),
    ('stencilTestEnable', ctypes.c_uint32),
    ('front', VkStencilOpState),
    ('back', VkStencilOpState),
    ('minDepthBounds', ctypes.c_float),
    ('maxDepthBounds', ctypes.c_float),
]

VkPipelineDepthStencilStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'depthTestEnable': ctypes.c_uint32,
    'depthWriteEnable': ctypes.c_uint32,
    'depthCompareOp': ctypes.c_int,
    'depthBoundsTestEnable': ctypes.c_uint32,
    'stencilTestEnable': ctypes.c_uint32,
    'front': VkStencilOpState,
    'back': VkStencilOpState,
    'minDepthBounds': ctypes.c_float,
    'maxDepthBounds': ctypes.c_float,
}
