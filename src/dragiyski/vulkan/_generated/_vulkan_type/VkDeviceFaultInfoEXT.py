import ctypes

class VkDeviceFaultInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceFaultAddressInfoEXT',
        'VkDeviceFaultVendorInfoEXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetDeviceFaultInfoEXT',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'description': 'description',
        'pAddressInfos': 'address_infos',
        'pVendorInfos': 'vendor_infos',
        'pVendorBinaryData': 'vendor_binary_data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_device_fault',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_FAULT_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_FAULT_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


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

VkDeviceFaultInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'description': ctypes.ARRAY(ctypes.c_char, 256),
    'pAddressInfos': ctypes.POINTER(VkDeviceFaultAddressInfoEXT),
    'pVendorInfos': ctypes.POINTER(VkDeviceFaultVendorInfoEXT),
    'pVendorBinaryData': ctypes.c_void_p,
}
