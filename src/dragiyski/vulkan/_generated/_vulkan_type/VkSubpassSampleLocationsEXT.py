import ctypes

class CType(ctypes.Structure):
    pass

from .VkSampleLocationsInfoEXT import CType as VkSampleLocationsInfoEXT

CType._fields_ = [
    ('subpassIndex', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]
