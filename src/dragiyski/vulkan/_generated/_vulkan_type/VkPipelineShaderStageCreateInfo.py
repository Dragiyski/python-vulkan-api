import ctypes

class VkPipelineShaderStageCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'stage': ctypes.c_uint32,
            'module': ctypes.c_void_p,
            'pName': ctypes.c_char_p,
            'pSpecializationInfo': ctypes.POINTER(VkSpecializationInfo),
        }


from .VkSpecializationInfo import VkSpecializationInfo

VkPipelineShaderStageCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', ctypes.c_uint32),
    ('module', ctypes.c_void_p),
    ('pName', ctypes.c_char_p),
    ('pSpecializationInfo', ctypes.POINTER(VkSpecializationInfo)),
]
