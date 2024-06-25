import ctypes

class VkPipelineLibraryCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('libraryCount', ctypes.c_uint32),
        ('pLibraries', ctypes.POINTER(ctypes.c_void_p)),
    ]

VkPipelineLibraryCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'libraryCount': ctypes.c_uint32,
    'pLibraries': ctypes.POINTER(ctypes.c_void_p),
}
