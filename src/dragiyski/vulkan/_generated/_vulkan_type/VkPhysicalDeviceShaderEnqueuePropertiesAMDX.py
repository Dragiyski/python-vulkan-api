import ctypes

class VkPhysicalDeviceShaderEnqueuePropertiesAMDX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxExecutionGraphDepth', ctypes.c_uint32),
        ('maxExecutionGraphShaderOutputNodes', ctypes.c_uint32),
        ('maxExecutionGraphShaderPayloadSize', ctypes.c_uint32),
        ('maxExecutionGraphShaderPayloadCount', ctypes.c_uint32),
        ('executionGraphDispatchAddressAlignment', ctypes.c_uint32),
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
        'maxExecutionGraphDepth': 'max_execution_graph_depth',
        'maxExecutionGraphShaderOutputNodes': 'max_execution_graph_shader_output_nodes',
        'maxExecutionGraphShaderPayloadSize': 'max_execution_graph_shader_payload_size',
        'maxExecutionGraphShaderPayloadCount': 'max_execution_graph_shader_payload_count',
        'executionGraphDispatchAddressAlignment': 'execution_graph_dispatch_address_alignment',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMDX_shader_enqueue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ENQUEUE_PROPERTIES_AMDX'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ENQUEUE_PROPERTIES_AMDX
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderEnqueuePropertiesAMDX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxExecutionGraphDepth': ctypes.c_uint32,
    'maxExecutionGraphShaderOutputNodes': ctypes.c_uint32,
    'maxExecutionGraphShaderPayloadSize': ctypes.c_uint32,
    'maxExecutionGraphShaderPayloadCount': ctypes.c_uint32,
    'executionGraphDispatchAddressAlignment': ctypes.c_uint32,
}
