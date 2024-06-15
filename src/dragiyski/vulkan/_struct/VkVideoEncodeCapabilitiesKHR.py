import ctypes, sys

class VkVideoEncodeCapabilitiesKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeCapabilitiesKHR

from . import VkExtent2D

VkVideoEncodeCapabilitiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('rateControlModes', ctypes.c_uint32),
    ('maxRateControlLayers', ctypes.c_uint32),
    ('maxBitrate', ctypes.c_uint64),
    ('maxQualityLevels', ctypes.c_uint32),
    ('encodeInputPictureGranularity', VkExtent2D),
    ('supportedEncodeFeedbackFlags', ctypes.c_uint32),
]