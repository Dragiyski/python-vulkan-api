import ctypes

class VkPipelineVertexInputDivisorStateCreateInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPipelineVertexInputStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkVertexInputBindingDivisorDescriptionKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'vertexBindingDivisorCount': 'vertex_binding_divisor_count',
        'pVertexBindingDivisors': 'vertex_binding_divisors',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_vertex_attribute_divisor',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_DIVISOR_STATE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_DIVISOR_STATE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVertexInputBindingDivisorDescriptionKHR import VkVertexInputBindingDivisorDescriptionKHR

VkPipelineVertexInputDivisorStateCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexBindingDivisorCount', ctypes.c_uint32),
    ('pVertexBindingDivisors', ctypes.POINTER(VkVertexInputBindingDivisorDescriptionKHR)),
]

VkPipelineVertexInputDivisorStateCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vertexBindingDivisorCount': ctypes.c_uint32,
    'pVertexBindingDivisors': ctypes.POINTER(VkVertexInputBindingDivisorDescriptionKHR),
}
