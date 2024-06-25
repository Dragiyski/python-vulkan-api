import ctypes

class VkExternalBufferProperties(ctypes.Structure):
    pass

from .VkExternalMemoryProperties import VkExternalMemoryProperties

VkExternalBufferProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('externalMemoryProperties', VkExternalMemoryProperties),
]

VkExternalBufferProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'externalMemoryProperties': VkExternalMemoryProperties,
}
