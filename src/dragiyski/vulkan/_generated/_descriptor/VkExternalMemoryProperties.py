from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExternalMemoryProperties'
_member_list_ = ['externalMemoryFeatures', 'exportFromImportedHandleTypes', 'compatibleHandleTypes']
_member_info_ = {
    'externalMemoryFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryFeatureFlags',
        'enum': 'VkExternalMemoryFeatureFlags',
        'is_string': False,
    },
    'exportFromImportedHandleTypes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryHandleTypeFlags',
        'enum': 'VkExternalMemoryHandleTypeFlags',
        'is_string': False,
    },
    'compatibleHandleTypes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryHandleTypeFlags',
        'enum': 'VkExternalMemoryHandleTypeFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkExternalBufferProperties',
    'VkExternalImageFormatProperties',
}
_input_of_ = set()
_output_of_ = set()
