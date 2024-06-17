import ctypes, sys

class VkPhysicalDeviceDriverProperties(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceDriverProperties

from . import VkConformanceVersion

VkPhysicalDeviceDriverProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('driverID', ctypes.c_int),
    ('driverName', ctypes.ARRAY(ctypes.c_char, 256)),
    ('driverInfo', ctypes.ARRAY(ctypes.c_char, 256)),
    ('conformanceVersion', VkConformanceVersion),
]
