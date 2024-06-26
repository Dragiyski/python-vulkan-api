import ctypes

class VkPhysicalDeviceRayTracingPipelinePropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderGroupHandleSize', ctypes.c_uint32),
        ('maxRayRecursionDepth', ctypes.c_uint32),
        ('maxShaderGroupStride', ctypes.c_uint32),
        ('shaderGroupBaseAlignment', ctypes.c_uint32),
        ('shaderGroupHandleCaptureReplaySize', ctypes.c_uint32),
        ('maxRayDispatchInvocationCount', ctypes.c_uint32),
        ('shaderGroupHandleAlignment', ctypes.c_uint32),
        ('maxRayHitAttributeSize', ctypes.c_uint32),
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
        'maxRayRecursionDepth': 'max_ray_recursion_depth',
        'maxShaderGroupStride': 'max_shader_group_stride',
        'shaderGroupBaseAlignment': 'shader_group_base_alignment',
        'shaderGroupHandleCaptureReplaySize': 'shader_group_handle_capture_replay_size',
        'maxRayDispatchInvocationCount': 'max_ray_dispatch_invocation_count',
        'shaderGroupHandleAlignment': 'shader_group_handle_alignment',
        'maxRayHitAttributeSize': 'max_ray_hit_attribute_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_ray_tracing_pipeline',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceRayTracingPipelinePropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderGroupHandleSize': ctypes.c_uint32,
    'maxRayRecursionDepth': ctypes.c_uint32,
    'maxShaderGroupStride': ctypes.c_uint32,
    'shaderGroupBaseAlignment': ctypes.c_uint32,
    'shaderGroupHandleCaptureReplaySize': ctypes.c_uint32,
    'maxRayDispatchInvocationCount': ctypes.c_uint32,
    'shaderGroupHandleAlignment': ctypes.c_uint32,
    'maxRayHitAttributeSize': ctypes.c_uint32,
}
