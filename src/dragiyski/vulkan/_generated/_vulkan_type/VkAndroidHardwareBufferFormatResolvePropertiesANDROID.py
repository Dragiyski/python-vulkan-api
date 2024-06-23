import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentFormat', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkAndroidHardwareBufferPropertiesANDROID',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_RESOLVE_PROPERTIES_ANDROID', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'colorAttachmentFormat': {'python_name': ['color', 'attachment', 'format'], 'type': 'VkFormat'},
    }
}
