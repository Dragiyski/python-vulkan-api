from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceImage2DViewOf3DFeaturesEXT'
_member_list_ = ['sType', 'pNext', 'image2DViewOf3D', 'sampler2DViewOf3D']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_2D_VIEW_OF_3D_FEATURES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image2DViewOf3D': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sampler2DViewOf3D': {
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
