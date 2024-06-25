import ctypes

class VkComputePipelineCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'stage': VkPipelineShaderStageCreateInfo,
            'layout': ctypes.c_void_p,
            'basePipelineHandle': ctypes.c_void_p,
            'basePipelineIndex': ctypes.c_int32,
        }


from .VkPipelineShaderStageCreateInfo import VkPipelineShaderStageCreateInfo

VkComputePipelineCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', VkPipelineShaderStageCreateInfo),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]
