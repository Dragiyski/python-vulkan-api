import ctypes

class VkPhysicalDeviceWorkgroupMemoryExplicitLayoutFeaturesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'workgroupMemoryExplicitLayout': ctypes.c_uint32,
            'workgroupMemoryExplicitLayoutScalarBlockLayout': ctypes.c_uint32,
            'workgroupMemoryExplicitLayout8BitAccess': ctypes.c_uint32,
            'workgroupMemoryExplicitLayout16BitAccess': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('workgroupMemoryExplicitLayout', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayoutScalarBlockLayout', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayout8BitAccess', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayout16BitAccess', ctypes.c_uint32),
    ]
