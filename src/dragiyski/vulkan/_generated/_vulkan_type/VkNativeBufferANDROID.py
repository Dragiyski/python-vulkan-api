import ctypes

class VkNativeBufferANDROID(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'handle': ctypes.c_void_p,
            'stride': ctypes.c_int,
            'format': ctypes.c_int,
            'usage': ctypes.c_int,
            'usage2': VkNativeBufferUsage2ANDROID,
        }


from .VkNativeBufferUsage2ANDROID import VkNativeBufferUsage2ANDROID

VkNativeBufferANDROID._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('handle', ctypes.c_void_p),
    ('stride', ctypes.c_int),
    ('format', ctypes.c_int),
    ('usage', ctypes.c_int),
    ('usage2', VkNativeBufferUsage2ANDROID),
]
