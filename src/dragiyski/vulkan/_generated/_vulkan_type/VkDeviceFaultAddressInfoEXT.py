import ctypes

class VkDeviceFaultAddressInfoEXT(ctypes.Structure):
    _fields_ = [
        ('addressType', ctypes.c_int),
        ('reportedAddress', ctypes.c_uint64),
        ('addressPrecision', ctypes.c_uint64),
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
        'addressType': 'address_type',
        'reportedAddress': 'reported_address',
        'addressPrecision': 'address_precision',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_device_fault',
    }
    _vk_enum_ = {
        'addressType': 'VkDeviceFaultAddressTypeEXT',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceFaultAddressInfoEXT._type_ = {
    'addressType': ctypes.c_int,
    'reportedAddress': ctypes.c_uint64,
    'addressPrecision': ctypes.c_uint64,
}
