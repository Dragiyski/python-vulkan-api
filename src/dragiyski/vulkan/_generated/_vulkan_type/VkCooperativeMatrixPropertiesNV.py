import ctypes

class VkCooperativeMatrixPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('MSize', ctypes.c_uint32),
        ('NSize', ctypes.c_uint32),
        ('KSize', ctypes.c_uint32),
        ('AType', ctypes.c_int),
        ('BType', ctypes.c_int),
        ('CType', ctypes.c_int),
        ('DType', ctypes.c_int),
        ('scope', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceCooperativeMatrixPropertiesNV',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'MSize': 'msize',
        'NSize': 'nsize',
        'KSize': 'ksize',
        'AType': 'atype',
        'BType': 'btype',
        'CType': 'ctype',
        'DType': 'dtype',
        'scope': 'scope',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_cooperative_matrix',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'AType': 'VkComponentTypeKHR',
        'BType': 'VkComponentTypeKHR',
        'CType': 'VkComponentTypeKHR',
        'DType': 'VkComponentTypeKHR',
        'scope': 'VkScopeKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COOPERATIVE_MATRIX_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COOPERATIVE_MATRIX_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkCooperativeMatrixPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'MSize': ctypes.c_uint32,
    'NSize': ctypes.c_uint32,
    'KSize': ctypes.c_uint32,
    'AType': ctypes.c_int,
    'BType': ctypes.c_int,
    'CType': ctypes.c_int,
    'DType': ctypes.c_int,
    'scope': ctypes.c_int,
}
