import ctypes

class VkPhysicalDeviceConservativeRasterizationPropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
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
