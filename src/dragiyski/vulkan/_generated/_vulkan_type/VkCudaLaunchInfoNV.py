import ctypes

class VkCudaLaunchInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('function', ctypes.c_void_p),
        ('gridDimX', ctypes.c_uint32),
        ('gridDimY', ctypes.c_uint32),
        ('gridDimZ', ctypes.c_uint32),
        ('blockDimX', ctypes.c_uint32),
        ('blockDimY', ctypes.c_uint32),
        ('blockDimZ', ctypes.c_uint32),
        ('sharedMemBytes', ctypes.c_uint32),
        ('paramCount', ctypes.c_size_t),
        ('pParams', ctypes.POINTER(ctypes.c_void_p)),
        ('extraCount', ctypes.c_size_t),
        ('pExtras', ctypes.POINTER(ctypes.c_void_p)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdCudaLaunchKernelNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'function': 'function',
        'gridDimX': 'grid_dim_x',
        'gridDimY': 'grid_dim_y',
        'gridDimZ': 'grid_dim_z',
        'blockDimX': 'block_dim_x',
        'blockDimY': 'block_dim_y',
        'blockDimZ': 'block_dim_z',
        'sharedMemBytes': 'shared_mem_bytes',
        'paramCount': 'param_count',
        'pParams': 'params',
        'extraCount': 'extra_count',
        'pExtras': 'extras',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_cuda_kernel_launch',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_CUDA_LAUNCH_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_CUDA_LAUNCH_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkCudaLaunchInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'function': ctypes.c_void_p,
    'gridDimX': ctypes.c_uint32,
    'gridDimY': ctypes.c_uint32,
    'gridDimZ': ctypes.c_uint32,
    'blockDimX': ctypes.c_uint32,
    'blockDimY': ctypes.c_uint32,
    'blockDimZ': ctypes.c_uint32,
    'sharedMemBytes': ctypes.c_uint32,
    'paramCount': ctypes.c_size_t,
    'pParams': ctypes.POINTER(ctypes.c_void_p),
    'extraCount': ctypes.c_size_t,
    'pExtras': ctypes.POINTER(ctypes.c_void_p),
}
