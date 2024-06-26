import ctypes

class VkDeviceFaultCountsEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('addressInfoCount', ctypes.c_uint32),
        ('vendorInfoCount', ctypes.c_uint32),
        ('vendorBinarySize', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetDeviceFaultInfoEXT',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'addressInfoCount': 'address_info_count',
        'vendorInfoCount': 'vendor_info_count',
        'vendorBinarySize': 'vendor_binary_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_device_fault',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_FAULT_COUNTS_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_FAULT_COUNTS_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceFaultCountsEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'addressInfoCount': ctypes.c_uint32,
    'vendorInfoCount': ctypes.c_uint32,
    'vendorBinarySize': ctypes.c_uint64,
}
