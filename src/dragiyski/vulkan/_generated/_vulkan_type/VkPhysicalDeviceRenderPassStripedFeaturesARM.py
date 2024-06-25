import ctypes

class VkPhysicalDeviceRenderPassStripedFeaturesARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('renderPassStriped', ctypes.c_uint32),
    ]

VkPhysicalDeviceRenderPassStripedFeaturesARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'renderPassStriped': ctypes.c_uint32,
}
