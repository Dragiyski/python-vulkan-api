import ctypes

class VkValidationFlagsEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('disabledValidationCheckCount', ctypes.c_uint32),
        ('pDisabledValidationChecks', ctypes.POINTER(ctypes.c_int)),
    ]

    _init_ = []
    _extends_ = {
        'VkInstanceCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'disabledValidationCheckCount': 'disabled_validation_check_count',
        'pDisabledValidationChecks': 'disabled_validation_checks',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_validation_flags',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pDisabledValidationChecks': 'VkValidationCheckEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VALIDATION_FLAGS_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VALIDATION_FLAGS_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkValidationFlagsEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'disabledValidationCheckCount': ctypes.c_uint32,
    'pDisabledValidationChecks': ctypes.POINTER(ctypes.c_int),
}
