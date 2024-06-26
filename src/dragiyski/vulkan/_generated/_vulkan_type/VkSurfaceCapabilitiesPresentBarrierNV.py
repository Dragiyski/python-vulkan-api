import ctypes

class VkSurfaceCapabilitiesPresentBarrierNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentBarrierSupported', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkSurfaceCapabilities2KHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'presentBarrierSupported': 'present_barrier_supported',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_present_barrier',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_PRESENT_BARRIER_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_PRESENT_BARRIER_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkSurfaceCapabilitiesPresentBarrierNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentBarrierSupported': ctypes.c_uint32,
}
