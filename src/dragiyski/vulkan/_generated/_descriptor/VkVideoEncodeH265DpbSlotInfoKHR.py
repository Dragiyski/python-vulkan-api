from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265DpbSlotInfoKHR'
_member_list_ = ['sType', 'pNext', 'pStdReferenceInfo']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_DPB_SLOT_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pStdReferenceInfo': {
        'type': CPointerType(CComplexType('StdVideoEncodeH265ReferenceInfo')),
        'type_name': 'StdVideoEncodeH265ReferenceInfo',
        'structure': 'StdVideoEncodeH265ReferenceInfo',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoReferenceSlotInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH265ReferenceInfo',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
