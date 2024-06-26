import ctypes

class VkCudaFunctionCreateInfoNV(ctypes.Structure):
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
        'vkCreateCudaFunctionNV',
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
        'VK_NV_cuda_kernel_launch',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_CUDA_FUNCTION_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_CUDA_FUNCTION_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkCudaFunctionCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'module': ctypes.c_void_p,
    'pName': ctypes.c_char_p,
}
