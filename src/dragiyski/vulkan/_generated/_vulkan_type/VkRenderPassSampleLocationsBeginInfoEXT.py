import ctypes

class VkRenderPassSampleLocationsBeginInfoEXT(ctypes.Structure):
    pass

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

VkRenderPassSampleLocationsBeginInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'attachmentInitialSampleLocationsCount': ctypes.c_uint32,
    'pAttachmentInitialSampleLocations': ctypes.POINTER(VkAttachmentSampleLocationsEXT),
    'postSubpassSampleLocationsCount': ctypes.c_uint32,
    'pPostSubpassSampleLocations': ctypes.POINTER(VkSubpassSampleLocationsEXT),
}
