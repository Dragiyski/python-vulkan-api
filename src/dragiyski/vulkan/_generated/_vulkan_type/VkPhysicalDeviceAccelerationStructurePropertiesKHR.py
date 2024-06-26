import ctypes

class VkPhysicalDeviceAccelerationStructurePropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxGeometryCount', ctypes.c_uint64),
        ('maxInstanceCount', ctypes.c_uint64),
        ('maxPrimitiveCount', ctypes.c_uint64),
        ('maxPerStageDescriptorAccelerationStructures', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindAccelerationStructures', ctypes.c_uint32),
        ('maxDescriptorSetAccelerationStructures', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindAccelerationStructures', ctypes.c_uint32),
        ('minAccelerationStructureScratchOffsetAlignment', ctypes.c_uint32),
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
        'maxGeometryCount': 'max_geometry_count',
        'maxInstanceCount': 'max_instance_count',
        'maxPrimitiveCount': 'max_primitive_count',
        'maxPerStageDescriptorAccelerationStructures': 'max_per_stage_descriptor_acceleration_structures',
        'maxPerStageDescriptorUpdateAfterBindAccelerationStructures': 'max_per_stage_descriptor_update_after_bind_acceleration_structures',
        'maxDescriptorSetAccelerationStructures': 'max_descriptor_set_acceleration_structures',
        'maxDescriptorSetUpdateAfterBindAccelerationStructures': 'max_descriptor_set_update_after_bind_acceleration_structures',
        'minAccelerationStructureScratchOffsetAlignment': 'min_acceleration_structure_scratch_offset_alignment',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceAccelerationStructurePropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxGeometryCount': ctypes.c_uint64,
    'maxInstanceCount': ctypes.c_uint64,
    'maxPrimitiveCount': ctypes.c_uint64,
    'maxPerStageDescriptorAccelerationStructures': ctypes.c_uint32,
    'maxPerStageDescriptorUpdateAfterBindAccelerationStructures': ctypes.c_uint32,
    'maxDescriptorSetAccelerationStructures': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindAccelerationStructures': ctypes.c_uint32,
    'minAccelerationStructureScratchOffsetAlignment': ctypes.c_uint32,
}
