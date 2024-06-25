import ctypes

class VkCopyCommandTransformInfoQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('transform', ctypes.c_uint32),
    ]

VkCopyCommandTransformInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'transform': ctypes.c_uint32,
}
