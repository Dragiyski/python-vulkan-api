import ctypes, sys

class VkVideoEncodeH265CapabilitiesKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH265CapabilitiesKHR

from . import VkExtent2D

VkVideoEncodeH265CapabilitiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('maxLevelIdc', ctypes.c_int),
    ('maxSliceSegmentCount', ctypes.c_uint32),
    ('maxTiles', VkExtent2D),
    ('ctbSizes', ctypes.c_uint32),
    ('transformBlockSizes', ctypes.c_uint32),
    ('maxPPictureL0ReferenceCount', ctypes.c_uint32),
    ('maxBPictureL0ReferenceCount', ctypes.c_uint32),
    ('maxL1ReferenceCount', ctypes.c_uint32),
    ('maxSubLayerCount', ctypes.c_uint32),
    ('expectDyadicTemporalSubLayerPattern', ctypes.c_uint32),
    ('minQp', ctypes.c_int32),
    ('maxQp', ctypes.c_int32),
    ('prefersGopRemainingFrames', ctypes.c_uint32),
    ('requiresGopRemainingFrames', ctypes.c_uint32),
    ('stdSyntaxFlags', ctypes.c_uint32),
]
