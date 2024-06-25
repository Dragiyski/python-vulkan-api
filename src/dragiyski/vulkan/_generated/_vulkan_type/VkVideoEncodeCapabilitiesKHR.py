import ctypes

class VkVideoEncodeCapabilitiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'rateControlModes': ctypes.c_uint32,
            'maxRateControlLayers': ctypes.c_uint32,
            'maxBitrate': ctypes.c_uint64,
            'maxQualityLevels': ctypes.c_uint32,
            'encodeInputPictureGranularity': VkExtent2D,
            'supportedEncodeFeedbackFlags': ctypes.c_uint32,
        }


from .VkExtent2D import VkExtent2D

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
