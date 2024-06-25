import ctypes

class VkExternalImageFormatPropertiesNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'imageFormatProperties': VkImageFormatProperties,
            'externalMemoryFeatures': ctypes.c_uint32,
            'exportFromImportedHandleTypes': ctypes.c_uint32,
            'compatibleHandleTypes': ctypes.c_uint32,
        }


from .VkImageFormatProperties import VkImageFormatProperties

VkExternalImageFormatPropertiesNV._fields_ = [
    ('imageFormatProperties', VkImageFormatProperties),
    ('externalMemoryFeatures', ctypes.c_uint32),
    ('exportFromImportedHandleTypes', ctypes.c_uint32),
    ('compatibleHandleTypes', ctypes.c_uint32),
]
