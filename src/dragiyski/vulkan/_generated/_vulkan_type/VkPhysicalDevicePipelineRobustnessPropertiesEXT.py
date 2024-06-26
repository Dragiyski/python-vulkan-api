import ctypes

class VkPhysicalDevicePipelineRobustnessPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('defaultRobustnessStorageBuffers', ctypes.c_int),
        ('defaultRobustnessUniformBuffers', ctypes.c_int),
        ('defaultRobustnessVertexInputs', ctypes.c_int),
        ('defaultRobustnessImages', ctypes.c_int),
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
        'defaultRobustnessStorageBuffers': 'default_robustness_storage_buffers',
        'defaultRobustnessUniformBuffers': 'default_robustness_uniform_buffers',
        'defaultRobustnessVertexInputs': 'default_robustness_vertex_inputs',
        'defaultRobustnessImages': 'default_robustness_images',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_pipeline_robustness',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'defaultRobustnessStorageBuffers': 'VkPipelineRobustnessBufferBehaviorEXT',
        'defaultRobustnessUniformBuffers': 'VkPipelineRobustnessBufferBehaviorEXT',
        'defaultRobustnessVertexInputs': 'VkPipelineRobustnessBufferBehaviorEXT',
        'defaultRobustnessImages': 'VkPipelineRobustnessImageBehaviorEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_ROBUSTNESS_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_ROBUSTNESS_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDevicePipelineRobustnessPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'defaultRobustnessStorageBuffers': ctypes.c_int,
    'defaultRobustnessUniformBuffers': ctypes.c_int,
    'defaultRobustnessVertexInputs': ctypes.c_int,
    'defaultRobustnessImages': ctypes.c_int,
}
