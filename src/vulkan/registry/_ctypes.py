class CType:
    pass

class CVoidType(CType):
    pass

class CNativeType(CType):
    # Refer to ctypes.<attribute> type class that have ctypes.sizeof()
    pass

class CPointerType(CType):
    # Pointer type with no length
    pass

class CArrayType(CType):
    # Array with element type and fixed length
    pass

class CArrayPointerType(CType):
    # Pointer type with length attribute
    pass

class CExternalType(CType):
    # External opaque type, cannot be used directly, but pointers to that type can be obtained.
    pass

class CVulkanType(CType):
    # A Vulkan specific type (part of Vulkan API, not external).
    pass

class CVulkanComplexType(CType):
    # A Vulkan structure/union
    pass

class CVulkanEnumType(CType):
    # A Vulkan enumeration type (can be either enum or bitmask/flags)
    pass

class CCallableType(CType):
    pass

class CVulkanCallbackType(CCallableType):
    # A Vulkan callback signature. Expected to be bound to a python callable.
    pass

class CVulkanCommandType(CCallableType):
    # A Vulkan API function. Expected to be initialized to a pointer retrieved by `vkInstanceGetProcAddr`
    # or `vkDeviceGetProcAddr` (except for `vkInstanceGetProcAddr` whose pointer is expected to be retrieved by another means).
    pass