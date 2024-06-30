from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH264SessionParametersAddInfoKHR'
_member_list_ = ['sType', 'pNext', 'stdSPSCount', 'pStdSPSs', 'stdPPSCount', 'pStdPPSs']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_PARAMETERS_ADD_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stdSPSCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStdSPSs': {
        'type': CPointerType(CComplexType('StdVideoH264SequenceParameterSet')),
        'type_name': 'StdVideoH264SequenceParameterSet',
        'structure': 'StdVideoH264SequenceParameterSet',
        'length': [['stdSPSCount']],
        'is_string': False,
    },
    'stdPPSCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStdPPSs': {
        'type': CPointerType(CComplexType('StdVideoH264PictureParameterSet')),
        'type_name': 'StdVideoH264PictureParameterSet',
        'structure': 'StdVideoH264PictureParameterSet',
        'length': [['stdPPSCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoSessionParametersUpdateInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'StdVideoH264PictureParameterSet',
    'StdVideoH264SequenceParameterSet',
}
_included_in_ = {
    'VkVideoEncodeH264SessionParametersCreateInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
