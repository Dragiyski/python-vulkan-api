import ctypes

class VkCuFunctionCreateInfoNVX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('module', ctypes.c_void_p),
        ('pName', ctypes.c_char_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateCuFunctionNVX',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'module': 'module',
        'pName': 'name',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NVX_binary_import',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_CU_FUNCTION_CREATE_INFO_NVX'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_CU_FUNCTION_CREATE_INFO_NVX
        for function in self._init_:
            function(self, *args, **kwargs)

VkCuFunctionCreateInfoNVX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'module': ctypes.c_void_p,
    'pName': ctypes.c_char_p,
}
