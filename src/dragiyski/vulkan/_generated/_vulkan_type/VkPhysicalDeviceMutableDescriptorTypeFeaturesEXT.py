import ctypes

class VkPhysicalDeviceMutableDescriptorTypeFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mutableDescriptorType', ctypes.c_uint32),
    ]

VkPhysicalDeviceMutableDescriptorTypeFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'mutableDescriptorType': ctypes.c_uint32,
}
