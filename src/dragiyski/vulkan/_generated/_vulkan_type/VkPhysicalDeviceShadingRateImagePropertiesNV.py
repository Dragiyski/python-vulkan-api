import ctypes

class VkPhysicalDeviceShadingRateImagePropertiesNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'shadingRateTexelSize': VkExtent2D,
            'shadingRatePaletteSize': ctypes.c_uint32,
            'shadingRateMaxCoarseSamples': ctypes.c_uint32,
        }


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceShadingRateImagePropertiesNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateTexelSize', VkExtent2D),
    ('shadingRatePaletteSize', ctypes.c_uint32),
    ('shadingRateMaxCoarseSamples', ctypes.c_uint32),
]
