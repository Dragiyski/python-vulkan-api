import ctypes

class VkExternalImageFormatPropertiesNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkImageFormatProperties',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceExternalImageFormatPropertiesNV',
    }
    _python_name_ = {
        'imageFormatProperties': 'image_format_properties',
        'externalMemoryFeatures': 'external_memory_features',
        'exportFromImportedHandleTypes': 'export_from_imported_handle_types',
        'compatibleHandleTypes': 'compatible_handle_types',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_external_memory_capabilities',
    }
    _vk_enum_ = {
        'externalMemoryFeatures': 'VkExternalMemoryFeatureFlagsNV',
        'exportFromImportedHandleTypes': 'VkExternalMemoryHandleTypeFlagsNV',
        'compatibleHandleTypes': 'VkExternalMemoryHandleTypeFlagsNV',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkImageFormatProperties import VkImageFormatProperties

VkExternalImageFormatPropertiesNV._fields_ = [
    ('imageFormatProperties', VkImageFormatProperties),
    ('externalMemoryFeatures', ctypes.c_uint32),
    ('exportFromImportedHandleTypes', ctypes.c_uint32),
    ('compatibleHandleTypes', ctypes.c_uint32),
]

VkExternalImageFormatPropertiesNV._type_ = {
    'imageFormatProperties': VkImageFormatProperties,
    'externalMemoryFeatures': ctypes.c_uint32,
    'exportFromImportedHandleTypes': ctypes.c_uint32,
    'compatibleHandleTypes': ctypes.c_uint32,
}
