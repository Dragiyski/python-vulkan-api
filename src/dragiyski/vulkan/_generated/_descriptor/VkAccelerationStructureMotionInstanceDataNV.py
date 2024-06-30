from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkAccelerationStructureMotionInstanceDataNV'
_member_list_ = ['staticInstance', 'matrixMotionInstance', 'srtMotionInstance']
_member_info_ = {
    'staticInstance': {
        'type': CComplexType('VkAccelerationStructureInstanceKHR'),
        'type_name': 'VkAccelerationStructureInstanceKHR',
        'structure': 'VkAccelerationStructureInstanceKHR',
        'is_string': False,
    },
    'matrixMotionInstance': {
        'type': CComplexType('VkAccelerationStructureMatrixMotionInstanceNV'),
        'type_name': 'VkAccelerationStructureMatrixMotionInstanceNV',
        'structure': 'VkAccelerationStructureMatrixMotionInstanceNV',
        'is_string': False,
    },
    'srtMotionInstance': {
        'type': CComplexType('VkAccelerationStructureSRTMotionInstanceNV'),
        'type_name': 'VkAccelerationStructureSRTMotionInstanceNV',
        'structure': 'VkAccelerationStructureSRTMotionInstanceNV',
        'is_string': False,
    },
}
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
