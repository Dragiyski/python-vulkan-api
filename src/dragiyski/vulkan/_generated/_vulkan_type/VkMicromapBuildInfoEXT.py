import ctypes

class VkMicromapBuildInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceOrHostAddressConstKHR',
        'VkDeviceOrHostAddressKHR',
        'VkMicromapUsageEXT',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkBuildMicromapsEXT',
        'vkCmdBuildMicromapsEXT',
        'vkGetMicromapBuildSizesEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'type': 'type',
        'flags': 'flags',
        'mode': 'mode',
        'dstMicromap': 'dst_micromap',
        'usageCountsCount': 'usage_counts_count',
        'pUsageCounts': 'usage_counts',
        'ppUsageCounts': 'usage_counts',
        'data': 'data',
        'scratchData': 'scratch_data',
        'triangleArray': 'triangle_array',
        'triangleArrayStride': 'triangle_array_stride',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_opacity_micromap',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'type': 'VkMicromapTypeEXT',
        'flags': 'VkBuildMicromapFlagsEXT',
        'mode': 'VkBuildMicromapModeEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MICROMAP_BUILD_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MICROMAP_BUILD_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR
from .VkDeviceOrHostAddressKHR import VkDeviceOrHostAddressKHR
from .VkMicromapUsageEXT import VkMicromapUsageEXT

VkMicromapBuildInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('mode', ctypes.c_int),
    ('dstMicromap', ctypes.c_void_p),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('data', VkDeviceOrHostAddressConstKHR),
    ('scratchData', VkDeviceOrHostAddressKHR),
    ('triangleArray', VkDeviceOrHostAddressConstKHR),
    ('triangleArrayStride', ctypes.c_uint64),
]

VkMicromapBuildInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'type': ctypes.c_int,
    'flags': ctypes.c_uint32,
    'mode': ctypes.c_int,
    'dstMicromap': ctypes.c_void_p,
    'usageCountsCount': ctypes.c_uint32,
    'pUsageCounts': ctypes.POINTER(VkMicromapUsageEXT),
    'ppUsageCounts': ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT)),
    'data': VkDeviceOrHostAddressConstKHR,
    'scratchData': VkDeviceOrHostAddressKHR,
    'triangleArray': VkDeviceOrHostAddressConstKHR,
    'triangleArrayStride': ctypes.c_uint64,
}
