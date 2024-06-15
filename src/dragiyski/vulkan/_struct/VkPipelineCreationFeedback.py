import ctypes, sys

class VkPipelineCreationFeedback(ctypes.Structure):
    _fields_ = [
        ('flags', ctypes.c_uint32),
        ('duration', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPipelineCreationFeedback
