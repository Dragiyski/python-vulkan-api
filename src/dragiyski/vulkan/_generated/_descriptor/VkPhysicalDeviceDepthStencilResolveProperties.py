from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceDepthStencilResolveProperties'
_member_list_ = ['sType', 'pNext', 'supportedDepthResolveModes', 'supportedStencilResolveModes', 'independentResolveNone', 'independentResolve']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_STENCIL_RESOLVE_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'supportedDepthResolveModes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkResolveModeFlags',
        'enum': 'VkResolveModeFlags',
        'is_string': False,
    },
    'supportedStencilResolveModes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkResolveModeFlags',
        'enum': 'VkResolveModeFlags',
        'is_string': False,
    },
    'independentResolveNone': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'independentResolve': {
        'type': CIntType('c_uint32'),
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
