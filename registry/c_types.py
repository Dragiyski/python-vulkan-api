from collections import OrderedDict

class CType:
    pass

class VulkanType(CType):
    def __init__(self, name):
        self.name = name

class VulkanValueType(VulkanType):
    def __init__(self, name, base_type):
        super().__init__(name)
        self.base_type = base_type

class VulkanEnumType(VulkanValueType):
    def __init__(self, name, base_type = 'c_int'):
        super().__init__(name, base_type)

class VulkanBitmaskType(VulkanValueType):
    pass

class VulkanCallableType(VulkanType):
    def __init__(self, name):
        super().__init__(name)
        self.return_type = None
        self.argument_type = []

class VulkanCommandType(VulkanCallableType):
    pass

class VulkanCallbackType(VulkanCallableType):
    pass

class VulkanComplexType(VulkanType):
    def __init__(self, name, constructor = 'Struct'):
        super().__init__(name)
        self.member_map = OrderedDict()
        self.constructor = constructor

class VulkanChainStructType(VulkanComplexType):
    pass

class CNativeType(CType):
    def __init__(self, name):
        self.name = name

class COpaqueType(CType):
    pass

class CPlainType(CNativeType):
    pass

class CBooleanType(CPlainType):
    pass

class CIntType(CPlainType):
    pass

class CFloatType(CPlainType):
    pass

class CPointerType(CType):
    def __init__(self, type: CType, *, input=False):
        self.type = type

class CStringPointerType(CPointerType):
    def __init__(self, char_type: CType, encoding='utf-8', **kwargs):
        super().__init__(char_type, **kwargs)
        self.encoding = encoding

class CArrayType(CType):
    def __init__(self, element_type: CType, length: int):
        self.element_type = element_type
        self.length = length

class CStringArrayType(CArrayType):
    def __init__(self, char_type: CType, length: int, encoding='utf-8', **kwargs):
        super().__init__(char_type, length, **kwargs)
        self.encoding = encoding

