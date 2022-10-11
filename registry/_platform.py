import ctypes as _ctypes

basic_ctypes = {
    'void': None,
    'char': 'ctypes.c_char',
    'float': 'ctypes.c_float',
    'double': 'ctypes.c_double',
    'int8_t': 'ctypes.c_int8',
    'uint8_t': 'ctypes.c_uint8',
    'int16_t': 'ctypes.c_int16',
    'uint16_t': 'ctypes.c_uint16',
    'uint32_t': 'ctypes.c_uint32',
    'uint64_t': 'ctypes.c_uint64',
    'int32_t': 'ctypes.c_int32',
    'int64_t': 'ctypes.c_int64',
    'size_t': 'ctypes.c_size_t',
    'int': 'ctypes.c_int',
    'bool': 'ctypes.c_bool',
    'unsigned int': 'ctypes.c_uint',
    'unsigned long': 'ctypes.c_ulong',
    'unsigned short': 'ctypes.c_ushort',
    'unsigned char': 'ctypes.c_ubyte',
    'unsigned long long': 'ctypes.c_ulonglong',
    'int': 'ctypes.c_int',
    'long': 'ctypes.c_long',
    'short': 'ctypes.c_short',
    'char': 'ctypes.c_byte',
    'long long': 'ctypes.c_longlong'
}

# Predefined platform types that might be used directly (not as pointer).
platform_ctypes = {
    'VisualID': 'ctypes.c_uint32',  # X11/Xlib.h: CARD32
    'Window': 'ctypes.c_uint32',  # X11/Xlib.h: CARD32 => XID
    'RROutput': 'ctypes.c_uint32',  # X11/extensions/Xrandr.h
    'xcb_window_t': 'ctypes.c_uint32',  # xcb/xcb.h
    'HINSTANCE': 'ctypes.c_void_p',  # windows.h
    'HWND': 'ctypes.c_void_p',  # windows.h
    'HMONITOR': 'ctypes.c_void_p',  # windows.h
    'HANDLE': 'ctypes.c_void_p',  # windows.h
    'DWORD': 'ctypes.c_uint32',  # windows.h
    'LPCWSTR': 'ctypes.c_wchar_p',  # windows.h
    'zx_handle_t': 'ctypes.c_uint32',  # zircon/types.h (Fuschia?)
    'GgpStreamDescriptor': 'ctypes.c_uint32',  # Google games platform?
    'GgpFrameToken': 'ctypes.c_uint32',  # Google games platform?
}

handle_ctypes = {
    'VK_DEFINE_HANDLE': 'ctypes.c_void_p'
}

# Default type for Vulkan non-dispatchable handles: always 64-bit, defined as a pointer when on 64-bit system.
if _ctypes.sizeof(_ctypes.c_void_p) == 8:
    handle_ctypes['VK_DEFINE_NON_DISPATCHABLE_HANDLE'] = 'ctypes.c_void_p'
else:
    handle_ctypes['VK_DEFINE_NON_DISPATCHABLE_HANDLE'] = 'ctypes.c_uint64'
