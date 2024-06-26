import ctypes

class VkImageStencilUsageCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stencilUsage', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkImageCreateInfo',
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
        'stencilUsage': 'stencil_usage',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'stencilUsage': 'VkImageUsageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_STENCIL_USAGE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_STENCIL_USAGE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkImageStencilUsageCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stencilUsage': ctypes.c_uint32,
}
