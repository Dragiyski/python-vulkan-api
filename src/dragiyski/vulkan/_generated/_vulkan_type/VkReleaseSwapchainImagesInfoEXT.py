import ctypes

class VkReleaseSwapchainImagesInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'swapchain': ctypes.c_void_p,
            'imageIndexCount': ctypes.c_uint32,
            'pImageIndices': ctypes.POINTER(ctypes.c_uint32),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchain', ctypes.c_void_p),
        ('imageIndexCount', ctypes.c_uint32),
        ('pImageIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]
