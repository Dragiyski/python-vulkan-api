import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vulkanMemoryModel', ctypes.c_uint32),
        ('vulkanMemoryModelDeviceScope', ctypes.c_uint32),
        ('vulkanMemoryModelAvailabilityVisibilityChains', ctypes.c_uint32),
    ]
