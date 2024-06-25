import ctypes

class VkAccelerationStructureMotionInstanceDataNV(ctypes.Union):
    pass

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
