import ctypes

class VkDeviceFaultVendorInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'description': ctypes.ARRAY(ctypes.c_char, 256),
            'vendorFaultCode': ctypes.c_uint64,
            'vendorFaultData': ctypes.c_uint64,
        }

    _fields_ = [
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('vendorFaultCode', ctypes.c_uint64),
        ('vendorFaultData', ctypes.c_uint64),
    ]
