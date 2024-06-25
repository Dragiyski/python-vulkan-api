import ctypes

class VkPhysicalDeviceScalarBlockLayoutFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('scalarBlockLayout', ctypes.c_uint32),
    ]

VkPhysicalDeviceScalarBlockLayoutFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'scalarBlockLayout': ctypes.c_uint32,
}
