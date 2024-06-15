import ctypes, sys

class VkQueueFamilyCheckpointProperties2NV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('checkpointExecutionStageMask', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkQueueFamilyCheckpointProperties2NV
