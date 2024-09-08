class CType:
    pass

class CVoidType(CType):
    __instance = None # Singleton
    pass

class CNativeType(CType):
    # Refer to ctypes.<attribute> type class that have ctypes.sizeof()
    pass

class CPointerType(CType):
    # Refer to ctypes type that is a typed pointer, namely:
    # 1. It has _type_ inner type, and
    # 2. It can access .contents if not NULL pointer
    # It doesn ot include c_void_p, instead c_Void_p is considered simple native type CNativeType
    # yet, underlying pointer value can be retrieved since this can be cast to c_void_p
    pass

class CArrayType(CType):
    # Array with element type and fixed length
    pass

class CComplexType(CType):
    # A complex type contain attributes. Every attribute have a CType and a name.
    pass

class CCallableType(CType):
    # A type that can called as a function, for example function types and CFuncPtr.
    # The underlying ctypes type can be constructed with:
    # 1. Python function to create a C callback. Very inefficient to use from python, but it can be given to C function to be called back or stored and recalled later.
    # 2. An int containin pointer address to create a python callable function that will invoke the underlying C function.

    # Crash may occur if:
    # 1. A callback created from the python
    pass