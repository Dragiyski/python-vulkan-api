import ctypes

class VkHdrMetadataEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'displayPrimaryRed': VkXYColorEXT,
            'displayPrimaryGreen': VkXYColorEXT,
            'displayPrimaryBlue': VkXYColorEXT,
            'whitePoint': VkXYColorEXT,
            'maxLuminance': ctypes.c_float,
            'minLuminance': ctypes.c_float,
            'maxContentLightLevel': ctypes.c_float,
            'maxFrameAverageLightLevel': ctypes.c_float,
        }


from .VkXYColorEXT import VkXYColorEXT

VkHdrMetadataEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayPrimaryRed', VkXYColorEXT),
    ('displayPrimaryGreen', VkXYColorEXT),
    ('displayPrimaryBlue', VkXYColorEXT),
    ('whitePoint', VkXYColorEXT),
    ('maxLuminance', ctypes.c_float),
    ('minLuminance', ctypes.c_float),
    ('maxContentLightLevel', ctypes.c_float),
    ('maxFrameAverageLightLevel', ctypes.c_float),
]
