import ctypes

class VkPhysicalDeviceRayTracingPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderGroupHandleSize', ctypes.c_uint32),
        ('maxRecursionDepth', ctypes.c_uint32),
        ('maxShaderGroupStride', ctypes.c_uint32),
        ('shaderGroupBaseAlignment', ctypes.c_uint32),
        ('maxGeometryCount', ctypes.c_uint64),
        ('maxInstanceCount', ctypes.c_uint64),
        ('maxTriangleCount', ctypes.c_uint64),
        ('maxDescriptorSetAccelerationStructures', ctypes.c_uint32),
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
        'shaderGroupHandleSize': 'shader_group_handle_size',
        'maxRecursionDepth': 'max_recursion_depth',
        'maxShaderGroupStride': 'max_shader_group_stride',
        'shaderGroupBaseAlignment': 'shader_group_base_alignment',
        'maxGeometryCount': 'max_geometry_count',
        'maxInstanceCount': 'max_instance_count',
        'maxTriangleCount': 'max_triangle_count',
        'maxDescriptorSetAccelerationStructures': 'max_descriptor_set_acceleration_structures',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceRayTracingPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderGroupHandleSize': ctypes.c_uint32,
    'maxRecursionDepth': ctypes.c_uint32,
    'maxShaderGroupStride': ctypes.c_uint32,
    'shaderGroupBaseAlignment': ctypes.c_uint32,
    'maxGeometryCount': ctypes.c_uint64,
    'maxInstanceCount': ctypes.c_uint64,
    'maxTriangleCount': ctypes.c_uint64,
    'maxDescriptorSetAccelerationStructures': ctypes.c_uint32,
}
