import ctypes

class VkVideoEncodeH264CapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('maxLevelIdc', ctypes.c_int),
        ('maxSliceCount', ctypes.c_uint32),
        ('maxPPictureL0ReferenceCount', ctypes.c_uint32),
        ('maxBPictureL0ReferenceCount', ctypes.c_uint32),
        ('maxL1ReferenceCount', ctypes.c_uint32),
        ('maxTemporalLayerCount', ctypes.c_uint32),
        ('expectDyadicTemporalLayerPattern', ctypes.c_uint32),
        ('minQp', ctypes.c_int32),
        ('maxQp', ctypes.c_int32),
        ('prefersGopRemainingFrames', ctypes.c_uint32),
        ('requiresGopRemainingFrames', ctypes.c_uint32),
        ('stdSyntaxFlags', ctypes.c_uint32),
    ]

VkVideoEncodeH264CapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'maxLevelIdc': ctypes.c_int,
    'maxSliceCount': ctypes.c_uint32,
    'maxPPictureL0ReferenceCount': ctypes.c_uint32,
    'maxBPictureL0ReferenceCount': ctypes.c_uint32,
    'maxL1ReferenceCount': ctypes.c_uint32,
    'maxTemporalLayerCount': ctypes.c_uint32,
    'expectDyadicTemporalLayerPattern': ctypes.c_uint32,
    'minQp': ctypes.c_int32,
    'maxQp': ctypes.c_int32,
    'prefersGopRemainingFrames': ctypes.c_uint32,
    'requiresGopRemainingFrames': ctypes.c_uint32,
    'stdSyntaxFlags': ctypes.c_uint32,
}
