import ctypes, sys

class VkAccelerationStructureMotionInstanceDataNV(ctypes.Union):
    pass

sys.modules[__name__] = VkAccelerationStructureMotionInstanceDataNV

from . import VkAccelerationStructureSRTMotionInstanceNV
from . import VkAccelerationStructureMatrixMotionInstanceNV
from . import VkAccelerationStructureInstanceKHR

VkAccelerationStructureMotionInstanceDataNV._fields_ = [
    ('staticInstance', VkAccelerationStructureInstanceKHR),
    ('matrixMotionInstance', VkAccelerationStructureMatrixMotionInstanceNV),
    ('srtMotionInstance', VkAccelerationStructureSRTMotionInstanceNV),
]
