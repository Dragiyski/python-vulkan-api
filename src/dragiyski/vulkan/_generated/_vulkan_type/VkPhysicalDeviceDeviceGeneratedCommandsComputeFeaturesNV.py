import ctypes, sys

class VkPhysicalDeviceDeviceGeneratedCommandsComputeFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceGeneratedCompute', ctypes.c_uint32),
        ('deviceGeneratedComputePipelines', ctypes.c_uint32),
        ('deviceGeneratedComputeCaptureReplay', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDeviceGeneratedCommandsComputeFeaturesNV
