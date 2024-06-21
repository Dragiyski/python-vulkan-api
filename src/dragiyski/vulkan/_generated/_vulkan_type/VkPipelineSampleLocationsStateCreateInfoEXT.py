import ctypes

class CType(ctypes.Structure):
    pass

from .VkSampleLocationsInfoEXT import CType as VkSampleLocationsInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsEnable', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]
