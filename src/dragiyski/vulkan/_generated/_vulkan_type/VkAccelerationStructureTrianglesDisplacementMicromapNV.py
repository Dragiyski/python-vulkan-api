import ctypes

class VkAccelerationStructureTrianglesDisplacementMicromapNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkAccelerationStructureGeometryTrianglesDataKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceOrHostAddressConstKHR',
        'VkMicromapUsageEXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'displacementBiasAndScaleFormat': 'displacement_bias_and_scale_format',
        'displacementVectorFormat': 'displacement_vector_format',
        'displacementBiasAndScaleBuffer': 'displacement_bias_and_scale_buffer',
        'displacementBiasAndScaleStride': 'displacement_bias_and_scale_stride',
        'displacementVectorBuffer': 'displacement_vector_buffer',
        'displacementVectorStride': 'displacement_vector_stride',
        'displacedMicromapPrimitiveFlags': 'displaced_micromap_primitive_flags',
        'displacedMicromapPrimitiveFlagsStride': 'displaced_micromap_primitive_flags_stride',
        'indexType': 'index_type',
        'indexBuffer': 'index_buffer',
        'indexStride': 'index_stride',
        'baseTriangle': 'base_triangle',
        'usageCountsCount': 'usage_counts_count',
        'pUsageCounts': 'usage_counts',
        'ppUsageCounts': 'usage_counts',
        'micromap': 'micromap',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_displacement_micromap',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'displacementBiasAndScaleFormat': 'VkFormat',
        'displacementVectorFormat': 'VkFormat',
        'indexType': 'VkIndexType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_TRIANGLES_DISPLACEMENT_MICROMAP_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_TRIANGLES_DISPLACEMENT_MICROMAP_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR
from .VkMicromapUsageEXT import VkMicromapUsageEXT

VkAccelerationStructureTrianglesDisplacementMicromapNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displacementBiasAndScaleFormat', ctypes.c_int),
    ('displacementVectorFormat', ctypes.c_int),
    ('displacementBiasAndScaleBuffer', VkDeviceOrHostAddressConstKHR),
    ('displacementBiasAndScaleStride', ctypes.c_uint64),
    ('displacementVectorBuffer', VkDeviceOrHostAddressConstKHR),
    ('displacementVectorStride', ctypes.c_uint64),
    ('displacedMicromapPrimitiveFlags', VkDeviceOrHostAddressConstKHR),
    ('displacedMicromapPrimitiveFlagsStride', ctypes.c_uint64),
    ('indexType', ctypes.c_int),
    ('indexBuffer', VkDeviceOrHostAddressConstKHR),
    ('indexStride', ctypes.c_uint64),
    ('baseTriangle', ctypes.c_uint32),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('micromap', ctypes.c_void_p),
]

VkAccelerationStructureTrianglesDisplacementMicromapNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'displacementBiasAndScaleFormat': ctypes.c_int,
    'displacementVectorFormat': ctypes.c_int,
    'displacementBiasAndScaleBuffer': VkDeviceOrHostAddressConstKHR,
    'displacementBiasAndScaleStride': ctypes.c_uint64,
    'displacementVectorBuffer': VkDeviceOrHostAddressConstKHR,
    'displacementVectorStride': ctypes.c_uint64,
    'displacedMicromapPrimitiveFlags': VkDeviceOrHostAddressConstKHR,
    'displacedMicromapPrimitiveFlagsStride': ctypes.c_uint64,
    'indexType': ctypes.c_int,
    'indexBuffer': VkDeviceOrHostAddressConstKHR,
    'indexStride': ctypes.c_uint64,
    'baseTriangle': ctypes.c_uint32,
    'usageCountsCount': ctypes.c_uint32,
    'pUsageCounts': ctypes.POINTER(VkMicromapUsageEXT),
    'ppUsageCounts': ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT)),
    'micromap': ctypes.c_void_p,
}
