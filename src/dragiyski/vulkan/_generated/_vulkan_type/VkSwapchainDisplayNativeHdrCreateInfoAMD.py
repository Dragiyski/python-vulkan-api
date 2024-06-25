import ctypes

class VkSwapchainDisplayNativeHdrCreateInfoAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('localDimmingEnable', ctypes.c_uint32),
    ]

VkSwapchainDisplayNativeHdrCreateInfoAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'localDimmingEnable': ctypes.c_uint32,
}
