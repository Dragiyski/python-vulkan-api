from . import c_types

native_types = {
    'char': c_types.CIntType('c_char'),
    'float': c_types.CFloatType('c_float'),
    'double': c_types.CFloatType('c_double'),
    'int8_t': c_types.CIntType('c_int8'),
    'uint8_t': c_types.CIntType('c_uint8'),
    'int16_t': c_types.CIntType('c_int16'),
    'uint16_t': c_types.CIntType('c_uint16'),
    'int32_t': c_types.CIntType('c_int32'),
    'uint32_t': c_types.CIntType('c_uint32'),
    'int64_t': c_types.CIntType('c_int64'),
    'uint64_t': c_types.CIntType('c_uint64'),
    'size_t': c_types.CIntType('c_size_t'),
    'int': c_types.CIntType('c_int'),
    'bool': c_types.CBooleanType('c_bool'),
    
}
