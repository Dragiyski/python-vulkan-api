import ctypes

class VkPipelineLayoutCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'setLayoutCount': ctypes.c_uint32,
            'pSetLayouts': ctypes.POINTER(ctypes.c_void_p),
            'pushConstantRangeCount': ctypes.c_uint32,
            'pPushConstantRanges': ctypes.POINTER(VkPushConstantRange),
        }


from .VkPushConstantRange import VkPushConstantRange

VkPipelineLayoutCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('setLayoutCount', ctypes.c_uint32),
    ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ('pushConstantRangeCount', ctypes.c_uint32),
    ('pPushConstantRanges', ctypes.POINTER(VkPushConstantRange)),
]
