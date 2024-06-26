import ctypes

class VkPhysicalDevicePrimitivesGeneratedQueryFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitivesGeneratedQuery', ctypes.c_uint32),
        ('primitivesGeneratedQueryWithRasterizerDiscard', ctypes.c_uint32),
        ('primitivesGeneratedQueryWithNonZeroStreams', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'primitivesGeneratedQuery': 'primitives_generated_query',
        'primitivesGeneratedQueryWithRasterizerDiscard': 'primitives_generated_query_with_rasterizer_discard',
        'primitivesGeneratedQueryWithNonZeroStreams': 'primitives_generated_query_with_non_zero_streams',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_primitives_generated_query',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIMITIVES_GENERATED_QUERY_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIMITIVES_GENERATED_QUERY_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDevicePrimitivesGeneratedQueryFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'primitivesGeneratedQuery': ctypes.c_uint32,
    'primitivesGeneratedQueryWithRasterizerDiscard': ctypes.c_uint32,
    'primitivesGeneratedQueryWithNonZeroStreams': ctypes.c_uint32,
}
