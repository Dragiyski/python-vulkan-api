import ctypes

class VkPhysicalDeviceCoverageReductionModeFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('coverageReductionMode', ctypes.c_uint32),
    ]

VkPhysicalDeviceCoverageReductionModeFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'coverageReductionMode': ctypes.c_uint32,
}
