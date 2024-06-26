import ctypes

class VkPhysicalDeviceShaderCoreProperties2AMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreFeatures', ctypes.c_uint32),
        ('activeComputeUnitCount', ctypes.c_uint32),
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
        'shaderCoreFeatures': 'shader_core_features',
        'activeComputeUnitCount': 'active_compute_unit_count',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMD_shader_core_properties2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'shaderCoreFeatures': 'VkShaderCorePropertiesFlagsAMD',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_2_AMD'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_2_AMD
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderCoreProperties2AMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderCoreFeatures': ctypes.c_uint32,
    'activeComputeUnitCount': ctypes.c_uint32,
}
