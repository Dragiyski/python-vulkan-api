import ctypes

class VkPhysicalDeviceVertexInputDynamicStateFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vertexInputDynamicState', ctypes.c_uint32),
    ]

VkPhysicalDeviceVertexInputDynamicStateFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vertexInputDynamicState': ctypes.c_uint32,
}
