import ctypes

class VkRayTracingShaderGroupCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('type', ctypes.c_int),
        ('generalShader', ctypes.c_uint32),
        ('closestHitShader', ctypes.c_uint32),
        ('anyHitShader', ctypes.c_uint32),
        ('intersectionShader', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkRayTracingPipelineCreateInfoNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'type': 'type',
        'generalShader': 'general_shader',
        'closestHitShader': 'closest_hit_shader',
        'anyHitShader': 'any_hit_shader',
        'intersectionShader': 'intersection_shader',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'type': 'VkRayTracingShaderGroupTypeKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkRayTracingShaderGroupCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'type': ctypes.c_int,
    'generalShader': ctypes.c_uint32,
    'closestHitShader': ctypes.c_uint32,
    'anyHitShader': ctypes.c_uint32,
    'intersectionShader': ctypes.c_uint32,
}
