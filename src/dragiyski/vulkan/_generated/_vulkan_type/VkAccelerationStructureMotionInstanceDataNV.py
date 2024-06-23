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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkAccelerationStructureInstanceKHR',
        'VkAccelerationStructureMatrixMotionInstanceNV',
        'VkAccelerationStructureSRTMotionInstanceNV',
    },
    'included_in': {
        'VkAccelerationStructureMotionInstanceNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'staticInstance': {'python_name': ['static', 'instance'], 'type': 'VkAccelerationStructureInstanceKHR'},
        'matrixMotionInstance': {'python_name': ['matrix', 'motion', 'instance'], 'type': 'VkAccelerationStructureMatrixMotionInstanceNV'},
        'srtMotionInstance': {'python_name': ['srt', 'motion', 'instance'], 'type': 'VkAccelerationStructureSRTMotionInstanceNV'},
    }
}
