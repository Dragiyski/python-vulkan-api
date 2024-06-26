import ctypes

class VkDeviceGroupBindSparseInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('resourceDeviceIndex', ctypes.c_uint32),
        ('memoryDeviceIndex', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkBindSparseInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'resourceDeviceIndex': 'resource_device_index',
        'memoryDeviceIndex': 'memory_device_index',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_GROUP_BIND_SPARSE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_BIND_SPARSE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceGroupBindSparseInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'resourceDeviceIndex': ctypes.c_uint32,
    'memoryDeviceIndex': ctypes.c_uint32,
}
