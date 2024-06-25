import ctypes

class VkPhysicalDevicePortabilitySubsetFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('constantAlphaColorBlendFactors', ctypes.c_uint32),
        ('events', ctypes.c_uint32),
        ('imageViewFormatReinterpretation', ctypes.c_uint32),
        ('imageViewFormatSwizzle', ctypes.c_uint32),
        ('imageView2DOn3DImage', ctypes.c_uint32),
        ('multisampleArrayImage', ctypes.c_uint32),
        ('mutableComparisonSamplers', ctypes.c_uint32),
        ('pointPolygons', ctypes.c_uint32),
        ('samplerMipLodBias', ctypes.c_uint32),
        ('separateStencilMaskRef', ctypes.c_uint32),
        ('shaderSampleRateInterpolationFunctions', ctypes.c_uint32),
        ('tessellationIsolines', ctypes.c_uint32),
        ('tessellationPointMode', ctypes.c_uint32),
        ('triangleFans', ctypes.c_uint32),
        ('vertexAttributeAccessBeyondStride', ctypes.c_uint32),
    ]

VkPhysicalDevicePortabilitySubsetFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'constantAlphaColorBlendFactors': ctypes.c_uint32,
    'events': ctypes.c_uint32,
    'imageViewFormatReinterpretation': ctypes.c_uint32,
    'imageViewFormatSwizzle': ctypes.c_uint32,
    'imageView2DOn3DImage': ctypes.c_uint32,
    'multisampleArrayImage': ctypes.c_uint32,
    'mutableComparisonSamplers': ctypes.c_uint32,
    'pointPolygons': ctypes.c_uint32,
    'samplerMipLodBias': ctypes.c_uint32,
    'separateStencilMaskRef': ctypes.c_uint32,
    'shaderSampleRateInterpolationFunctions': ctypes.c_uint32,
    'tessellationIsolines': ctypes.c_uint32,
    'tessellationPointMode': ctypes.c_uint32,
    'triangleFans': ctypes.c_uint32,
    'vertexAttributeAccessBeyondStride': ctypes.c_uint32,
}
