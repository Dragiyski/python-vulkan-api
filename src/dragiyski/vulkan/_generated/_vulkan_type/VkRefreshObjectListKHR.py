import ctypes, sys

class VkRefreshObjectListKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkRefreshObjectListKHR

from . import VkRefreshObjectKHR

VkRefreshObjectListKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('objectCount', ctypes.c_uint32),
    ('pObjects', ctypes.POINTER(VkRefreshObjectKHR)),
]
