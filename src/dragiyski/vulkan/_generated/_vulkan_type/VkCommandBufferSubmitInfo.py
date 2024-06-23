import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandBuffer', ctypes.c_void_p),
        ('deviceMask', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkRenderPassStripeSubmitInfoARM',
    },
    'includes': set(),
    'included_in': {
        'VkSubmitInfo2',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_SUBMIT_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'commandBuffer': {'python_name': ['command', 'buffer']},
        'deviceMask': {'python_name': ['device', 'mask']},
    }
}
