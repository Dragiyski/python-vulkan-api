import ctypes

class VkSwapchainPresentScalingCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('scalingBehavior', ctypes.c_uint32),
        ('presentGravityX', ctypes.c_uint32),
        ('presentGravityY', ctypes.c_uint32),
    ]

VkSwapchainPresentScalingCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'scalingBehavior': ctypes.c_uint32,
    'presentGravityX': ctypes.c_uint32,
    'presentGravityY': ctypes.c_uint32,
}
