from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkShaderResourceUsageAMD'
_member_list_ = ['numUsedVgprs', 'numUsedSgprs', 'ldsSizePerLocalWorkGroup', 'ldsUsageSizeInBytes', 'scratchMemUsageInBytes']
_member_info_ = {
    'numUsedVgprs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'numUsedSgprs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'ldsSizePerLocalWorkGroup': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'ldsUsageSizeInBytes': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'scratchMemUsageInBytes': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkShaderStatisticsInfoAMD',
}
_input_of_ = set()
_output_of_ = set()
