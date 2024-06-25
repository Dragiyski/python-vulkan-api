import ctypes

class VkPresentTimesInfoGOOGLE(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'swapchainCount': ctypes.c_uint32,
            'pTimes': ctypes.POINTER(VkPresentTimeGOOGLE),
        }


from .VkPresentTimeGOOGLE import VkPresentTimeGOOGLE

VkPresentTimesInfoGOOGLE._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pTimes', ctypes.POINTER(VkPresentTimeGOOGLE)),
]
