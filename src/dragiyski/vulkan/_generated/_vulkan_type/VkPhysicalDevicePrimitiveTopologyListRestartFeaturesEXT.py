import ctypes

class VkPhysicalDevicePrimitiveTopologyListRestartFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitiveTopologyListRestart', ctypes.c_uint32),
        ('primitiveTopologyPatchListRestart', ctypes.c_uint32),
    ]

VkPhysicalDevicePrimitiveTopologyListRestartFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'primitiveTopologyListRestart': ctypes.c_uint32,
    'primitiveTopologyPatchListRestart': ctypes.c_uint32,
}
