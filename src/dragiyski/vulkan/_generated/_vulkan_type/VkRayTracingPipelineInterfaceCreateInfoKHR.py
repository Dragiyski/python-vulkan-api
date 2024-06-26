import ctypes

class VkRayTracingPipelineInterfaceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxPipelineRayPayloadSize', ctypes.c_uint32),
        ('maxPipelineRayHitAttributeSize', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkRayTracingPipelineCreateInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxPipelineRayPayloadSize': 'max_pipeline_ray_payload_size',
        'maxPipelineRayHitAttributeSize': 'max_pipeline_ray_hit_attribute_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_ray_tracing_pipeline',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_INTERFACE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_INTERFACE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkRayTracingPipelineInterfaceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxPipelineRayPayloadSize': ctypes.c_uint32,
    'maxPipelineRayHitAttributeSize': ctypes.c_uint32,
}
