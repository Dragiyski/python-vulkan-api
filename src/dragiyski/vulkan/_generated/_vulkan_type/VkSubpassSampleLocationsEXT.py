import ctypes

class VkSubpassSampleLocationsEXT(ctypes.Structure):
    pass

from .VkSampleLocationsInfoEXT import VkSampleLocationsInfoEXT

VkSubpassSampleLocationsEXT._fields_ = [
    ('subpassIndex', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]

VkSubpassSampleLocationsEXT._type_ = {
    'subpassIndex': ctypes.c_uint32,
    'sampleLocationsInfo': VkSampleLocationsInfoEXT,
}
