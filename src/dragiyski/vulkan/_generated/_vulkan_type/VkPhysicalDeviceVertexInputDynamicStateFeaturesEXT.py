import ctypes, sys

class VkPhysicalDeviceVertexInputDynamicStateFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vertexInputDynamicState', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceVertexInputDynamicStateFeaturesEXT
