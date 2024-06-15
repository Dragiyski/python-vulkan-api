import ctypes, sys

class VkPipelineSampleLocationsStateCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineSampleLocationsStateCreateInfoEXT

from . import VkSampleLocationsInfoEXT

VkPipelineSampleLocationsStateCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsEnable', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]
