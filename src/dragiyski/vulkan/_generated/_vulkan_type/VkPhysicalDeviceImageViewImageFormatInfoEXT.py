import ctypes

class VkPhysicalDeviceImageViewImageFormatInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageViewType', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceImageFormatInfo2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'imageViewType': 'image_view_type',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_filter_cubic',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'imageViewType': 'VkImageViewType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_VIEW_IMAGE_FORMAT_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_VIEW_IMAGE_FORMAT_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceImageViewImageFormatInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageViewType': ctypes.c_int,
}
