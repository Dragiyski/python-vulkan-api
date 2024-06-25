import ctypes

class VkPhysicalDevicePerStageDescriptorSetFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('perStageDescriptorSet', ctypes.c_uint32),
        ('dynamicPipelineLayout', ctypes.c_uint32),
    ]

VkPhysicalDevicePerStageDescriptorSetFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'perStageDescriptorSet': ctypes.c_uint32,
    'dynamicPipelineLayout': ctypes.c_uint32,
}
