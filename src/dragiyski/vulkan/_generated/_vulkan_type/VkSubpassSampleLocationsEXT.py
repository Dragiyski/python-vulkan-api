import ctypes, sys

class VkSubpassSampleLocationsEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkSubpassSampleLocationsEXT

from . import VkSampleLocationsInfoEXT

VkSubpassSampleLocationsEXT._fields_ = [
    ('subpassIndex', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]
