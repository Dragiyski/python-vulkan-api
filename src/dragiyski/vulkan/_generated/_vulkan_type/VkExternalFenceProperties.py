import ctypes

class VkExternalFenceProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
        ('externalFenceFeatures', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceExternalFenceProperties',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'exportFromImportedHandleTypes': 'export_from_imported_handle_types',
        'compatibleHandleTypes': 'compatible_handle_types',
        'externalFenceFeatures': 'external_fence_features',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'exportFromImportedHandleTypes': 'VkExternalFenceHandleTypeFlags',
        'compatibleHandleTypes': 'VkExternalFenceHandleTypeFlags',
        'externalFenceFeatures': 'VkExternalFenceFeatureFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_EXTERNAL_FENCE_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_FENCE_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkExternalFenceProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'exportFromImportedHandleTypes': ctypes.c_uint32,
    'compatibleHandleTypes': ctypes.c_uint32,
    'externalFenceFeatures': ctypes.c_uint32,
}
