from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoSessionCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'queueFamilyIndex', 'flags', 'pVideoProfile', 'pictureFormat', 'maxCodedExtent', 'referencePictureFormat', 'maxDpbSlots', 'maxActiveReferencePictures', 'pStdHeaderVersion']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_SESSION_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoSessionCreateFlagsKHR',
        'enum': 'VkVideoSessionCreateFlagsKHR',
        'is_string': False,
    },
    'pVideoProfile': {
        'type': CPointerType(CComplexType('VkVideoProfileInfoKHR')),
        'type_name': 'VkVideoProfileInfoKHR',
        'structure': 'VkVideoProfileInfoKHR',
        'is_string': False,
    },
    'pictureFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'maxCodedExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'referencePictureFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'maxDpbSlots': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxActiveReferencePictures': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStdHeaderVersion': {
        'type': CPointerType(CComplexType('VkExtensionProperties')),
        'type_name': 'VkExtensionProperties',
        'structure': 'VkExtensionProperties',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoEncodeH264SessionCreateInfoKHR',
    'VkVideoEncodeH265SessionCreateInfoKHR',
}
_includes_ = {
    'VkExtensionProperties',
    'VkExtent2D',
    'VkVideoProfileInfoKHR',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateVideoSessionKHR',
}
_output_of_ = set()
