import ctypes, sys

class VkGraphicsPipelineShaderGroupsCreateInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkGraphicsPipelineShaderGroupsCreateInfoNV

from . import VkGraphicsShaderGroupCreateInfoNV

VkGraphicsPipelineShaderGroupsCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('groupCount', ctypes.c_uint32),
    ('pGroups', ctypes.POINTER(VkGraphicsShaderGroupCreateInfoNV)),
    ('pipelineCount', ctypes.c_uint32),
    ('pPipelines', ctypes.POINTER(ctypes.c_void_p)),
]
