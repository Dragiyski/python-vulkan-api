import ctypes

class VkWriteDescriptorSetAccelerationStructureKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructureCount', ctypes.c_uint32),
        ('pAccelerationStructures', ctypes.POINTER(ctypes.c_void_p)),
    ]

    _init_ = []
    _extends_ = {
        'VkWriteDescriptorSet',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'accelerationStructureCount': 'acceleration_structure_count',
        'pAccelerationStructures': 'acceleration_structures',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_ACCELERATION_STRUCTURE_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_ACCELERATION_STRUCTURE_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkWriteDescriptorSetAccelerationStructureKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'accelerationStructureCount': ctypes.c_uint32,
    'pAccelerationStructures': ctypes.POINTER(ctypes.c_void_p),
}
