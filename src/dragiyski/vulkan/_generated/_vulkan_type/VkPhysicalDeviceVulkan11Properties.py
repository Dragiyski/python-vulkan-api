import ctypes

class VkPhysicalDeviceVulkan11Properties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('driverUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('deviceLUID', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('deviceNodeMask', ctypes.c_uint32),
        ('deviceLUIDValid', ctypes.c_uint32),
        ('subgroupSize', ctypes.c_uint32),
        ('subgroupSupportedStages', ctypes.c_uint32),
        ('subgroupSupportedOperations', ctypes.c_uint32),
        ('subgroupQuadOperationsInAllStages', ctypes.c_uint32),
        ('pointClippingBehavior', ctypes.c_int),
        ('maxMultiviewViewCount', ctypes.c_uint32),
        ('maxMultiviewInstanceIndex', ctypes.c_uint32),
        ('protectedNoFault', ctypes.c_uint32),
        ('maxPerSetDescriptors', ctypes.c_uint32),
        ('maxMemoryAllocationSize', ctypes.c_uint64),
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
        'deviceUUID': 'device_uuid',
        'driverUUID': 'driver_uuid',
        'deviceLUID': 'device_luid',
        'deviceNodeMask': 'device_node_mask',
        'deviceLUIDValid': 'device_luidvalid',
        'subgroupSize': 'subgroup_size',
        'subgroupSupportedStages': 'subgroup_supported_stages',
        'subgroupSupportedOperations': 'subgroup_supported_operations',
        'subgroupQuadOperationsInAllStages': 'subgroup_quad_operations_in_all_stages',
        'pointClippingBehavior': 'point_clipping_behavior',
        'maxMultiviewViewCount': 'max_multiview_view_count',
        'maxMultiviewInstanceIndex': 'max_multiview_instance_index',
        'protectedNoFault': 'protected_no_fault',
        'maxPerSetDescriptors': 'max_per_set_descriptors',
        'maxMemoryAllocationSize': 'max_memory_allocation_size',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'subgroupSupportedStages': 'VkShaderStageFlags',
        'subgroupSupportedOperations': 'VkSubgroupFeatureFlags',
        'pointClippingBehavior': 'VkPointClippingBehavior',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceVulkan11Properties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'driverUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'deviceLUID': ctypes.ARRAY(ctypes.c_uint8, 8),
    'deviceNodeMask': ctypes.c_uint32,
    'deviceLUIDValid': ctypes.c_uint32,
    'subgroupSize': ctypes.c_uint32,
    'subgroupSupportedStages': ctypes.c_uint32,
    'subgroupSupportedOperations': ctypes.c_uint32,
    'subgroupQuadOperationsInAllStages': ctypes.c_uint32,
    'pointClippingBehavior': ctypes.c_int,
    'maxMultiviewViewCount': ctypes.c_uint32,
    'maxMultiviewInstanceIndex': ctypes.c_uint32,
    'protectedNoFault': ctypes.c_uint32,
    'maxPerSetDescriptors': ctypes.c_uint32,
    'maxMemoryAllocationSize': ctypes.c_uint64,
}
