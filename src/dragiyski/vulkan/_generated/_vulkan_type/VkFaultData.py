import ctypes

class VkFaultData(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('faultLevel', ctypes.c_int),
        ('faultType', ctypes.c_int),
    ]

VkFaultData._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'faultLevel': ctypes.c_int,
    'faultType': ctypes.c_int,
}
