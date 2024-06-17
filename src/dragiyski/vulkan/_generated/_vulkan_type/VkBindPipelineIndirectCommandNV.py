import ctypes, sys

class VkBindPipelineIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('pipelineAddress', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkBindPipelineIndirectCommandNV
