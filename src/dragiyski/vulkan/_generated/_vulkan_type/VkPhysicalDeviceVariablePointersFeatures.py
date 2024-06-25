import ctypes

class VkPhysicalDeviceVariablePointersFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('variablePointersStorageBuffer', ctypes.c_uint32),
        ('variablePointers', ctypes.c_uint32),
    ]

VkPhysicalDeviceVariablePointersFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'variablePointersStorageBuffer': ctypes.c_uint32,
    'variablePointers': ctypes.c_uint32,
}
