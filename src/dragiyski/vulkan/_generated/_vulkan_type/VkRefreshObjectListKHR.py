import ctypes

class VkRefreshObjectListKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'objectCount': ctypes.c_uint32,
            'pObjects': ctypes.POINTER(VkRefreshObjectKHR),
        }


from .VkRefreshObjectKHR import VkRefreshObjectKHR

VkRefreshObjectListKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('objectCount', ctypes.c_uint32),
    ('pObjects', ctypes.POINTER(VkRefreshObjectKHR)),
]
