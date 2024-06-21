import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentSampleLocationsEXT import CType as VkAttachmentSampleLocationsEXT
from .VkSubpassSampleLocationsEXT import CType as VkSubpassSampleLocationsEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentInitialSampleLocationsCount', ctypes.c_uint32),
    ('pAttachmentInitialSampleLocations', ctypes.POINTER(VkAttachmentSampleLocationsEXT)),
    ('postSubpassSampleLocationsCount', ctypes.c_uint32),
    ('pPostSubpassSampleLocations', ctypes.POINTER(VkSubpassSampleLocationsEXT)),
]
