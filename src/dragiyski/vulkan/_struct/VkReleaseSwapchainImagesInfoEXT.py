import ctypes, sys

class VkReleaseSwapchainImagesInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchain', ctypes.c_void_p),
        ('imageIndexCount', ctypes.c_uint32),
        ('pImageIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

sys.modules[__name__] = VkReleaseSwapchainImagesInfoEXT
