import ctypes

class VkQueueFamilyCheckpointPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('checkpointExecutionStageMask', ctypes.c_uint32),
    ]

VkQueueFamilyCheckpointPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'checkpointExecutionStageMask': ctypes.c_uint32,
}
