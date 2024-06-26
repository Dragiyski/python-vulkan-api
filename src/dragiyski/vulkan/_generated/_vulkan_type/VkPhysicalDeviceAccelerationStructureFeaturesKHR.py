import ctypes

class VkPhysicalDeviceAccelerationStructureFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_uint32),
        ('accelerationStructureCaptureReplay', ctypes.c_uint32),
        ('accelerationStructureIndirectBuild', ctypes.c_uint32),
        ('accelerationStructureHostCommands', ctypes.c_uint32),
        ('descriptorBindingAccelerationStructureUpdateAfterBind', ctypes.c_uint32),
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
        'accelerationStructure': 'acceleration_structure',
        'accelerationStructureCaptureReplay': 'acceleration_structure_capture_replay',
        'accelerationStructureIndirectBuild': 'acceleration_structure_indirect_build',
        'accelerationStructureHostCommands': 'acceleration_structure_host_commands',
        'descriptorBindingAccelerationStructureUpdateAfterBind': 'descriptor_binding_acceleration_structure_update_after_bind',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_FEATURES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_FEATURES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceAccelerationStructureFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'accelerationStructure': ctypes.c_uint32,
    'accelerationStructureCaptureReplay': ctypes.c_uint32,
    'accelerationStructureIndirectBuild': ctypes.c_uint32,
    'accelerationStructureHostCommands': ctypes.c_uint32,
    'descriptorBindingAccelerationStructureUpdateAfterBind': ctypes.c_uint32,
}
