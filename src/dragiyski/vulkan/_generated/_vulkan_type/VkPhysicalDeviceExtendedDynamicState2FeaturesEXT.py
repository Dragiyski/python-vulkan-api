import ctypes

class VkPhysicalDeviceExtendedDynamicState2FeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('extendedDynamicState2', ctypes.c_uint32),
        ('extendedDynamicState2LogicOp', ctypes.c_uint32),
        ('extendedDynamicState2PatchControlPoints', ctypes.c_uint32),
    ]

VkPhysicalDeviceExtendedDynamicState2FeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'extendedDynamicState2': ctypes.c_uint32,
    'extendedDynamicState2LogicOp': ctypes.c_uint32,
    'extendedDynamicState2PatchControlPoints': ctypes.c_uint32,
}
