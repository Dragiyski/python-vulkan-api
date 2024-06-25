import ctypes

class VkAttachmentSampleLocationsEXT(ctypes.Structure):
    pass

from .VkSampleLocationsInfoEXT import VkSampleLocationsInfoEXT

VkAttachmentSampleLocationsEXT._fields_ = [
    ('attachmentIndex', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]

VkAttachmentSampleLocationsEXT._type_ = {
    'attachmentIndex': ctypes.c_uint32,
    'sampleLocationsInfo': VkSampleLocationsInfoEXT,
}
