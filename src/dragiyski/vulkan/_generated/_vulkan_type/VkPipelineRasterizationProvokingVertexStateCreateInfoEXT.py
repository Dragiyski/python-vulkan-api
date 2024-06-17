import ctypes, sys

class VkPipelineRasterizationProvokingVertexStateCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('provokingVertexMode', ctypes.c_int),
    ]

sys.modules[__name__] = VkPipelineRasterizationProvokingVertexStateCreateInfoEXT
