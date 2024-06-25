import ctypes

class VkPhysicalDeviceSeparateDepthStencilLayoutsFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('separateDepthStencilLayouts', ctypes.c_uint32),
    ]

VkPhysicalDeviceSeparateDepthStencilLayoutsFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'separateDepthStencilLayouts': ctypes.c_uint32,
}
