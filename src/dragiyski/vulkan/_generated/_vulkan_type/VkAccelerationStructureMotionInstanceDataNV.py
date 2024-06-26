import ctypes

class VkAccelerationStructureMotionInstanceDataNV(ctypes.Union):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkAccelerationStructureInstanceKHR',
        'VkAccelerationStructureMatrixMotionInstanceNV',
        'VkAccelerationStructureSRTMotionInstanceNV',
    }
    _included_in_ = {
        'VkAccelerationStructureMotionInstanceNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'staticInstance': 'static_instance',
        'matrixMotionInstance': 'matrix_motion_instance',
        'srtMotionInstance': 'srt_motion_instance',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing_motion_blur',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAccelerationStructureInstanceKHR import VkAccelerationStructureInstanceKHR
from .VkAccelerationStructureMatrixMotionInstanceNV import VkAccelerationStructureMatrixMotionInstanceNV
from .VkAccelerationStructureSRTMotionInstanceNV import VkAccelerationStructureSRTMotionInstanceNV

VkAccelerationStructureMotionInstanceDataNV._fields_ = [
    ('staticInstance', VkAccelerationStructureInstanceKHR),
    ('matrixMotionInstance', VkAccelerationStructureMatrixMotionInstanceNV),
    ('srtMotionInstance', VkAccelerationStructureSRTMotionInstanceNV),
]

VkAccelerationStructureMotionInstanceDataNV._type_ = {
    'staticInstance': VkAccelerationStructureInstanceKHR,
    'matrixMotionInstance': VkAccelerationStructureMatrixMotionInstanceNV,
    'srtMotionInstance': VkAccelerationStructureSRTMotionInstanceNV,
}
