import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
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
