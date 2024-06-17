import ctypes, sys

class VkAccelerationStructureMotionInstanceDataNV(ctypes.Union):
    pass

sys.modules[__name__] = VkAccelerationStructureMotionInstanceDataNV

from . import VkAccelerationStructureInstanceKHR
from . import VkAccelerationStructureMatrixMotionInstanceNV
from . import VkAccelerationStructureSRTMotionInstanceNV

VkAccelerationStructureMotionInstanceDataNV._fields_ = [
    ('staticInstance', VkAccelerationStructureInstanceKHR),
    ('matrixMotionInstance', VkAccelerationStructureMatrixMotionInstanceNV),
    ('srtMotionInstance', VkAccelerationStructureSRTMotionInstanceNV),
]
