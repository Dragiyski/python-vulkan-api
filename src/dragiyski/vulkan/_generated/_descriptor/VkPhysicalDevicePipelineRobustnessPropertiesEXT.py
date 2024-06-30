from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDevicePipelineRobustnessPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'defaultRobustnessStorageBuffers', 'defaultRobustnessUniformBuffers', 'defaultRobustnessVertexInputs', 'defaultRobustnessImages']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_ROBUSTNESS_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'defaultRobustnessStorageBuffers': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineRobustnessBufferBehaviorEXT',
        'enum': 'VkPipelineRobustnessBufferBehaviorEXT',
        'is_string': False,
    },
    'defaultRobustnessUniformBuffers': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineRobustnessBufferBehaviorEXT',
        'enum': 'VkPipelineRobustnessBufferBehaviorEXT',
        'is_string': False,
    },
    'defaultRobustnessVertexInputs': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineRobustnessBufferBehaviorEXT',
        'enum': 'VkPipelineRobustnessBufferBehaviorEXT',
        'is_string': False,
    },
    'defaultRobustnessImages': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineRobustnessImageBehaviorEXT',
        'enum': 'VkPipelineRobustnessImageBehaviorEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
