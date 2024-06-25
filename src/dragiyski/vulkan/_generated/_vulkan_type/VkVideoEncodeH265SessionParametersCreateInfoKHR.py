import ctypes

class VkVideoEncodeH265SessionParametersCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'maxStdVPSCount': ctypes.c_uint32,
            'maxStdSPSCount': ctypes.c_uint32,
            'maxStdPPSCount': ctypes.c_uint32,
            'pParametersAddInfo': ctypes.POINTER(VkVideoEncodeH265SessionParametersAddInfoKHR),
        }


from .VkVideoEncodeH265SessionParametersAddInfoKHR import VkVideoEncodeH265SessionParametersAddInfoKHR

VkVideoEncodeH265SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdVPSCount', ctypes.c_uint32),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoEncodeH265SessionParametersAddInfoKHR)),
]
