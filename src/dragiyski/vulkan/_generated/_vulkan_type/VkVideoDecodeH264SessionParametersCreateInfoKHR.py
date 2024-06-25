import ctypes

class VkVideoDecodeH264SessionParametersCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'maxStdSPSCount': ctypes.c_uint32,
            'maxStdPPSCount': ctypes.c_uint32,
            'pParametersAddInfo': ctypes.POINTER(VkVideoDecodeH264SessionParametersAddInfoKHR),
        }


from .VkVideoDecodeH264SessionParametersAddInfoKHR import VkVideoDecodeH264SessionParametersAddInfoKHR

VkVideoDecodeH264SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoDecodeH264SessionParametersAddInfoKHR)),
]
