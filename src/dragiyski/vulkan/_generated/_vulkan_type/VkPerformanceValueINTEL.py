import ctypes

class CType(ctypes.Structure):
    pass

from .VkPerformanceValueDataINTEL import CType as VkPerformanceValueDataINTEL

CType._fields_ = [
    ('type', ctypes.c_int),
    ('data', VkPerformanceValueDataINTEL),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkPerformanceValueDataINTEL',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPerformanceParameterINTEL',
    },
    'member_map': {
        'type': {'python_name': ['type'], 'type': 'VkPerformanceValueTypeINTEL'},
        'data': {'python_name': ['data'], 'type': 'VkPerformanceValueDataINTEL'},
    }
}
