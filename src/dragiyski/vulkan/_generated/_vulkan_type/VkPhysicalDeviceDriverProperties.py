import ctypes

class VkPhysicalDeviceDriverProperties(ctypes.Structure):
    pass

from .VkConformanceVersion import VkConformanceVersion

VkPhysicalDeviceDriverProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('driverID', ctypes.c_int),
    ('driverName', ctypes.ARRAY(ctypes.c_char, 256)),
    ('driverInfo', ctypes.ARRAY(ctypes.c_char, 256)),
    ('conformanceVersion', VkConformanceVersion),
]

VkPhysicalDeviceDriverProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'driverID': ctypes.c_int,
    'driverName': ctypes.ARRAY(ctypes.c_char, 256),
    'driverInfo': ctypes.ARRAY(ctypes.c_char, 256),
    'conformanceVersion': VkConformanceVersion,
}
