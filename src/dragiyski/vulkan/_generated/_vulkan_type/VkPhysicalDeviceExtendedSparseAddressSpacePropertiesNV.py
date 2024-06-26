import ctypes

class VkPhysicalDeviceExtendedSparseAddressSpacePropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('extendedSparseAddressSpaceSize', ctypes.c_uint64),
        ('extendedSparseImageUsageFlags', ctypes.c_uint32),
        ('extendedSparseBufferUsageFlags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'extendedSparseAddressSpaceSize': 'extended_sparse_address_space_size',
        'extendedSparseImageUsageFlags': 'extended_sparse_image_usage_flags',
        'extendedSparseBufferUsageFlags': 'extended_sparse_buffer_usage_flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_extended_sparse_address_space',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'extendedSparseImageUsageFlags': 'VkImageUsageFlags',
        'extendedSparseBufferUsageFlags': 'VkBufferUsageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_SPARSE_ADDRESS_SPACE_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_SPARSE_ADDRESS_SPACE_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceExtendedSparseAddressSpacePropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'extendedSparseAddressSpaceSize': ctypes.c_uint64,
    'extendedSparseImageUsageFlags': ctypes.c_uint32,
    'extendedSparseBufferUsageFlags': ctypes.c_uint32,
}
