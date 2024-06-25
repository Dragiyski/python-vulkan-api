import ctypes

class VkCoarseSampleOrderCustomNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'shadingRate': ctypes.c_int,
            'sampleCount': ctypes.c_uint32,
            'sampleLocationCount': ctypes.c_uint32,
            'pSampleLocations': ctypes.POINTER(VkCoarseSampleLocationNV),
        }


from .VkCoarseSampleLocationNV import VkCoarseSampleLocationNV

VkCoarseSampleOrderCustomNV._fields_ = [
    ('shadingRate', ctypes.c_int),
    ('sampleCount', ctypes.c_uint32),
    ('sampleLocationCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkCoarseSampleLocationNV)),
]
