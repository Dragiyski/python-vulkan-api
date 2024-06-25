import ctypes

class VkVideoProfileListInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'profileCount': ctypes.c_uint32,
            'pProfiles': ctypes.POINTER(VkVideoProfileInfoKHR),
        }


from .VkVideoProfileInfoKHR import VkVideoProfileInfoKHR

VkVideoProfileListInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('profileCount', ctypes.c_uint32),
    ('pProfiles', ctypes.POINTER(VkVideoProfileInfoKHR)),
]
