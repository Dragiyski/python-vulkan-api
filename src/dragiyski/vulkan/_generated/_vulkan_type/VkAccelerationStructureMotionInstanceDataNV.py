import ctypes

class CType(ctypes.Union):
    pass

from .VkAccelerationStructureInstanceKHR import CType as VkAccelerationStructureInstanceKHR
from .VkAccelerationStructureMatrixMotionInstanceNV import CType as VkAccelerationStructureMatrixMotionInstanceNV
from .VkAccelerationStructureSRTMotionInstanceNV import CType as VkAccelerationStructureSRTMotionInstanceNV

CType._fields_ = [
    ('staticInstance', VkAccelerationStructureInstanceKHR),
    ('matrixMotionInstance', VkAccelerationStructureMatrixMotionInstanceNV),
    ('srtMotionInstance', VkAccelerationStructureSRTMotionInstanceNV),
]
