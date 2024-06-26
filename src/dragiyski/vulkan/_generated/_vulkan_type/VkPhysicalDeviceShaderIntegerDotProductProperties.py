import ctypes

class VkPhysicalDeviceShaderIntegerDotProductProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('integerDotProduct8BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct8BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct8BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProduct4x8BitPackedUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct4x8BitPackedSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct4x8BitPackedMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProduct16BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct16BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct16BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProduct32BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct32BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct32BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProduct64BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct64BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProduct64BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating8BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating8BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating8BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating4x8BitPackedUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating4x8BitPackedSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating4x8BitPackedMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating16BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating16BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating16BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating32BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating32BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating32BitMixedSignednessAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating64BitUnsignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating64BitSignedAccelerated', ctypes.c_uint32),
        ('integerDotProductAccumulatingSaturating64BitMixedSignednessAccelerated', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'integerDotProduct8BitUnsignedAccelerated': 'integer_dot_product8_bit_unsigned_accelerated',
        'integerDotProduct8BitSignedAccelerated': 'integer_dot_product8_bit_signed_accelerated',
        'integerDotProduct8BitMixedSignednessAccelerated': 'integer_dot_product8_bit_mixed_signedness_accelerated',
        'integerDotProduct4x8BitPackedUnsignedAccelerated': 'integer_dot_product4x8_bit_packed_unsigned_accelerated',
        'integerDotProduct4x8BitPackedSignedAccelerated': 'integer_dot_product4x8_bit_packed_signed_accelerated',
        'integerDotProduct4x8BitPackedMixedSignednessAccelerated': 'integer_dot_product4x8_bit_packed_mixed_signedness_accelerated',
        'integerDotProduct16BitUnsignedAccelerated': 'integer_dot_product16_bit_unsigned_accelerated',
        'integerDotProduct16BitSignedAccelerated': 'integer_dot_product16_bit_signed_accelerated',
        'integerDotProduct16BitMixedSignednessAccelerated': 'integer_dot_product16_bit_mixed_signedness_accelerated',
        'integerDotProduct32BitUnsignedAccelerated': 'integer_dot_product32_bit_unsigned_accelerated',
        'integerDotProduct32BitSignedAccelerated': 'integer_dot_product32_bit_signed_accelerated',
        'integerDotProduct32BitMixedSignednessAccelerated': 'integer_dot_product32_bit_mixed_signedness_accelerated',
        'integerDotProduct64BitUnsignedAccelerated': 'integer_dot_product64_bit_unsigned_accelerated',
        'integerDotProduct64BitSignedAccelerated': 'integer_dot_product64_bit_signed_accelerated',
        'integerDotProduct64BitMixedSignednessAccelerated': 'integer_dot_product64_bit_mixed_signedness_accelerated',
        'integerDotProductAccumulatingSaturating8BitUnsignedAccelerated': 'integer_dot_product_accumulating_saturating8_bit_unsigned_accelerated',
        'integerDotProductAccumulatingSaturating8BitSignedAccelerated': 'integer_dot_product_accumulating_saturating8_bit_signed_accelerated',
        'integerDotProductAccumulatingSaturating8BitMixedSignednessAccelerated': 'integer_dot_product_accumulating_saturating8_bit_mixed_signedness_accelerated',
        'integerDotProductAccumulatingSaturating4x8BitPackedUnsignedAccelerated': 'integer_dot_product_accumulating_saturating4x8_bit_packed_unsigned_accelerated',
        'integerDotProductAccumulatingSaturating4x8BitPackedSignedAccelerated': 'integer_dot_product_accumulating_saturating4x8_bit_packed_signed_accelerated',
        'integerDotProductAccumulatingSaturating4x8BitPackedMixedSignednessAccelerated': 'integer_dot_product_accumulating_saturating4x8_bit_packed_mixed_signedness_accelerated',
        'integerDotProductAccumulatingSaturating16BitUnsignedAccelerated': 'integer_dot_product_accumulating_saturating16_bit_unsigned_accelerated',
        'integerDotProductAccumulatingSaturating16BitSignedAccelerated': 'integer_dot_product_accumulating_saturating16_bit_signed_accelerated',
        'integerDotProductAccumulatingSaturating16BitMixedSignednessAccelerated': 'integer_dot_product_accumulating_saturating16_bit_mixed_signedness_accelerated',
        'integerDotProductAccumulatingSaturating32BitUnsignedAccelerated': 'integer_dot_product_accumulating_saturating32_bit_unsigned_accelerated',
        'integerDotProductAccumulatingSaturating32BitSignedAccelerated': 'integer_dot_product_accumulating_saturating32_bit_signed_accelerated',
        'integerDotProductAccumulatingSaturating32BitMixedSignednessAccelerated': 'integer_dot_product_accumulating_saturating32_bit_mixed_signedness_accelerated',
        'integerDotProductAccumulatingSaturating64BitUnsignedAccelerated': 'integer_dot_product_accumulating_saturating64_bit_unsigned_accelerated',
        'integerDotProductAccumulatingSaturating64BitSignedAccelerated': 'integer_dot_product_accumulating_saturating64_bit_signed_accelerated',
        'integerDotProductAccumulatingSaturating64BitMixedSignednessAccelerated': 'integer_dot_product_accumulating_saturating64_bit_mixed_signedness_accelerated',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INTEGER_DOT_PRODUCT_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INTEGER_DOT_PRODUCT_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderIntegerDotProductProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'integerDotProduct8BitUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProduct8BitSignedAccelerated': ctypes.c_uint32,
    'integerDotProduct8BitMixedSignednessAccelerated': ctypes.c_uint32,
    'integerDotProduct4x8BitPackedUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProduct4x8BitPackedSignedAccelerated': ctypes.c_uint32,
    'integerDotProduct4x8BitPackedMixedSignednessAccelerated': ctypes.c_uint32,
    'integerDotProduct16BitUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProduct16BitSignedAccelerated': ctypes.c_uint32,
    'integerDotProduct16BitMixedSignednessAccelerated': ctypes.c_uint32,
    'integerDotProduct32BitUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProduct32BitSignedAccelerated': ctypes.c_uint32,
    'integerDotProduct32BitMixedSignednessAccelerated': ctypes.c_uint32,
    'integerDotProduct64BitUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProduct64BitSignedAccelerated': ctypes.c_uint32,
    'integerDotProduct64BitMixedSignednessAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating8BitUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating8BitSignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating8BitMixedSignednessAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating4x8BitPackedUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating4x8BitPackedSignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating4x8BitPackedMixedSignednessAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating16BitUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating16BitSignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating16BitMixedSignednessAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating32BitUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating32BitSignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating32BitMixedSignednessAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating64BitUnsignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating64BitSignedAccelerated': ctypes.c_uint32,
    'integerDotProductAccumulatingSaturating64BitMixedSignednessAccelerated': ctypes.c_uint32,
}
