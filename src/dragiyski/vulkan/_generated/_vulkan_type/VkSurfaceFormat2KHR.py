import ctypes

class VkSurfaceFormat2KHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkImageCompressionPropertiesEXT',
    }
    _includes_ = {
        'VkSurfaceFormatKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceSurfaceFormats2KHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'surfaceFormat': 'surface_format',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_get_surface_capabilities2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SURFACE_FORMAT_2_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_FORMAT_2_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSurfaceFormatKHR import VkSurfaceFormatKHR

VkSurfaceFormat2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceFormat', VkSurfaceFormatKHR),
]

VkSurfaceFormat2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'surfaceFormat': VkSurfaceFormatKHR,
}
