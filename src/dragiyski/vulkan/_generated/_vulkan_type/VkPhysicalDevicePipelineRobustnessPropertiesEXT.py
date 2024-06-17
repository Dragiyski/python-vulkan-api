import ctypes, sys

class VkPhysicalDevicePipelineRobustnessPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('defaultRobustnessStorageBuffers', ctypes.c_int),
        ('defaultRobustnessUniformBuffers', ctypes.c_int),
        ('defaultRobustnessVertexInputs', ctypes.c_int),
        ('defaultRobustnessImages', ctypes.c_int),
    ]

sys.modules[__name__] = VkPhysicalDevicePipelineRobustnessPropertiesEXT
