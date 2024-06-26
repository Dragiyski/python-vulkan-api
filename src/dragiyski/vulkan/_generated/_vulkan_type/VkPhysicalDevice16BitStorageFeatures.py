import ctypes

class VkPhysicalDevice16BitStorageFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffer16BitAccess', ctypes.c_uint32),
        ('uniformAndStorageBuffer16BitAccess', ctypes.c_uint32),
        ('storagePushConstant16', ctypes.c_uint32),
        ('storageInputOutput16', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'storageBuffer16BitAccess': 'storage_buffer16_bit_access',
        'uniformAndStorageBuffer16BitAccess': 'uniform_and_storage_buffer16_bit_access',
        'storagePushConstant16': 'storage_push_constant16',
        'storageInputOutput16': 'storage_input_output16',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDevice16BitStorageFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'storageBuffer16BitAccess': ctypes.c_uint32,
    'uniformAndStorageBuffer16BitAccess': ctypes.c_uint32,
    'storagePushConstant16': ctypes.c_uint32,
    'storageInputOutput16': ctypes.c_uint32,
}
