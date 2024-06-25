import ctypes

class VkPhysicalDeviceTextureCompressionASTCHDRFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('textureCompressionASTC_HDR', ctypes.c_uint32),
    ]

VkPhysicalDeviceTextureCompressionASTCHDRFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'textureCompressionASTC_HDR': ctypes.c_uint32,
}
