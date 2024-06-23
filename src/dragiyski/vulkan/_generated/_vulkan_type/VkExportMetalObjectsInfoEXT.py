import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkExportMetalBufferInfoEXT',
        'VkExportMetalCommandQueueInfoEXT',
        'VkExportMetalDeviceInfoEXT',
        'VkExportMetalIOSurfaceInfoEXT',
        'VkExportMetalSharedEventInfoEXT',
        'VkExportMetalTextureInfoEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkExportMetalObjectsEXT',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXPORT_METAL_OBJECTS_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
    }
}
