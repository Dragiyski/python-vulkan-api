import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rasterizationOrderColorAttachmentAccess', ctypes.c_uint32),
        ('rasterizationOrderDepthAttachmentAccess', ctypes.c_uint32),
        ('rasterizationOrderStencilAttachmentAccess', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RASTERIZATION_ORDER_ATTACHMENT_ACCESS_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'rasterizationOrderColorAttachmentAccess': {'python_name': ['rasterization', 'order', 'color', 'attachment', 'access']},
        'rasterizationOrderDepthAttachmentAccess': {'python_name': ['rasterization', 'order', 'depth', 'attachment', 'access']},
        'rasterizationOrderStencilAttachmentAccess': {'python_name': ['rasterization', 'order', 'stencil', 'attachment', 'access']},
    }
}
