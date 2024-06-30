from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeH265CapabilitiesKHR'
_member_list_ = ['sType', 'pNext', 'maxLevelIdc']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_CAPABILITIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxLevelIdc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265LevelIdc',
        'enum': 'StdVideoH265LevelIdc',
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
