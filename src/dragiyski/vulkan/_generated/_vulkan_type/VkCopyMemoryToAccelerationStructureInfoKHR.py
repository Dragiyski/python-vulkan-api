import ctypes

class VkCopyMemoryToAccelerationStructureInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceOrHostAddressConstKHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdCopyMemoryToAccelerationStructureKHR',
        'vkCopyMemoryToAccelerationStructureKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'src': 'src',
        'dst': 'dst',
        'mode': 'mode',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'mode': 'VkCopyAccelerationStructureModeKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COPY_MEMORY_TO_ACCELERATION_STRUCTURE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_MEMORY_TO_ACCELERATION_STRUCTURE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkCopyMemoryToAccelerationStructureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', VkDeviceOrHostAddressConstKHR),
    ('dst', ctypes.c_void_p),
    ('mode', ctypes.c_int),
]

VkCopyMemoryToAccelerationStructureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'src': VkDeviceOrHostAddressConstKHR,
    'dst': ctypes.c_void_p,
    'mode': ctypes.c_int,
}
