import ctypes

class VkPresentFrameTokenGGP(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('frameToken', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPresentInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'frameToken': 'frame_token',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_GGP_frame_token',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PRESENT_FRAME_TOKEN_GGP'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_FRAME_TOKEN_GGP
        for function in self._init_:
            function(self, *args, **kwargs)

VkPresentFrameTokenGGP._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'frameToken': ctypes.c_uint32,
}
