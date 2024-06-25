import ctypes

class VkDeviceFaultInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'description': ctypes.ARRAY(ctypes.c_char, 256),
            'pAddressInfos': ctypes.POINTER(VkDeviceFaultAddressInfoEXT),
            'pVendorInfos': ctypes.POINTER(VkDeviceFaultVendorInfoEXT),
            'pVendorBinaryData': ctypes.c_void_p,
        }


from .VkDeviceFaultAddressInfoEXT import VkDeviceFaultAddressInfoEXT
from .VkDeviceFaultVendorInfoEXT import VkDeviceFaultVendorInfoEXT

VkDeviceFaultInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ('pAddressInfos', ctypes.POINTER(VkDeviceFaultAddressInfoEXT)),
    ('pVendorInfos', ctypes.POINTER(VkDeviceFaultVendorInfoEXT)),
    ('pVendorBinaryData', ctypes.c_void_p),
]
