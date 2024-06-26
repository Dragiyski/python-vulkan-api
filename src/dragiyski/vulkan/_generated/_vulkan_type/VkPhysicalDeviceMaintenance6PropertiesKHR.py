import ctypes

class VkPhysicalDeviceMaintenance6PropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('blockTexelViewCompatibleMultipleLayers', ctypes.c_uint32),
        ('maxCombinedImageSamplerDescriptorCount', ctypes.c_uint32),
        ('fragmentShadingRateClampCombinerInputs', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'blockTexelViewCompatibleMultipleLayers': 'block_texel_view_compatible_multiple_layers',
        'maxCombinedImageSamplerDescriptorCount': 'max_combined_image_sampler_descriptor_count',
        'fragmentShadingRateClampCombinerInputs': 'fragment_shading_rate_clamp_combiner_inputs',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance6',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_6_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_6_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceMaintenance6PropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'blockTexelViewCompatibleMultipleLayers': ctypes.c_uint32,
    'maxCombinedImageSamplerDescriptorCount': ctypes.c_uint32,
    'fragmentShadingRateClampCombinerInputs': ctypes.c_uint32,
}
