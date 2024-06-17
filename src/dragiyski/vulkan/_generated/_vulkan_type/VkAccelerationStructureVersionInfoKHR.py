import ctypes, sys

class VkAccelerationStructureVersionInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pVersionData', ctypes.POINTER(ctypes.c_uint8)),
    ]

sys.modules[__name__] = VkAccelerationStructureVersionInfoKHR
