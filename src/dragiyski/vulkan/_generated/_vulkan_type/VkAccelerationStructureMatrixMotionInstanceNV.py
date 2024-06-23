import ctypes

class CType(ctypes.Structure):
    pass

from .VkTransformMatrixKHR import CType as VkTransformMatrixKHR

CType._fields_ = [
    ('transformT0', VkTransformMatrixKHR),
    ('transformT1', VkTransformMatrixKHR),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkTransformMatrixKHR',
    },
    'included_in': {
        'VkAccelerationStructureMotionInstanceDataNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'transformT0': {'python_name': ['transform', 't0'], 'type': 'VkTransformMatrixKHR'},
        'transformT1': {'python_name': ['transform', 't1'], 'type': 'VkTransformMatrixKHR'},
        'instanceCustomIndex': {'python_name': ['instance', 'custom', 'index']},
        'mask': {'python_name': ['mask']},
        'instanceShaderBindingTableRecordOffset': {'python_name': ['instance', 'shader', 'binding', 'table', 'record', 'offset']},
        'flags': {'python_name': ['flags'], 'type': 'VkGeometryInstanceFlagsKHR'},
        'accelerationStructureReference': {'python_name': ['acceleration', 'structure', 'reference']},
    }
}
