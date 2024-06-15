import ctypes, sys

class VkAccelerationStructureDeviceAddressInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkAccelerationStructureDeviceAddressInfoKHR
