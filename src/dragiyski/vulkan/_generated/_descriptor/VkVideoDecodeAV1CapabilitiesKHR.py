from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeAV1CapabilitiesKHR'
_member_list_ = ['sType', 'pNext', 'maxLevel']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_CAPABILITIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxLevel': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1Level',
        'enum': 'StdVideoAV1Level',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoCapabilitiesKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
