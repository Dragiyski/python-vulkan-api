import ctypes

class VkAccelerationStructureMotionInstanceDataNV(ctypes.Union):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'staticInstance': VkAccelerationStructureInstanceKHR,
            'matrixMotionInstance': VkAccelerationStructureMatrixMotionInstanceNV,
            'srtMotionInstance': VkAccelerationStructureSRTMotionInstanceNV,
        }


from .VkAccelerationStructureInstanceKHR import VkAccelerationStructureInstanceKHR
from .VkAccelerationStructureMatrixMotionInstanceNV import VkAccelerationStructureMatrixMotionInstanceNV
from .VkAccelerationStructureSRTMotionInstanceNV import VkAccelerationStructureSRTMotionInstanceNV

VkAccelerationStructureMotionInstanceDataNV._fields_ = [
    ('staticInstance', VkAccelerationStructureInstanceKHR),
    ('matrixMotionInstance', VkAccelerationStructureMatrixMotionInstanceNV),
    ('srtMotionInstance', VkAccelerationStructureSRTMotionInstanceNV),
]
