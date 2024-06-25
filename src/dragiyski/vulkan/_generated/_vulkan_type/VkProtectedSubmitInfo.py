import ctypes

class VkProtectedSubmitInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('protectedSubmit', ctypes.c_uint32),
    ]

VkProtectedSubmitInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'protectedSubmit': ctypes.c_uint32,
}
