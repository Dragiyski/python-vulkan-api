import ctypes

class VkDeviceQueueShaderCoreControlCreateInfoARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreCount', ctypes.c_uint32),
    ]

VkDeviceQueueShaderCoreControlCreateInfoARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderCoreCount': ctypes.c_uint32,
}
