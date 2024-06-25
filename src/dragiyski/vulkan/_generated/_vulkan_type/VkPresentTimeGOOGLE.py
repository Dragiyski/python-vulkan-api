import ctypes

class VkPresentTimeGOOGLE(ctypes.Structure):
    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
    ]

VkPresentTimeGOOGLE._type_ = {
    'presentID': ctypes.c_uint32,
    'desiredPresentTime': ctypes.c_uint64,
}
