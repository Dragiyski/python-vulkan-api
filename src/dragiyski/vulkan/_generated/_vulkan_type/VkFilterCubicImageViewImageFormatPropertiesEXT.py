import ctypes

class VkFilterCubicImageViewImageFormatPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('filterCubic', ctypes.c_uint32),
        ('filterCubicMinmax', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkImageFormatProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'filterCubic': 'filter_cubic',
        'filterCubicMinmax': 'filter_cubic_minmax',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_filter_cubic',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FILTER_CUBIC_IMAGE_VIEW_IMAGE_FORMAT_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FILTER_CUBIC_IMAGE_VIEW_IMAGE_FORMAT_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkFilterCubicImageViewImageFormatPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'filterCubic': ctypes.c_uint32,
    'filterCubicMinmax': ctypes.c_uint32,
}
