import ctypes, sys

class VkPhysicalDeviceMaintenance6PropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('blockTexelViewCompatibleMultipleLayers', ctypes.c_uint32),
        ('maxCombinedImageSamplerDescriptorCount', ctypes.c_uint32),
        ('fragmentShadingRateClampCombinerInputs', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMaintenance6PropertiesKHR
