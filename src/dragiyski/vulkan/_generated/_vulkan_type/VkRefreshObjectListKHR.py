import ctypes

class VkRefreshObjectListKHR(ctypes.Structure):
    pass

from .VkRefreshObjectKHR import VkRefreshObjectKHR

VkRefreshObjectListKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('objectCount', ctypes.c_uint32),
    ('pObjects', ctypes.POINTER(VkRefreshObjectKHR)),
]

VkRefreshObjectListKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'objectCount': ctypes.c_uint32,
    'pObjects': ctypes.POINTER(VkRefreshObjectKHR),
}
