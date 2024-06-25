import ctypes

class VkGraphicsPipelineShaderGroupsCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'groupCount': ctypes.c_uint32,
            'pGroups': ctypes.POINTER(VkGraphicsShaderGroupCreateInfoNV),
            'pipelineCount': ctypes.c_uint32,
            'pPipelines': ctypes.POINTER(ctypes.c_void_p),
        }


from .VkGraphicsShaderGroupCreateInfoNV import VkGraphicsShaderGroupCreateInfoNV

VkGraphicsPipelineShaderGroupsCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('groupCount', ctypes.c_uint32),
    ('pGroups', ctypes.POINTER(VkGraphicsShaderGroupCreateInfoNV)),
    ('pipelineCount', ctypes.c_uint32),
    ('pPipelines', ctypes.POINTER(ctypes.c_void_p)),
]
