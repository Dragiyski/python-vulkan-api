from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceLineRasterizationFeaturesKHR'
_member_list_ = ['sType', 'pNext', 'rectangularLines', 'bresenhamLines', 'smoothLines', 'stippledRectangularLines', 'stippledBresenhamLines', 'stippledSmoothLines']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_FEATURES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'rectangularLines': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bresenhamLines': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'smoothLines': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stippledRectangularLines': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stippledBresenhamLines': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stippledSmoothLines': {
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
