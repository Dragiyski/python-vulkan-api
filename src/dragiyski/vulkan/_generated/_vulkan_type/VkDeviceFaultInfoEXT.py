import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceFaultAddressInfoEXT import CType as VkDeviceFaultAddressInfoEXT
from .VkDeviceFaultVendorInfoEXT import CType as VkDeviceFaultVendorInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ('pAddressInfos', ctypes.POINTER(VkDeviceFaultAddressInfoEXT)),
    ('pVendorInfos', ctypes.POINTER(VkDeviceFaultVendorInfoEXT)),
    ('pVendorBinaryData', ctypes.c_void_p),
]
