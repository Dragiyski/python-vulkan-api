import ctypes, sys

class VkPhysicalDevicePipelinePropertiesFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelinePropertiesIdentifier', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePipelinePropertiesFeaturesEXT
