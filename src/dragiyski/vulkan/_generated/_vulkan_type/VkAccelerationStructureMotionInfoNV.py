import ctypes

class VkAccelerationStructureMotionInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxInstances', ctypes.c_uint32),
        ('flags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkAccelerationStructureCreateInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxInstances': 'max_instances',
        'flags': 'flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing_motion_blur',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkAccelerationStructureMotionInfoFlagsNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_MOTION_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_MOTION_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkAccelerationStructureMotionInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxInstances': ctypes.c_uint32,
    'flags': ctypes.c_uint32,
}
