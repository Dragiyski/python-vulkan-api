import ctypes

class VkViSurfaceCreateInfoNN(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('window', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateViSurfaceNN',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'window': 'window',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NN_vi_surface',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkViSurfaceCreateFlagsNN',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VI_SURFACE_CREATE_INFO_NN'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VI_SURFACE_CREATE_INFO_NN
        for function in self._init_:
            function(self, *args, **kwargs)

VkViSurfaceCreateInfoNN._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'window': ctypes.c_void_p,
}
