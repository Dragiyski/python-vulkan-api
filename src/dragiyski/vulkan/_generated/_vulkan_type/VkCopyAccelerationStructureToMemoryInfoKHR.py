import ctypes

class VkCopyAccelerationStructureToMemoryInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceOrHostAddressKHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdCopyAccelerationStructureToMemoryKHR',
        'vkCopyAccelerationStructureToMemoryKHR',
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
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COPY_ACCELERATION_STRUCTURE_TO_MEMORY_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_ACCELERATION_STRUCTURE_TO_MEMORY_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDeviceOrHostAddressKHR import VkDeviceOrHostAddressKHR

VkCopyAccelerationStructureToMemoryInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', ctypes.c_void_p),
    ('dst', VkDeviceOrHostAddressKHR),
    ('mode', ctypes.c_int),
]

VkCopyAccelerationStructureToMemoryInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'src': ctypes.c_void_p,
    'dst': VkDeviceOrHostAddressKHR,
    'mode': ctypes.c_int,
}
