import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('transform', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkRenderPassBeginInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_TRANSFORM_BEGIN_INFO_QCOM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'transform': {'python_name': ['transform'], 'type': 'VkSurfaceTransformFlagBitsKHR'},
    }
}
