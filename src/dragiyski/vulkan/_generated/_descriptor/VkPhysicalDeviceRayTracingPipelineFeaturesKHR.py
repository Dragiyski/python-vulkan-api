from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceRayTracingPipelineFeaturesKHR'
_member_list_ = ['sType', 'pNext', 'rayTracingPipeline', 'rayTracingPipelineShaderGroupHandleCaptureReplay', 'rayTracingPipelineShaderGroupHandleCaptureReplayMixed', 'rayTracingPipelineTraceRaysIndirect', 'rayTraversalPrimitiveCulling']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_FEATURES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'rayTracingPipeline': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'rayTracingPipelineShaderGroupHandleCaptureReplay': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'rayTracingPipelineShaderGroupHandleCaptureReplayMixed': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'rayTracingPipelineTraceRaysIndirect': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'rayTraversalPrimitiveCulling': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
