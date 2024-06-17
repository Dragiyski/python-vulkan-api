import ctypes, sys

class VkPipelineRasterizationStateRasterizationOrderAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rasterizationOrder', ctypes.c_int),
    ]

sys.modules[__name__] = VkPipelineRasterizationStateRasterizationOrderAMD
