from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkTransformMatrixKHR'
_member_list_ = ['matrix']
_member_info_ = {
    'matrix': {
        'type': CArrayType(CArrayType(CFloatType('c_float'), 4), 3),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkAccelerationStructureInstanceKHR',
    'VkAccelerationStructureMatrixMotionInstanceNV',
}
_input_of_ = set()
_output_of_ = set()
