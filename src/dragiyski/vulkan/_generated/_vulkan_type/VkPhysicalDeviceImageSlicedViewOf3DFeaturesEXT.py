import ctypes

class VkPhysicalDeviceImageSlicedViewOf3DFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageSlicedViewOf3D', ctypes.c_uint32),
    ]

VkPhysicalDeviceImageSlicedViewOf3DFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageSlicedViewOf3D': ctypes.c_uint32,
}
