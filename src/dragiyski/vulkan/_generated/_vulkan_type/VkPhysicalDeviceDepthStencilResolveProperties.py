import ctypes

class VkPhysicalDeviceDepthStencilResolveProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedDepthResolveModes', ctypes.c_uint32),
        ('supportedStencilResolveModes', ctypes.c_uint32),
        ('independentResolveNone', ctypes.c_uint32),
        ('independentResolve', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'supportedDepthResolveModes': 'supported_depth_resolve_modes',
        'supportedStencilResolveModes': 'supported_stencil_resolve_modes',
        'independentResolveNone': 'independent_resolve_none',
        'independentResolve': 'independent_resolve',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'supportedDepthResolveModes': 'VkResolveModeFlags',
        'supportedStencilResolveModes': 'VkResolveModeFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_STENCIL_RESOLVE_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_STENCIL_RESOLVE_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceDepthStencilResolveProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supportedDepthResolveModes': ctypes.c_uint32,
    'supportedStencilResolveModes': ctypes.c_uint32,
    'independentResolveNone': ctypes.c_uint32,
    'independentResolve': ctypes.c_uint32,
}
