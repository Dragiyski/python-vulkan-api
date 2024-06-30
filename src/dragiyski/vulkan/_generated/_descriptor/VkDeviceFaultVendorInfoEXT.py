from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceFaultVendorInfoEXT'
_member_list_ = ['description', 'vendorFaultCode', 'vendorFaultData']
_member_info_ = {
    'description': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'vendorFaultCode': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'vendorFaultData': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDeviceFaultInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
