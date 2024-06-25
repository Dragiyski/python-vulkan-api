import ctypes

class VkPipelineSampleLocationsStateCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'sampleLocationsEnable': ctypes.c_uint32,
            'sampleLocationsInfo': VkSampleLocationsInfoEXT,
        }


from .VkSampleLocationsInfoEXT import VkSampleLocationsInfoEXT

VkPipelineSampleLocationsStateCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsEnable', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]
