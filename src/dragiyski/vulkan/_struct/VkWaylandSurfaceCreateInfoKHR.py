import ctypes, sys

class VkWaylandSurfaceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('display', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkWaylandSurfaceCreateInfoKHR
