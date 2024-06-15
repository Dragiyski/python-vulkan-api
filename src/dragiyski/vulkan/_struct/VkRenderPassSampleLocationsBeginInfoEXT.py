import ctypes, sys

class VkRenderPassSampleLocationsBeginInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassSampleLocationsBeginInfoEXT

from . import VkSubpassSampleLocationsEXT
from . import VkAttachmentSampleLocationsEXT

VkRenderPassSampleLocationsBeginInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentInitialSampleLocationsCount', ctypes.c_uint32),
    ('pAttachmentInitialSampleLocations', ctypes.POINTER(VkAttachmentSampleLocationsEXT)),
    ('postSubpassSampleLocationsCount', ctypes.c_uint32),
    ('pPostSubpassSampleLocations', ctypes.POINTER(VkSubpassSampleLocationsEXT)),
]
