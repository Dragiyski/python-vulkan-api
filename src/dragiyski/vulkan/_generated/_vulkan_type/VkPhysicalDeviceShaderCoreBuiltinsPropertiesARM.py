import ctypes

class VkPhysicalDeviceShaderCoreBuiltinsPropertiesARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreMask', ctypes.c_uint64),
        ('shaderCoreCount', ctypes.c_uint32),
        ('shaderWarpsPerCore', ctypes.c_uint32),
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
        'shaderCoreMask': 'shader_core_mask',
        'shaderCoreCount': 'shader_core_count',
        'shaderWarpsPerCore': 'shader_warps_per_core',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ARM_shader_core_builtins',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_BUILTINS_PROPERTIES_ARM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_BUILTINS_PROPERTIES_ARM
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderCoreBuiltinsPropertiesARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderCoreMask': ctypes.c_uint64,
    'shaderCoreCount': ctypes.c_uint32,
    'shaderWarpsPerCore': ctypes.c_uint32,
}
