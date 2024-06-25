import ctypes

class VkPhysicalDevicePCIBusInfoPropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pciDomain': ctypes.c_uint32,
            'pciBus': ctypes.c_uint32,
            'pciDevice': ctypes.c_uint32,
            'pciFunction': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pciDomain', ctypes.c_uint32),
        ('pciBus', ctypes.c_uint32),
        ('pciDevice', ctypes.c_uint32),
        ('pciFunction', ctypes.c_uint32),
    ]
