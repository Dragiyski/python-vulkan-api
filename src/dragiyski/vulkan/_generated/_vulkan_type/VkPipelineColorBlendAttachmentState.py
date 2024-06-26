import ctypes

class VkPipelineColorBlendAttachmentState(ctypes.Structure):
    _fields_ = [
        ('blendEnable', ctypes.c_uint32),
        ('srcColorBlendFactor', ctypes.c_int),
        ('dstColorBlendFactor', ctypes.c_int),
        ('colorBlendOp', ctypes.c_int),
        ('srcAlphaBlendFactor', ctypes.c_int),
        ('dstAlphaBlendFactor', ctypes.c_int),
        ('alphaBlendOp', ctypes.c_int),
        ('colorWriteMask', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineColorBlendStateCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'blendEnable': 'blend_enable',
        'srcColorBlendFactor': 'src_color_blend_factor',
        'dstColorBlendFactor': 'dst_color_blend_factor',
        'colorBlendOp': 'color_blend_op',
        'srcAlphaBlendFactor': 'src_alpha_blend_factor',
        'dstAlphaBlendFactor': 'dst_alpha_blend_factor',
        'alphaBlendOp': 'alpha_blend_op',
        'colorWriteMask': 'color_write_mask',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'srcColorBlendFactor': 'VkBlendFactor',
        'dstColorBlendFactor': 'VkBlendFactor',
        'colorBlendOp': 'VkBlendOp',
        'srcAlphaBlendFactor': 'VkBlendFactor',
        'dstAlphaBlendFactor': 'VkBlendFactor',
        'alphaBlendOp': 'VkBlendOp',
        'colorWriteMask': 'VkColorComponentFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineColorBlendAttachmentState._type_ = {
    'blendEnable': ctypes.c_uint32,
    'srcColorBlendFactor': ctypes.c_int,
    'dstColorBlendFactor': ctypes.c_int,
    'colorBlendOp': ctypes.c_int,
    'srcAlphaBlendFactor': ctypes.c_int,
    'dstAlphaBlendFactor': ctypes.c_int,
    'alphaBlendOp': ctypes.c_int,
    'colorWriteMask': ctypes.c_uint32,
}
