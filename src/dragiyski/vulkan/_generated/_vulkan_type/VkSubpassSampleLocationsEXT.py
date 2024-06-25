import ctypes

class VkSubpassSampleLocationsEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'subpassIndex': ctypes.c_uint32,
            'sampleLocationsInfo': VkSampleLocationsInfoEXT,
        }


from .VkSampleLocationsInfoEXT import VkSampleLocationsInfoEXT

VkSubpassSampleLocationsEXT._fields_ = [
    ('subpassIndex', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]
