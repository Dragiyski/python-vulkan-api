import ctypes

class VkColorBlendAdvancedEXT(ctypes.Structure):
    _fields_ = [
        ('advancedBlendOp', ctypes.c_int),
        ('srcPremultiplied', ctypes.c_uint32),
        ('dstPremultiplied', ctypes.c_uint32),
        ('blendOverlap', ctypes.c_int),
        ('clampResults', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdSetColorBlendAdvancedEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'advancedBlendOp': 'advanced_blend_op',
        'srcPremultiplied': 'src_premultiplied',
        'dstPremultiplied': 'dst_premultiplied',
        'blendOverlap': 'blend_overlap',
        'clampResults': 'clamp_results',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_extended_dynamic_state3',
        'VK_EXT_shader_object',
    }
    _vk_enum_ = {
        'advancedBlendOp': 'VkBlendOp',
        'blendOverlap': 'VkBlendOverlapEXT',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkColorBlendAdvancedEXT._type_ = {
    'advancedBlendOp': ctypes.c_int,
    'srcPremultiplied': ctypes.c_uint32,
    'dstPremultiplied': ctypes.c_uint32,
    'blendOverlap': ctypes.c_int,
    'clampResults': ctypes.c_uint32,
}
