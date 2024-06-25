import ctypes

class VkAttachmentSampleLocationsEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'attachmentIndex': ctypes.c_uint32,
            'sampleLocationsInfo': VkSampleLocationsInfoEXT,
        }


from .VkSampleLocationsInfoEXT import VkSampleLocationsInfoEXT

VkAttachmentSampleLocationsEXT._fields_ = [
    ('attachmentIndex', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]
