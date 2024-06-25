import ctypes

class VkPhysicalDeviceInheritedViewportScissorFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('inheritedViewportScissor2D', ctypes.c_uint32),
    ]

VkPhysicalDeviceInheritedViewportScissorFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'inheritedViewportScissor2D': ctypes.c_uint32,
}
