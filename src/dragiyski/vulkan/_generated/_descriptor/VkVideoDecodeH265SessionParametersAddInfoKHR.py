from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeH265SessionParametersAddInfoKHR'
_member_list_ = ['sType', 'pNext', 'stdVPSCount', 'pStdVPSs', 'stdSPSCount', 'pStdSPSs', 'stdPPSCount', 'pStdPPSs']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_SESSION_PARAMETERS_ADD_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stdVPSCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStdVPSs': {
        'type': CPointerType(CComplexType('StdVideoH265VideoParameterSet')),
        'type_name': 'StdVideoH265VideoParameterSet',
        'structure': 'StdVideoH265VideoParameterSet',
        'length': [['stdVPSCount']],
        'is_string': False,
    },
    'stdSPSCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStdSPSs': {
        'type': CPointerType(CComplexType('StdVideoH265SequenceParameterSet')),
        'type_name': 'StdVideoH265SequenceParameterSet',
        'structure': 'StdVideoH265SequenceParameterSet',
        'length': [['stdSPSCount']],
        'is_string': False,
    },
    'stdPPSCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStdPPSs': {
        'type': CPointerType(CComplexType('StdVideoH265PictureParameterSet')),
        'type_name': 'StdVideoH265PictureParameterSet',
        'structure': 'StdVideoH265PictureParameterSet',
        'length': [['stdPPSCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoSessionParametersUpdateInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'StdVideoH265PictureParameterSet',
    'StdVideoH265SequenceParameterSet',
    'StdVideoH265VideoParameterSet',
}
_included_in_ = {
    'VkVideoDecodeH265SessionParametersCreateInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
