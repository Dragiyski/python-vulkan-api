import ctypes

class CType(ctypes.Structure):
    pass

from .VkShaderResourceUsageAMD import CType as VkShaderResourceUsageAMD

CType._fields_ = [
    ('shaderStageMask', ctypes.c_uint32),
    ('resourceUsage', VkShaderResourceUsageAMD),
    ('numPhysicalVgprs', ctypes.c_uint32),
    ('numPhysicalSgprs', ctypes.c_uint32),
    ('numAvailableVgprs', ctypes.c_uint32),
    ('numAvailableSgprs', ctypes.c_uint32),
    ('computeWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkShaderResourceUsageAMD',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'shaderStageMask': {'python_name': ['shader', 'stage', 'mask'], 'type': 'VkShaderStageFlags'},
        'resourceUsage': {'python_name': ['resource', 'usage'], 'type': 'VkShaderResourceUsageAMD'},
        'numPhysicalVgprs': {'python_name': ['num', 'physical', 'vgprs']},
        'numPhysicalSgprs': {'python_name': ['num', 'physical', 'sgprs']},
        'numAvailableVgprs': {'python_name': ['num', 'available', 'vgprs']},
        'numAvailableSgprs': {'python_name': ['num', 'available', 'sgprs']},
        'computeWorkGroupSize': {'python_name': ['compute', 'work', 'group', 'size']},
    }
}
