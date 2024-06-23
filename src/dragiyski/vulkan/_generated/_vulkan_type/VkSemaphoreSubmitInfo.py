import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('value', ctypes.c_uint64),
        ('stageMask', ctypes.c_uint64),
        ('deviceIndex', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkRenderPassStripeSubmitInfoARM',
        'VkSubmitInfo2',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SEMAPHORE_SUBMIT_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'semaphore': {'python_name': ['semaphore']},
        'value': {'python_name': ['value']},
        'stageMask': {'python_name': ['stage', 'mask'], 'type': 'VkPipelineStageFlags2'},
        'deviceIndex': {'python_name': ['device', 'index']},
    }
}
