import ctypes, sys

class VkExecutionGraphPipelineScratchSizeAMDX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('size', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkExecutionGraphPipelineScratchSizeAMDX
