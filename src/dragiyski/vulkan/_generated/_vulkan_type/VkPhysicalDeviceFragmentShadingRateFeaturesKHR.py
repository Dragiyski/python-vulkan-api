import ctypes

class VkPhysicalDeviceFragmentShadingRateFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineFragmentShadingRate', ctypes.c_uint32),
        ('primitiveFragmentShadingRate', ctypes.c_uint32),
        ('attachmentFragmentShadingRate', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pipelineFragmentShadingRate': 'pipeline_fragment_shading_rate',
        'primitiveFragmentShadingRate': 'primitive_fragment_shading_rate',
        'attachmentFragmentShadingRate': 'attachment_fragment_shading_rate',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_fragment_shading_rate',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_FEATURES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_FEATURES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceFragmentShadingRateFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineFragmentShadingRate': ctypes.c_uint32,
    'primitiveFragmentShadingRate': ctypes.c_uint32,
    'attachmentFragmentShadingRate': ctypes.c_uint32,
}
