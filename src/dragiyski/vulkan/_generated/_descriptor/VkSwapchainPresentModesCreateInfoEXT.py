from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSwapchainPresentModesCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'presentModeCount', 'pPresentModes']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_MODES_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'presentModeCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPresentModes': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkPresentModeKHR',
        'enum': 'VkPresentModeKHR',
        'length': [['presentModeCount']],
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
