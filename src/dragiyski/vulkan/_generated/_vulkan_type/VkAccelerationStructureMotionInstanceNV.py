import ctypes

class VkAccelerationStructureMotionInstanceNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkAccelerationStructureMotionInstanceDataNV',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'type': 'type',
        'flags': 'flags',
        'data': 'data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing_motion_blur',
    }
    _vk_enum_ = {
        'type': 'VkAccelerationStructureMotionInstanceTypeNV',
        'flags': 'VkAccelerationStructureMotionInstanceFlagsNV',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAccelerationStructureMotionInstanceDataNV import VkAccelerationStructureMotionInstanceDataNV

VkAccelerationStructureMotionInstanceNV._fields_ = [
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('data', VkAccelerationStructureMotionInstanceDataNV),
]

VkAccelerationStructureMotionInstanceNV._type_ = {
    'type': ctypes.c_int,
    'flags': ctypes.c_uint32,
    'data': VkAccelerationStructureMotionInstanceDataNV,
}
