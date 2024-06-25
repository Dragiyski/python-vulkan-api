import ctypes

class VkPipelineSampleLocationsStateCreateInfoEXT(ctypes.Structure):
    pass

from .VkSampleLocationsInfoEXT import VkSampleLocationsInfoEXT

VkPipelineSampleLocationsStateCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsEnable', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]

VkPipelineSampleLocationsStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampleLocationsEnable': ctypes.c_uint32,
    'sampleLocationsInfo': VkSampleLocationsInfoEXT,
}
