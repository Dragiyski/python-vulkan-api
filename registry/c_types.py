class CType:
    pass

class VulkanType(CType):
    pass

class VulkanValueType(VulkanType):
    pass

class VulkanEnumType(VulkanValueType):
    pass

class VulkanBitmaskType(VulkanValueType):
    pass

class VulkanCallableType(VulkanType):
    pass

class VulkanCommandType(VulkanCallableType):
    pass

class VulkanCallbackType(VulkanCallableType):
    pass

class VulkanComplexType(VulkanType):
    pass

class VulkanChainStructType(VulkanComplexType):
    pass

class CVoidType(CType):
    pass

class COpaqueType(CType):
    pass

class CPlainType(CType):
    pass

class CBooleanType(CPlainType):
    pass

class CIntType(CPlainType):
    pass

class CFloatType(CPlainType):
    pass

class CStringType(CPlainType):
    pass

class CPointerType(CType):
    pass

class CArrayType(CType):
    pass