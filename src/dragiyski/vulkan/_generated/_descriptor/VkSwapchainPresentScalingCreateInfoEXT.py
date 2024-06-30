from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSwapchainPresentScalingCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'scalingBehavior', 'presentGravityX', 'presentGravityY']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_SCALING_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'scalingBehavior': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPresentScalingFlagsEXT',
        'enum': 'VkPresentScalingFlagsEXT',
        'is_string': False,
    },
    'presentGravityX': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPresentGravityFlagsEXT',
        'enum': 'VkPresentGravityFlagsEXT',
        'is_string': False,
    },
    'presentGravityY': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPresentGravityFlagsEXT',
        'enum': 'VkPresentGravityFlagsEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkSwapchainCreateInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
