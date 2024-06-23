import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkRect2D)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdOpticalFlowExecuteNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_EXECUTE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkOpticalFlowExecuteFlagsNV'},
        'regionCount': {'python_name': ['region', 'count']},
        'pRegions': {'python_name': ['p', 'regions'], 'len': [['regionCount']], 'type': 'VkRect2D'},
    }
}
