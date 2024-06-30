from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceFaultVendorBinaryHeaderVersionOneEXT'
_member_list_ = ['headerSize', 'headerVersion', 'vendorID', 'deviceID', 'driverVersion', 'pipelineCacheUUID', 'applicationNameOffset', 'applicationVersion', 'engineNameOffset', 'engineVersion', 'apiVersion']
_member_info_ = {
    'headerSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'headerVersion': {
        'type': CIntType('c_int'),
        'type_name': 'VkDeviceFaultVendorBinaryHeaderVersionEXT',
        'enum': 'VkDeviceFaultVendorBinaryHeaderVersionEXT',
        'is_string': False,
    },
    'vendorID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'deviceID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'driverVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pipelineCacheUUID': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
    'applicationNameOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'applicationVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'engineNameOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'engineVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'apiVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
