import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('format', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceOpticalFlowImageFormatsNV',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_IMAGE_FORMAT_PROPERTIES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
    }
}
