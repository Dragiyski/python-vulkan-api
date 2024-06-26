import ctypes

class VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentShaderSampleInterlock', ctypes.c_uint32),
        ('fragmentShaderPixelInterlock', ctypes.c_uint32),
        ('fragmentShaderShadingRateInterlock', ctypes.c_uint32),
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
        'fragmentShaderSampleInterlock': 'fragment_shader_sample_interlock',
        'fragmentShaderPixelInterlock': 'fragment_shader_pixel_interlock',
        'fragmentShaderShadingRateInterlock': 'fragment_shader_shading_rate_interlock',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_fragment_shader_interlock',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_INTERLOCK_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_INTERLOCK_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentShaderSampleInterlock': ctypes.c_uint32,
    'fragmentShaderPixelInterlock': ctypes.c_uint32,
    'fragmentShaderShadingRateInterlock': ctypes.c_uint32,
}
