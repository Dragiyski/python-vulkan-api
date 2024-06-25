import ctypes

class VkPhysicalDeviceDriverProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'driverID': ctypes.c_int,
            'driverName': ctypes.ARRAY(ctypes.c_char, 256),
            'driverInfo': ctypes.ARRAY(ctypes.c_char, 256),
            'conformanceVersion': VkConformanceVersion,
        }


from .VkConformanceVersion import VkConformanceVersion

VkPhysicalDeviceDriverProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('driverID', ctypes.c_int),
    ('driverName', ctypes.ARRAY(ctypes.c_char, 256)),
    ('driverInfo', ctypes.ARRAY(ctypes.c_char, 256)),
    ('conformanceVersion', VkConformanceVersion),
]
