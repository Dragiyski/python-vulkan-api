import ctypes

class VkAccelerationStructureTrianglesOpacityMicromapEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkAccelerationStructureGeometryTrianglesDataKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceOrHostAddressConstKHR',
        'VkMicromapUsageEXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'indexType': 'index_type',
        'indexBuffer': 'index_buffer',
        'indexStride': 'index_stride',
        'baseTriangle': 'base_triangle',
        'usageCountsCount': 'usage_counts_count',
        'pUsageCounts': 'usage_counts',
        'ppUsageCounts': 'usage_counts',
        'micromap': 'micromap',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_opacity_micromap',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'indexType': 'VkIndexType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_TRIANGLES_OPACITY_MICROMAP_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_TRIANGLES_OPACITY_MICROMAP_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR
from .VkMicromapUsageEXT import VkMicromapUsageEXT

VkAccelerationStructureTrianglesOpacityMicromapEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('indexType', ctypes.c_int),
    ('indexBuffer', VkDeviceOrHostAddressConstKHR),
    ('indexStride', ctypes.c_uint64),
    ('baseTriangle', ctypes.c_uint32),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('micromap', ctypes.c_void_p),
]

VkAccelerationStructureTrianglesOpacityMicromapEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'indexType': ctypes.c_int,
    'indexBuffer': VkDeviceOrHostAddressConstKHR,
    'indexStride': ctypes.c_uint64,
    'baseTriangle': ctypes.c_uint32,
    'usageCountsCount': ctypes.c_uint32,
    'pUsageCounts': ctypes.POINTER(VkMicromapUsageEXT),
    'ppUsageCounts': ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT)),
    'micromap': ctypes.c_void_p,
}
