import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('extendedDynamicState2', ctypes.c_uint32),
        ('extendedDynamicState2LogicOp', ctypes.c_uint32),
        ('extendedDynamicState2PatchControlPoints', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_2_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'extendedDynamicState2': {'python_name': ['extended', 'dynamic', 'state2']},
        'extendedDynamicState2LogicOp': {'python_name': ['extended', 'dynamic', 'state2', 'logic', 'op']},
        'extendedDynamicState2PatchControlPoints': {'python_name': ['extended', 'dynamic', 'state2', 'patch', 'control', 'points']},
    }
}
