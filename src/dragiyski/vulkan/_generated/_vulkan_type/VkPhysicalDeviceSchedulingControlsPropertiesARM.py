import ctypes

class VkPhysicalDeviceSchedulingControlsPropertiesARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('schedulingControlsFlags', ctypes.c_uint64),
    ]

VkPhysicalDeviceSchedulingControlsPropertiesARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'schedulingControlsFlags': ctypes.c_uint64,
}
