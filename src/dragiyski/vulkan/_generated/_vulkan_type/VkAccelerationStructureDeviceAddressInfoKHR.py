import ctypes

class VkAccelerationStructureDeviceAddressInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_void_p),
    ]

VkAccelerationStructureDeviceAddressInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'accelerationStructure': ctypes.c_void_p,
}
