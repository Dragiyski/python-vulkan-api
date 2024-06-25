import ctypes

class VkQueueFamilyCheckpointProperties2NV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('checkpointExecutionStageMask', ctypes.c_uint64),
    ]

VkQueueFamilyCheckpointProperties2NV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'checkpointExecutionStageMask': ctypes.c_uint64,
}
