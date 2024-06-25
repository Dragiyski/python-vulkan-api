import ctypes

class VkPhysicalDeviceVulkanSC10Features(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderAtomicInstructions', ctypes.c_uint32),
    ]

VkPhysicalDeviceVulkanSC10Features._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderAtomicInstructions': ctypes.c_uint32,
}
