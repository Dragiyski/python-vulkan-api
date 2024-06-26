import ctypes

class VkImageViewAddressPropertiesNVX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetImageViewAddressNVX',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'deviceAddress': 'device_address',
        'size': 'size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NVX_image_view_handle',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_VIEW_ADDRESS_PROPERTIES_NVX'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_ADDRESS_PROPERTIES_NVX
        for function in self._init_:
            function(self, *args, **kwargs)

VkImageViewAddressPropertiesNVX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceAddress': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
