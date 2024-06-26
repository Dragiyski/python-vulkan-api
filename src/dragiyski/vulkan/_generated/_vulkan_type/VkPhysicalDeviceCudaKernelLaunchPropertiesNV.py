import ctypes

class VkPhysicalDeviceCudaKernelLaunchPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('computeCapabilityMinor', ctypes.c_uint32),
        ('computeCapabilityMajor', ctypes.c_uint32),
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
        'computeCapabilityMinor': 'compute_capability_minor',
        'computeCapabilityMajor': 'compute_capability_major',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_cuda_kernel_launch',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUDA_KERNEL_LAUNCH_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUDA_KERNEL_LAUNCH_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceCudaKernelLaunchPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'computeCapabilityMinor': ctypes.c_uint32,
    'computeCapabilityMajor': ctypes.c_uint32,
}
