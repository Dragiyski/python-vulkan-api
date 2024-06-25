import ctypes

class VkPhysicalDeviceImageProcessing2PropertiesQCOM(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkPhysicalDeviceImageProcessing2PropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxBlockMatchWindow', VkExtent2D),
]

VkPhysicalDeviceImageProcessing2PropertiesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxBlockMatchWindow': VkExtent2D,
}
