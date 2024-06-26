import ctypes

class VkColorBlendEquationEXT(ctypes.Structure):
    _fields_ = [
        ('srcColorBlendFactor', ctypes.c_int),
        ('dstColorBlendFactor', ctypes.c_int),
        ('colorBlendOp', ctypes.c_int),
        ('srcAlphaBlendFactor', ctypes.c_int),
        ('dstAlphaBlendFactor', ctypes.c_int),
        ('alphaBlendOp', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdSetColorBlendEquationEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'srcColorBlendFactor': 'src_color_blend_factor',
        'dstColorBlendFactor': 'dst_color_blend_factor',
        'colorBlendOp': 'color_blend_op',
        'srcAlphaBlendFactor': 'src_alpha_blend_factor',
        'dstAlphaBlendFactor': 'dst_alpha_blend_factor',
        'alphaBlendOp': 'alpha_blend_op',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_extended_dynamic_state3',
        'VK_EXT_shader_object',
    }
    _vk_enum_ = {
        'srcColorBlendFactor': 'VkBlendFactor',
        'dstColorBlendFactor': 'VkBlendFactor',
        'colorBlendOp': 'VkBlendOp',
        'srcAlphaBlendFactor': 'VkBlendFactor',
        'dstAlphaBlendFactor': 'VkBlendFactor',
        'alphaBlendOp': 'VkBlendOp',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkColorBlendEquationEXT._type_ = {
    'srcColorBlendFactor': ctypes.c_int,
    'dstColorBlendFactor': ctypes.c_int,
    'colorBlendOp': ctypes.c_int,
    'srcAlphaBlendFactor': ctypes.c_int,
    'dstAlphaBlendFactor': ctypes.c_int,
    'alphaBlendOp': ctypes.c_int,
}
