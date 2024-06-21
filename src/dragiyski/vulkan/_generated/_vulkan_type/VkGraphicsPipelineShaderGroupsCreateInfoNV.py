import ctypes

class CType(ctypes.Structure):
    pass

from .VkGraphicsShaderGroupCreateInfoNV import CType as VkGraphicsShaderGroupCreateInfoNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('groupCount', ctypes.c_uint32),
    ('pGroups', ctypes.POINTER(VkGraphicsShaderGroupCreateInfoNV)),
    ('pipelineCount', ctypes.c_uint32),
    ('pPipelines', ctypes.POINTER(ctypes.c_void_p)),
]
