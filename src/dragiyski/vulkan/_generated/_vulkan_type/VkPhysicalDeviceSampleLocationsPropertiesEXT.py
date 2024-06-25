import ctypes

class VkPhysicalDeviceSampleLocationsPropertiesEXT(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkPhysicalDeviceSampleLocationsPropertiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationSampleCounts', ctypes.c_uint32),
    ('maxSampleLocationGridSize', VkExtent2D),
    ('sampleLocationCoordinateRange', ctypes.ARRAY(ctypes.c_float, 2)),
    ('sampleLocationSubPixelBits', ctypes.c_uint32),
    ('variableSampleLocations', ctypes.c_uint32),
]

VkPhysicalDeviceSampleLocationsPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampleLocationSampleCounts': ctypes.c_uint32,
    'maxSampleLocationGridSize': VkExtent2D,
    'sampleLocationCoordinateRange': ctypes.ARRAY(ctypes.c_float, 2),
    'sampleLocationSubPixelBits': ctypes.c_uint32,
    'variableSampleLocations': ctypes.c_uint32,
}
