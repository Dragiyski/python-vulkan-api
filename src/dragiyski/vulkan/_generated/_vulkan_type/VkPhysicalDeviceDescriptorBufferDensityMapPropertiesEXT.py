import ctypes

class VkPhysicalDeviceDescriptorBufferDensityMapPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('combinedImageSamplerDensityMapDescriptorSize', ctypes.c_size_t),
    ]

VkPhysicalDeviceDescriptorBufferDensityMapPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'combinedImageSamplerDensityMapDescriptorSize': ctypes.c_size_t,
}
