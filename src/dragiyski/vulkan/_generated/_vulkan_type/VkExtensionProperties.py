import ctypes

class VkExtensionProperties(ctypes.Structure):
    _fields_ = [
        ('extensionName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
    ]

VkExtensionProperties._type_ = {
    'extensionName': ctypes.ARRAY(ctypes.c_char, 256),
    'specVersion': ctypes.c_uint32,
}
