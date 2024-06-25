import ctypes

class VkPhysicalDeviceDescriptorSetHostMappingFeaturesVALVE(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorSetHostMapping', ctypes.c_uint32),
    ]

VkPhysicalDeviceDescriptorSetHostMappingFeaturesVALVE._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'descriptorSetHostMapping': ctypes.c_uint32,
}
