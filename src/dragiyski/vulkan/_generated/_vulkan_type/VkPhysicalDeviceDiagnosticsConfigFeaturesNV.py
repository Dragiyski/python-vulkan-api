import ctypes, sys

class VkPhysicalDeviceDiagnosticsConfigFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('diagnosticsConfig', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDiagnosticsConfigFeaturesNV
