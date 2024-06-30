from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265GopRemainingFrameInfoKHR'
_member_list_ = ['sType', 'pNext', 'useGopRemainingFrames', 'gopRemainingI', 'gopRemainingP', 'gopRemainingB']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_GOP_REMAINING_FRAME_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'useGopRemainingFrames': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'gopRemainingI': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'gopRemainingP': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'gopRemainingB': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoBeginCodingInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
