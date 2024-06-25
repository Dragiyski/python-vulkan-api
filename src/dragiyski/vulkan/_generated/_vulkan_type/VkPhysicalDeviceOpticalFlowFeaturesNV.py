import ctypes

class VkPhysicalDeviceOpticalFlowFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('opticalFlow', ctypes.c_uint32),
    ]

VkPhysicalDeviceOpticalFlowFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'opticalFlow': ctypes.c_uint32,
}
