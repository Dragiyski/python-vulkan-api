import ctypes

class VkPhysicalDeviceImage2DViewOf3DFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image2DViewOf3D', ctypes.c_uint32),
        ('sampler2DViewOf3D', ctypes.c_uint32),
    ]

VkPhysicalDeviceImage2DViewOf3DFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'image2DViewOf3D': ctypes.c_uint32,
    'sampler2DViewOf3D': ctypes.c_uint32,
}
