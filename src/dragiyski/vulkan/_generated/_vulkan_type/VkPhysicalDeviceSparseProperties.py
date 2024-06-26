import ctypes

class VkPhysicalDeviceSparseProperties(ctypes.Structure):
    _fields_ = [
        ('residencyStandard2DBlockShape', ctypes.c_uint32),
        ('residencyStandard2DMultisampleBlockShape', ctypes.c_uint32),
        ('residencyStandard3DBlockShape', ctypes.c_uint32),
        ('residencyAlignedMipSize', ctypes.c_uint32),
        ('residencyNonResidentStrict', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPhysicalDeviceProperties',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'residencyStandard2DBlockShape': 'residency_standard2_dblock_shape',
        'residencyStandard2DMultisampleBlockShape': 'residency_standard2_dmultisample_block_shape',
        'residencyStandard3DBlockShape': 'residency_standard3_dblock_shape',
        'residencyAlignedMipSize': 'residency_aligned_mip_size',
        'residencyNonResidentStrict': 'residency_non_resident_strict',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceSparseProperties._type_ = {
    'residencyStandard2DBlockShape': ctypes.c_uint32,
    'residencyStandard2DMultisampleBlockShape': ctypes.c_uint32,
    'residencyStandard3DBlockShape': ctypes.c_uint32,
    'residencyAlignedMipSize': ctypes.c_uint32,
    'residencyNonResidentStrict': ctypes.c_uint32,
}
