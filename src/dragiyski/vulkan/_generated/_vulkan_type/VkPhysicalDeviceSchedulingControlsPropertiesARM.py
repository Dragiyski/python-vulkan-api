import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('schedulingControlsFlags', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCHEDULING_CONTROLS_PROPERTIES_ARM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'schedulingControlsFlags': {'python_name': ['scheduling', 'controls', 'flags'], 'type': 'VkPhysicalDeviceSchedulingControlsFlagsARM'},
    }
}
