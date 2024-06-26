import ctypes

class VkExternalMemoryProperties(ctypes.Structure):
    _fields_ = [
        ('externalMemoryFeatures', ctypes.c_uint32),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkExternalBufferProperties',
        'VkExternalImageFormatProperties',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'externalMemoryFeatures': 'external_memory_features',
        'exportFromImportedHandleTypes': 'export_from_imported_handle_types',
        'compatibleHandleTypes': 'compatible_handle_types',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'externalMemoryFeatures': 'VkExternalMemoryFeatureFlags',
        'exportFromImportedHandleTypes': 'VkExternalMemoryHandleTypeFlags',
        'compatibleHandleTypes': 'VkExternalMemoryHandleTypeFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkExternalMemoryProperties._type_ = {
    'externalMemoryFeatures': ctypes.c_uint32,
    'exportFromImportedHandleTypes': ctypes.c_uint32,
    'compatibleHandleTypes': ctypes.c_uint32,
}
