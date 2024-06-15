import ctypes, sys

class VkDeviceFaultInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkDeviceFaultInfoEXT

from . import VkDeviceFaultVendorInfoEXT
from . import VkDeviceFaultAddressInfoEXT

VkDeviceFaultInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ('pAddressInfos', ctypes.POINTER(VkDeviceFaultAddressInfoEXT)),
    ('pVendorInfos', ctypes.POINTER(VkDeviceFaultVendorInfoEXT)),
    ('pVendorBinaryData', ctypes.c_void_p),
]
