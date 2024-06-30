from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceVulkan13Properties'
_member_list_ = ['sType', 'pNext', 'minSubgroupSize', 'maxSubgroupSize', 'maxComputeWorkgroupSubgroups', 'requiredSubgroupSizeStages', 'maxInlineUniformBlockSize', 'maxPerStageDescriptorInlineUniformBlocks', 'maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks', 'maxDescriptorSetInlineUniformBlocks', 'maxDescriptorSetUpdateAfterBindInlineUniformBlocks', 'maxInlineUniformTotalSize', 'integerDotProduct8BitUnsignedAccelerated', 'integerDotProduct8BitSignedAccelerated', 'integerDotProduct8BitMixedSignednessAccelerated', 'integerDotProduct4x8BitPackedUnsignedAccelerated', 'integerDotProduct4x8BitPackedSignedAccelerated', 'integerDotProduct4x8BitPackedMixedSignednessAccelerated', 'integerDotProduct16BitUnsignedAccelerated', 'integerDotProduct16BitSignedAccelerated', 'integerDotProduct16BitMixedSignednessAccelerated', 'integerDotProduct32BitUnsignedAccelerated', 'integerDotProduct32BitSignedAccelerated', 'integerDotProduct32BitMixedSignednessAccelerated', 'integerDotProduct64BitUnsignedAccelerated', 'integerDotProduct64BitSignedAccelerated', 'integerDotProduct64BitMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating8BitUnsignedAccelerated', 'integerDotProductAccumulatingSaturating8BitSignedAccelerated', 'integerDotProductAccumulatingSaturating8BitMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating4x8BitPackedUnsignedAccelerated', 'integerDotProductAccumulatingSaturating4x8BitPackedSignedAccelerated', 'integerDotProductAccumulatingSaturating4x8BitPackedMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating16BitUnsignedAccelerated', 'integerDotProductAccumulatingSaturating16BitSignedAccelerated', 'integerDotProductAccumulatingSaturating16BitMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating32BitUnsignedAccelerated', 'integerDotProductAccumulatingSaturating32BitSignedAccelerated', 'integerDotProductAccumulatingSaturating32BitMixedSignednessAccelerated', 'integerDotProductAccumulatingSaturating64BitUnsignedAccelerated', 'integerDotProductAccumulatingSaturating64BitSignedAccelerated', 'integerDotProductAccumulatingSaturating64BitMixedSignednessAccelerated', 'storageTexelBufferOffsetAlignmentBytes', 'storageTexelBufferOffsetSingleTexelAlignment', 'uniformTexelBufferOffsetAlignmentBytes', 'uniformTexelBufferOffsetSingleTexelAlignment', 'maxBufferSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_3_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'minSubgroupSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxSubgroupSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxComputeWorkgroupSubgroups': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'requiredSubgroupSizeStages': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'maxInlineUniformBlockSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorInlineUniformBlocks': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetInlineUniformBlocks': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindInlineUniformBlocks': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxInlineUniformTotalSize': {
        'type': CIntType('c_uint32'),
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
    'storageTexelBufferOffsetAlignmentBytes': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'storageTexelBufferOffsetSingleTexelAlignment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'uniformTexelBufferOffsetAlignmentBytes': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'uniformTexelBufferOffsetSingleTexelAlignment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxBufferSize': {
        'type': CIntType('c_uint64'),
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
