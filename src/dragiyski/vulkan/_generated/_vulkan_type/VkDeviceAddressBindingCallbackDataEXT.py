import ctypes

class VkDeviceAddressBindingCallbackDataEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('baseAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('bindingType', ctypes.c_int),
    ]

VkDeviceAddressBindingCallbackDataEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'baseAddress': ctypes.c_uint64,
    'size': ctypes.c_uint64,
    'bindingType': ctypes.c_int,
}
