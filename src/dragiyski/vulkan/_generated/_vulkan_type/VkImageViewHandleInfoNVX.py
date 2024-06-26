import ctypes

class VkImageViewHandleInfoNVX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('descriptorType', ctypes.c_int),
        ('sampler', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkGetImageViewHandleNVX',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'imageView': 'image_view',
        'descriptorType': 'descriptor_type',
        'sampler': 'sampler',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NVX_image_view_handle',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'descriptorType': 'VkDescriptorType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_VIEW_HANDLE_INFO_NVX'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_HANDLE_INFO_NVX
        for function in self._init_:
            function(self, *args, **kwargs)

VkImageViewHandleInfoNVX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageView': ctypes.c_void_p,
    'descriptorType': ctypes.c_int,
    'sampler': ctypes.c_void_p,
}
