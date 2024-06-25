import ctypes

class VkPipelineLibraryCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'libraryCount': ctypes.c_uint32,
            'pLibraries': ctypes.POINTER(ctypes.c_void_p),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('libraryCount', ctypes.c_uint32),
        ('pLibraries', ctypes.POINTER(ctypes.c_void_p)),
    ]
