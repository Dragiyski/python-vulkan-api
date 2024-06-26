import ctypes

class VkPhysicalDeviceRayTracingInvocationReorderPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingInvocationReorderReorderingHint', ctypes.c_int),
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
        'rayTracingInvocationReorderReorderingHint': 'ray_tracing_invocation_reorder_reordering_hint',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing_invocation_reorder',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'rayTracingInvocationReorderReorderingHint': 'VkRayTracingInvocationReorderModeNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_INVOCATION_REORDER_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_INVOCATION_REORDER_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceRayTracingInvocationReorderPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rayTracingInvocationReorderReorderingHint': ctypes.c_int,
}
