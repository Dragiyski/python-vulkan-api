import ctypes

class VkCudaModuleCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dataSize', ctypes.c_size_t),
        ('pData', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateCudaModuleNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'dataSize': 'data_size',
        'pData': 'data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_cuda_kernel_launch',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_CUDA_MODULE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_CUDA_MODULE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkCudaModuleCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'dataSize': ctypes.c_size_t,
    'pData': ctypes.c_void_p,
}
