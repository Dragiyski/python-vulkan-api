import ctypes, sys

class VkExternalBufferProperties(ctypes.Structure):
    pass

sys.modules[__name__] = VkExternalBufferProperties

from . import VkExternalMemoryProperties

VkExternalBufferProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('externalMemoryProperties', VkExternalMemoryProperties),
]
