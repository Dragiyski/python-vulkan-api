import ctypes

class VkPhysicalDeviceNestedCommandBufferFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('nestedCommandBuffer', ctypes.c_uint32),
        ('nestedCommandBufferRendering', ctypes.c_uint32),
        ('nestedCommandBufferSimultaneousUse', ctypes.c_uint32),
    ]

VkPhysicalDeviceNestedCommandBufferFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'nestedCommandBuffer': ctypes.c_uint32,
    'nestedCommandBufferRendering': ctypes.c_uint32,
    'nestedCommandBufferSimultaneousUse': ctypes.c_uint32,
}
