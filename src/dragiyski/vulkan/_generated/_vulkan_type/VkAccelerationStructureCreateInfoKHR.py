import ctypes

class VkAccelerationStructureCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('createFlags', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('type', ctypes.c_int),
        ('deviceAddress', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkAccelerationStructureMotionInfoNV',
        'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateAccelerationStructureKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'createFlags': 'create_flags',
        'buffer': 'buffer',
        'offset': 'offset',
        'size': 'size',
        'type': 'type',
        'deviceAddress': 'device_address',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'createFlags': 'VkAccelerationStructureCreateFlagsKHR',
        'type': 'VkAccelerationStructureTypeKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkAccelerationStructureCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'createFlags': ctypes.c_uint32,
    'buffer': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
    'size': ctypes.c_uint64,
    'type': ctypes.c_int,
    'deviceAddress': ctypes.c_uint64,
}
