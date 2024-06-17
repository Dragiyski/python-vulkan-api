import ctypes, sys

class VkAttachmentSampleLocationsEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkAttachmentSampleLocationsEXT

from . import VkSampleLocationsInfoEXT

VkAttachmentSampleLocationsEXT._fields_ = [
    ('attachmentIndex', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]
