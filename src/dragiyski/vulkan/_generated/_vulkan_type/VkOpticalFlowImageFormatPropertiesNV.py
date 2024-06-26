import ctypes

class VkOpticalFlowImageFormatPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('format', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceOpticalFlowImageFormatsNV',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'format': 'format',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_optical_flow',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'format': 'VkFormat',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_IMAGE_FORMAT_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPTICAL_FLOW_IMAGE_FORMAT_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkOpticalFlowImageFormatPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'format': ctypes.c_int,
}
