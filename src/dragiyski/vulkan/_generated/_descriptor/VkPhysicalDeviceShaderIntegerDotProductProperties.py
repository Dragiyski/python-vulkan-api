from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceShaderIntegerDotProductProperties'
_member_list_ = ['sType', 'pNext', 'integerDotProduct8BitUnsignedAccelerated', 'integerDotProduct8BitSignedAccelerated', 'integerDotProduct8BitMixedSignednessAccelerated', 'integerDotProduct4x8BitPackedUnsignedAccelerated', 'integerDotProduct4x8BitPackedSignedAccelerated', 'integerDotProduct4x8BitPackedMixedSignednessAccelerated', 'integerDotProduct16BitUnsignedAccelerated', 'integerDotProduct16BitSignedAccelerated', 'integerDotProduct16BitMixedSignednessAccelerated', 'integerDotProduct32BitUnsignedAccelerated', 'integerDotProduct32BitSignedAccelerated', 'integerDotProduct32BitMixedSignednessAccelerated', 'integerDotProduct64BitUnsignedAccelerated', 'integerDotProduct64BitSignedAccelerated', 'integerDotProduct64BitMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating8BitUnsignedAccelerated', 'integerDotProductAccumulatingSaturating8BitSignedAccelerated', 'integerDotProductAccumulatingSaturating8BitMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating4x8BitPackedUnsignedAccelerated', 'integerDotProductAccumulatingSaturating4x8BitPackedSignedAccelerated', 'integerDotProductAccumulatingSaturating4x8BitPackedMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating16BitUnsignedAccelerated', 'integerDotProductAccumulatingSaturating16BitSignedAccelerated', 'integerDotProductAccumulatingSaturating16BitMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating32BitUnsignedAccelerated', 'integerDotProductAccumulatingSaturating32BitSignedAccelerated', 'integerDotProductAccumulatingSaturating32BitMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating64BitUnsignedAccelerated', 'integerDotProductAccumulatingSaturating64BitSignedAccelerated', 'integerDotProductAccumulatingSaturating64BitMixedSignednessAccelerated']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INTEGER_DOT_PRODUCT_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'integerDotProduct8BitUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct8BitSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct8BitMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct4x8BitPackedUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct4x8BitPackedSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct4x8BitPackedMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct16BitUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct16BitSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct16BitMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct32BitUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct32BitSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct32BitMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct64BitUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct64BitSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProduct64BitMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating8BitUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating8BitSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating8BitMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating4x8BitPackedUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating4x8BitPackedSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating4x8BitPackedMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating16BitUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating16BitSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating16BitMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating32BitUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating32BitSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating32BitMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating64BitUnsignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating64BitSignedAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'integerDotProductAccumulatingSaturating64BitMixedSignednessAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
