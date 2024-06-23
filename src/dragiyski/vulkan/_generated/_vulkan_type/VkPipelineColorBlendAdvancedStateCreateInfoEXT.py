import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcPremultiplied', ctypes.c_uint32),
        ('dstPremultiplied', ctypes.c_uint32),
        ('blendOverlap', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkPipelineColorBlendStateCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_ADVANCED_STATE_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcPremultiplied': {'python_name': ['src', 'premultiplied']},
        'dstPremultiplied': {'python_name': ['dst', 'premultiplied']},
        'blendOverlap': {'python_name': ['blend', 'overlap'], 'type': 'VkBlendOverlapEXT'},
    }
}
