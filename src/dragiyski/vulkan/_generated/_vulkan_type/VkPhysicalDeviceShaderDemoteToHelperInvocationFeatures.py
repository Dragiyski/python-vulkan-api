import ctypes

class VkPhysicalDeviceShaderDemoteToHelperInvocationFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderDemoteToHelperInvocation', ctypes.c_uint32),
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
        'shaderDemoteToHelperInvocation': 'shader_demote_to_helper_invocation',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DEMOTE_TO_HELPER_INVOCATION_FEATURES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DEMOTE_TO_HELPER_INVOCATION_FEATURES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderDemoteToHelperInvocationFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderDemoteToHelperInvocation': ctypes.c_uint32,
}
