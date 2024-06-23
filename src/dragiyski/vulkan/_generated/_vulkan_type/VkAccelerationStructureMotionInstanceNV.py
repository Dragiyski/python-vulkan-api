import ctypes

class CType(ctypes.Structure):
    pass

from .VkAccelerationStructureMotionInstanceDataNV import CType as VkAccelerationStructureMotionInstanceDataNV

CType._fields_ = [
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('data', VkAccelerationStructureMotionInstanceDataNV),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkAccelerationStructureMotionInstanceDataNV',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'type': {'python_name': ['type'], 'type': 'VkAccelerationStructureMotionInstanceTypeNV'},
        'flags': {'python_name': ['flags'], 'type': 'VkAccelerationStructureMotionInstanceFlagsNV'},
        'data': {'python_name': ['data'], 'type': 'VkAccelerationStructureMotionInstanceDataNV'},
    }
}
