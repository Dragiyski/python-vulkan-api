from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureMatrixMotionInstanceNV'
_member_list_ = ['transformT0', 'transformT1', 'instanceCustomIndex', 'mask', 'instanceShaderBindingTableRecordOffset', 'flags', 'accelerationStructureReference']
_member_info_ = {
    'transformT0': {
        'type': CComplexType('VkTransformMatrixKHR'),
        'type_name': 'VkTransformMatrixKHR',
        'structure': 'VkTransformMatrixKHR',
        'is_string': False,
    },
    'transformT1': {
        'type': CComplexType('VkTransformMatrixKHR'),
        'type_name': 'VkTransformMatrixKHR',
        'structure': 'VkTransformMatrixKHR',
        'is_string': False,
    },
    'instanceCustomIndex': {
        'type': CIntType('c_uint32'),
        'bitsize': 24,
        'is_string': False,
    },
    'mask': {
        'type': CIntType('c_uint32'),
        'bitsize': 8,
        'is_string': False,
    },
    'instanceShaderBindingTableRecordOffset': {
        'type': CIntType('c_uint32'),
        'bitsize': 24,
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkGeometryInstanceFlagsKHR',
        'enum': 'VkGeometryInstanceFlagsKHR',
        'bitsize': 8,
        'is_string': False,
    },
    'accelerationStructureReference': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkTransformMatrixKHR',
}
_included_in_ = {
    'VkAccelerationStructureMotionInstanceDataNV',
}
_input_of_ = set()
_output_of_ = set()
