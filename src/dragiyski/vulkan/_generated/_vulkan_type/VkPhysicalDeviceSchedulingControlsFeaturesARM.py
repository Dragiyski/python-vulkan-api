import ctypes

class VkPhysicalDeviceSchedulingControlsFeaturesARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('schedulingControls', ctypes.c_uint32),
    ]

VkPhysicalDeviceSchedulingControlsFeaturesARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'schedulingControls': ctypes.c_uint32,
}
