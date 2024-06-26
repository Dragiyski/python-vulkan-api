import ctypes

class VkPhysicalDeviceWorkgroupMemoryExplicitLayoutFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('workgroupMemoryExplicitLayout', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayoutScalarBlockLayout', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayout8BitAccess', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayout16BitAccess', ctypes.c_uint32),
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
        'workgroupMemoryExplicitLayout': 'workgroup_memory_explicit_layout',
        'workgroupMemoryExplicitLayoutScalarBlockLayout': 'workgroup_memory_explicit_layout_scalar_block_layout',
        'workgroupMemoryExplicitLayout8BitAccess': 'workgroup_memory_explicit_layout8_bit_access',
        'workgroupMemoryExplicitLayout16BitAccess': 'workgroup_memory_explicit_layout16_bit_access',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_workgroup_memory_explicit_layout',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_WORKGROUP_MEMORY_EXPLICIT_LAYOUT_FEATURES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_WORKGROUP_MEMORY_EXPLICIT_LAYOUT_FEATURES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceWorkgroupMemoryExplicitLayoutFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'workgroupMemoryExplicitLayout': ctypes.c_uint32,
    'workgroupMemoryExplicitLayoutScalarBlockLayout': ctypes.c_uint32,
    'workgroupMemoryExplicitLayout8BitAccess': ctypes.c_uint32,
    'workgroupMemoryExplicitLayout16BitAccess': ctypes.c_uint32,
}
