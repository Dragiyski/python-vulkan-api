import ctypes, sys

class VkPhysicalDeviceImageProcessing2PropertiesQCOM(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceImageProcessing2PropertiesQCOM

from . import VkExtent2D

VkPhysicalDeviceImageProcessing2PropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxBlockMatchWindow', VkExtent2D),
]
