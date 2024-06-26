import ctypes

class VkExternalSemaphoreProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
        ('externalSemaphoreFeatures', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceExternalSemaphoreProperties',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'exportFromImportedHandleTypes': 'export_from_imported_handle_types',
        'compatibleHandleTypes': 'compatible_handle_types',
        'externalSemaphoreFeatures': 'external_semaphore_features',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'exportFromImportedHandleTypes': 'VkExternalSemaphoreHandleTypeFlags',
        'compatibleHandleTypes': 'VkExternalSemaphoreHandleTypeFlags',
        'externalSemaphoreFeatures': 'VkExternalSemaphoreFeatureFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_EXTERNAL_SEMAPHORE_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_SEMAPHORE_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkExternalSemaphoreProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'exportFromImportedHandleTypes': ctypes.c_uint32,
    'compatibleHandleTypes': ctypes.c_uint32,
    'externalSemaphoreFeatures': ctypes.c_uint32,
}
