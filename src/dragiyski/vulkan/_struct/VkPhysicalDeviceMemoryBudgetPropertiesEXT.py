import ctypes, sys

class VkPhysicalDeviceMemoryBudgetPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('heapBudget', ctypes.ARRAY(ctypes.c_uint64, 16)),
        ('heapUsage', ctypes.ARRAY(ctypes.c_uint64, 16)),
    ]

sys.modules[__name__] = VkPhysicalDeviceMemoryBudgetPropertiesEXT
