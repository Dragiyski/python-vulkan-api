import ctypes

class VkAccelerationStructureBuildSizesInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructureSize', ctypes.c_uint64),
        ('updateScratchSize', ctypes.c_uint64),
        ('buildScratchSize', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetAccelerationStructureBuildSizesKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'accelerationStructureSize': 'acceleration_structure_size',
        'updateScratchSize': 'update_scratch_size',
        'buildScratchSize': 'build_scratch_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_SIZES_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_SIZES_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkAccelerationStructureBuildSizesInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'accelerationStructureSize': ctypes.c_uint64,
    'updateScratchSize': ctypes.c_uint64,
    'buildScratchSize': ctypes.c_uint64,
}
