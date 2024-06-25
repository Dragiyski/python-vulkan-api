import ctypes

class VkPipelineExecutableInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipeline', ctypes.c_void_p),
        ('executableIndex', ctypes.c_uint32),
    ]

VkPipelineExecutableInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipeline': ctypes.c_void_p,
    'executableIndex': ctypes.c_uint32,
}
