import ctypes

c_handle_type = ctypes.c_void_p if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_uint64
