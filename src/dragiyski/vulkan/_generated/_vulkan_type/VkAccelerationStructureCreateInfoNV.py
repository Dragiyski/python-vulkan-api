import ctypes

class VkAccelerationStructureCreateInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
    }
    _includes_ = {
        'VkAccelerationStructureInfoNV',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateAccelerationStructureNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'compactedSize': 'compacted_size',
        'info': 'info',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAccelerationStructureInfoNV import VkAccelerationStructureInfoNV

VkAccelerationStructureCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('compactedSize', ctypes.c_uint64),
    ('info', VkAccelerationStructureInfoNV),
]

VkAccelerationStructureCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'compactedSize': ctypes.c_uint64,
    'info': VkAccelerationStructureInfoNV,
}
