import ctypes

class VkPhysicalDeviceConditionalRenderingFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('conditionalRendering', ctypes.c_uint32),
        ('inheritedConditionalRendering', ctypes.c_uint32),
    ]

VkPhysicalDeviceConditionalRenderingFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'conditionalRendering': ctypes.c_uint32,
    'inheritedConditionalRendering': ctypes.c_uint32,
}
