import ctypes

class VkDeviceFaultAddressInfoEXT(ctypes.Structure):
    _fields_ = [
        ('addressType', ctypes.c_int),
        ('reportedAddress', ctypes.c_uint64),
        ('addressPrecision', ctypes.c_uint64),
    ]

VkDeviceFaultAddressInfoEXT._type_ = {
    'addressType': ctypes.c_int,
    'reportedAddress': ctypes.c_uint64,
    'addressPrecision': ctypes.c_uint64,
}
