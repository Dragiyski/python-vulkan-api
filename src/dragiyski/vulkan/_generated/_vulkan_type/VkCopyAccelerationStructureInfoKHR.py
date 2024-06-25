import ctypes

class VkCopyAccelerationStructureInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('src', ctypes.c_void_p),
        ('dst', ctypes.c_void_p),
        ('mode', ctypes.c_int),
    ]

VkCopyAccelerationStructureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'src': ctypes.c_void_p,
    'dst': ctypes.c_void_p,
    'mode': ctypes.c_int,
}
