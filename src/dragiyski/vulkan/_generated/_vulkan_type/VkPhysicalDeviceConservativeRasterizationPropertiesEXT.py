import ctypes

class VkPhysicalDeviceConservativeRasterizationPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitiveOverestimationSize', ctypes.c_float),
        ('maxExtraPrimitiveOverestimationSize', ctypes.c_float),
        ('extraPrimitiveOverestimationSizeGranularity', ctypes.c_float),
        ('primitiveUnderestimation', ctypes.c_uint32),
        ('conservativePointAndLineRasterization', ctypes.c_uint32),
        ('degenerateTrianglesRasterized', ctypes.c_uint32),
        ('degenerateLinesRasterized', ctypes.c_uint32),
        ('fullyCoveredFragmentShaderInputVariable', ctypes.c_uint32),
        ('conservativeRasterizationPostDepthCoverage', ctypes.c_uint32),
    ]

VkPhysicalDeviceConservativeRasterizationPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'primitiveOverestimationSize': ctypes.c_float,
    'maxExtraPrimitiveOverestimationSize': ctypes.c_float,
    'extraPrimitiveOverestimationSizeGranularity': ctypes.c_float,
    'primitiveUnderestimation': ctypes.c_uint32,
    'conservativePointAndLineRasterization': ctypes.c_uint32,
    'degenerateTrianglesRasterized': ctypes.c_uint32,
    'degenerateLinesRasterized': ctypes.c_uint32,
    'fullyCoveredFragmentShaderInputVariable': ctypes.c_uint32,
    'conservativeRasterizationPostDepthCoverage': ctypes.c_uint32,
}
