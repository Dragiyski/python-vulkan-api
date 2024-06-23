import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('advancedBlendOp', ctypes.c_int),
        ('srcPremultiplied', ctypes.c_uint32),
        ('dstPremultiplied', ctypes.c_uint32),
        ('blendOverlap', ctypes.c_int),
        ('clampResults', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdSetColorBlendAdvancedEXT',
    },
    'output_of': set(),
    'member_map': {
        'advancedBlendOp': {'python_name': ['advanced', 'blend', 'op'], 'type': 'VkBlendOp'},
        'srcPremultiplied': {'python_name': ['src', 'premultiplied']},
        'dstPremultiplied': {'python_name': ['dst', 'premultiplied']},
        'blendOverlap': {'python_name': ['blend', 'overlap'], 'type': 'VkBlendOverlapEXT'},
        'clampResults': {'python_name': ['clamp', 'results']},
    }
}
