from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceRayTracingInvocationReorderPropertiesNV'
_member_list_ = ['sType', 'pNext', 'rayTracingInvocationReorderReorderingHint']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_INVOCATION_REORDER_PROPERTIES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'rayTracingInvocationReorderReorderingHint': {
        'type': CIntType('c_int'),
        'type_name': 'VkRayTracingInvocationReorderModeNV',
        'enum': 'VkRayTracingInvocationReorderModeNV',
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
