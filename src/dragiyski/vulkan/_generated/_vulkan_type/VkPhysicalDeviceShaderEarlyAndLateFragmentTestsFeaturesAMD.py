import ctypes

class VkPhysicalDeviceShaderEarlyAndLateFragmentTestsFeaturesAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderEarlyAndLateFragmentTests', ctypes.c_uint32),
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
        'shaderEarlyAndLateFragmentTests': 'shader_early_and_late_fragment_tests',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMD_shader_early_and_late_fragment_tests',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_EARLY_AND_LATE_FRAGMENT_TESTS_FEATURES_AMD'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_EARLY_AND_LATE_FRAGMENT_TESTS_FEATURES_AMD
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderEarlyAndLateFragmentTestsFeaturesAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderEarlyAndLateFragmentTests': ctypes.c_uint32,
}
