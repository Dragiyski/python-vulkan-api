import ctypes, sys

class VkPhysicalDeviceBufferDeviceAddressFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('bufferDeviceAddress', ctypes.c_uint32),
        ('bufferDeviceAddressCaptureReplay', ctypes.c_uint32),
        ('bufferDeviceAddressMultiDevice', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceBufferDeviceAddressFeatures
