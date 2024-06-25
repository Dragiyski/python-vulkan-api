import ctypes

class VkPhysicalDeviceShaderObjectPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderBinaryUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('shaderBinaryVersion', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderObjectPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderBinaryUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'shaderBinaryVersion': ctypes.c_uint32,
}
