import ctypes

class VkPhysicalDeviceVertexAttributeDivisorPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxVertexAttribDivisor', ctypes.c_uint32),
        ('supportsNonZeroFirstInstance', ctypes.c_uint32),
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
        'maxVertexAttribDivisor': 'max_vertex_attrib_divisor',
        'supportsNonZeroFirstInstance': 'supports_non_zero_first_instance',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_vertex_attribute_divisor',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceVertexAttributeDivisorPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxVertexAttribDivisor': ctypes.c_uint32,
    'supportsNonZeroFirstInstance': ctypes.c_uint32,
}
