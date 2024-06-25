import ctypes

class VkAccelerationStructureVersionInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pVersionData', ctypes.POINTER(ctypes.c_uint8)),
    ]

VkAccelerationStructureVersionInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pVersionData': ctypes.POINTER(ctypes.c_uint8),
}
