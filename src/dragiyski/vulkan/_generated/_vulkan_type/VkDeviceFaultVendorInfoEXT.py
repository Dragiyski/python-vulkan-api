import ctypes

class VkDeviceFaultVendorInfoEXT(ctypes.Structure):
    _fields_ = [
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('vendorFaultCode', ctypes.c_uint64),
        ('vendorFaultData', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDeviceFaultInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'description': 'description',
        'vendorFaultCode': 'vendor_fault_code',
        'vendorFaultData': 'vendor_fault_data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_device_fault',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceFaultVendorInfoEXT._type_ = {
    'description': ctypes.ARRAY(ctypes.c_char, 256),
    'vendorFaultCode': ctypes.c_uint64,
    'vendorFaultData': ctypes.c_uint64,
}
