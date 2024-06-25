import ctypes

class VkPhysicalDeviceRawAccessChainsFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderRawAccessChains', ctypes.c_uint32),
    ]

VkPhysicalDeviceRawAccessChainsFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderRawAccessChains': ctypes.c_uint32,
}
