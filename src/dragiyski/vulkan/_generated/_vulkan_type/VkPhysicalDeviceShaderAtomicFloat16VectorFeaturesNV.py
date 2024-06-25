import ctypes

class VkPhysicalDeviceShaderAtomicFloat16VectorFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderFloat16VectorAtomics', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderAtomicFloat16VectorFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderFloat16VectorAtomics': ctypes.c_uint32,
}
