import ctypes

class VkBindImageMemoryDeviceGroupInfo(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkBindImageMemoryInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkRect2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'deviceIndexCount': 'device_index_count',
        'pDeviceIndices': 'device_indices',
        'splitInstanceBindRegionCount': 'split_instance_bind_region_count',
        'pSplitInstanceBindRegions': 'split_instance_bind_regions',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_DEVICE_GROUP_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_DEVICE_GROUP_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkBindImageMemoryDeviceGroupInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('deviceIndexCount', ctypes.c_uint32),
    ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ('splitInstanceBindRegionCount', ctypes.c_uint32),
    ('pSplitInstanceBindRegions', ctypes.POINTER(VkRect2D)),
]

VkBindImageMemoryDeviceGroupInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceIndexCount': ctypes.c_uint32,
    'pDeviceIndices': ctypes.POINTER(ctypes.c_uint32),
    'splitInstanceBindRegionCount': ctypes.c_uint32,
    'pSplitInstanceBindRegions': ctypes.POINTER(VkRect2D),
}
