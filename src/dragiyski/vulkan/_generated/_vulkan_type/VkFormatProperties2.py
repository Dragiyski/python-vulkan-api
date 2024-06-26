import ctypes

class VkFormatProperties2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDrmFormatModifierPropertiesList2EXT',
        'VkDrmFormatModifierPropertiesListEXT',
        'VkFormatProperties3',
        'VkSubpassResolvePerformanceQueryEXT',
    }
    _includes_ = {
        'VkFormatProperties',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceFormatProperties2',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'formatProperties': 'format_properties',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkFormatProperties import VkFormatProperties

VkFormatProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatProperties', VkFormatProperties),
]

VkFormatProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'formatProperties': VkFormatProperties,
}
