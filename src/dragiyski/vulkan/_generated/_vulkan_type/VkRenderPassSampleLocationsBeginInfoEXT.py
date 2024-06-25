import ctypes

class VkRenderPassSampleLocationsBeginInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'attachmentInitialSampleLocationsCount': ctypes.c_uint32,
            'pAttachmentInitialSampleLocations': ctypes.POINTER(VkAttachmentSampleLocationsEXT),
            'postSubpassSampleLocationsCount': ctypes.c_uint32,
            'pPostSubpassSampleLocations': ctypes.POINTER(VkSubpassSampleLocationsEXT),
        }


from .VkAttachmentSampleLocationsEXT import VkAttachmentSampleLocationsEXT
from .VkSubpassSampleLocationsEXT import VkSubpassSampleLocationsEXT

VkRenderPassSampleLocationsBeginInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentInitialSampleLocationsCount', ctypes.c_uint32),
    ('pAttachmentInitialSampleLocations', ctypes.POINTER(VkAttachmentSampleLocationsEXT)),
    ('postSubpassSampleLocationsCount', ctypes.c_uint32),
    ('pPostSubpassSampleLocations', ctypes.POINTER(VkSubpassSampleLocationsEXT)),
]
