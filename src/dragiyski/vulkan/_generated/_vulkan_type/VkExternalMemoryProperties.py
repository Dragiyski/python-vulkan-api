import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('externalMemoryFeatures', ctypes.c_uint32),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkExternalBufferProperties',
        'VkExternalImageFormatProperties',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'externalMemoryFeatures': {'python_name': ['external', 'memory', 'features'], 'type': 'VkExternalMemoryFeatureFlags'},
        'exportFromImportedHandleTypes': {'python_name': ['export', 'from', 'imported', 'handle', 'types'], 'type': 'VkExternalMemoryHandleTypeFlags'},
        'compatibleHandleTypes': {'python_name': ['compatible', 'handle', 'types'], 'type': 'VkExternalMemoryHandleTypeFlags'},
    }
}
