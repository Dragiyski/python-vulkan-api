import ctypes

class VkAmigoProfilingSubmitInfoSEC(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('firstDrawTimestamp', ctypes.c_uint64),
        ('swapBufferTimestamp', ctypes.c_uint64),
    ]

VkAmigoProfilingSubmitInfoSEC._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'firstDrawTimestamp': ctypes.c_uint64,
    'swapBufferTimestamp': ctypes.c_uint64,
}
