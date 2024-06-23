import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxSubpassShadingWorkgroupSizeAspectRatio', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBPASS_SHADING_PROPERTIES_HUAWEI', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxSubpassShadingWorkgroupSizeAspectRatio': {'python_name': ['max', 'subpass', 'shading', 'workgroup', 'size', 'aspect', 'ratio']},
    }
}
