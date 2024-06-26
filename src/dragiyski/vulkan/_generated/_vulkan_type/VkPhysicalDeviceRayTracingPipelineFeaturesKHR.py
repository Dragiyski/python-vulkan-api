import ctypes

class VkPhysicalDeviceRayTracingPipelineFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingPipeline', ctypes.c_uint32),
        ('rayTracingPipelineShaderGroupHandleCaptureReplay', ctypes.c_uint32),
        ('rayTracingPipelineShaderGroupHandleCaptureReplayMixed', ctypes.c_uint32),
        ('rayTracingPipelineTraceRaysIndirect', ctypes.c_uint32),
        ('rayTraversalPrimitiveCulling', ctypes.c_uint32),
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
        'rayTracingPipeline': 'ray_tracing_pipeline',
        'rayTracingPipelineShaderGroupHandleCaptureReplay': 'ray_tracing_pipeline_shader_group_handle_capture_replay',
        'rayTracingPipelineShaderGroupHandleCaptureReplayMixed': 'ray_tracing_pipeline_shader_group_handle_capture_replay_mixed',
        'rayTracingPipelineTraceRaysIndirect': 'ray_tracing_pipeline_trace_rays_indirect',
        'rayTraversalPrimitiveCulling': 'ray_traversal_primitive_culling',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_ray_tracing_pipeline',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_FEATURES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_FEATURES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceRayTracingPipelineFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rayTracingPipeline': ctypes.c_uint32,
    'rayTracingPipelineShaderGroupHandleCaptureReplay': ctypes.c_uint32,
    'rayTracingPipelineShaderGroupHandleCaptureReplayMixed': ctypes.c_uint32,
    'rayTracingPipelineTraceRaysIndirect': ctypes.c_uint32,
    'rayTraversalPrimitiveCulling': ctypes.c_uint32,
}
