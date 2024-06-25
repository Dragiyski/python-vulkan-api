import ctypes

class VkPhysicalDeviceImageCompressionControlFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageCompressionControl', ctypes.c_uint32),
    ]

VkPhysicalDeviceImageCompressionControlFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageCompressionControl': ctypes.c_uint32,
}
