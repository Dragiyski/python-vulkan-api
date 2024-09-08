import ctypes

native_types = {
    'char': ctypes.c_char,
    'float': ctypes.c_float,
    'double': ctypes.c_double,
    'int8_t': ctypes.c_int8,
    'uint8_t': ctypes.c_uint8,
    'int16_t': ctypes.c_int16,
    'uint16_t': ctypes.c_uint16,
    'uint32_t': ctypes.c_uint32,
    'uint64_t': ctypes.c_uint64,
    'int32_t': ctypes.c_int32,
    'int64_t': ctypes.c_int64,
    'size_t': ctypes.c_size_t,
    'int': ctypes.c_int,
    'bool': ctypes.c_bool,
    'unsigned int': ctypes.c_uint,
    'unsigned long': ctypes.c_ulong,
    'unsigned long int': ctypes.c_ulong,
    'unsigned short': ctypes.c_ushort,
    'unsigned short int': ctypes.c_ushort,
    'unsigned char': ctypes.c_ubyte,
    'unsigned long long': ctypes.c_ulonglong,
    'unsigned long long int': ctypes.c_ulonglong,
    'int': ctypes.c_int,
    'long': ctypes.c_long,
    'long int': ctypes.c_long,
    'short': ctypes.c_short,
    'short int': ctypes.c_short,
    'long long': ctypes.c_longlong,
    'long long int': ctypes.c_longlong,
}

# List of platform type aliases.
# Note: does not include opaque types, only direct types.
platform_types = {
    'VisualID': ctypes.c_uint32,  # X11/Xlib.h: CARD32
    'Window': ctypes.c_uint32,  # X11/Xlib.h: CARD32 => XID
    'RROutput': ctypes.c_uint32,  # X11/extensions/Xrandr.h
    'xcb_window_t': ctypes.c_uint32,  # xcb/xcb.h
    'xcb_visualid_t': ctypes.c_uint32, # xcb/xcb.h
    'HINSTANCE': ctypes.c_void_p,  # windows.h
    'HWND': ctypes.c_void_p,  # windows.h
    'HMONITOR': ctypes.c_void_p,  # windows.h
    'HANDLE': ctypes.c_void_p,  # windows.h
    'DWORD': ctypes.c_uint32,  # windows.h
    'LPCSTR': ctypes.c_char_p,  # windows.h
    'LPCTSTR': ctypes.c_char_p,  # windows.h
    'LPCWSTR': ctypes.c_wchar_p,  # windows.h
    'zx_handle_t': ctypes.c_uint32,  # zircon/types.h (Fuschia?)
    'GgpStreamDescriptor': ctypes.c_uint32,  # Google games platform?
    'GgpFrameToken': ctypes.c_uint32,  # Google games platform?
    'NvSciSyncAttrList': ctypes.c_void_p, # NV Sci Platform
    'NvSciSyncObj': ctypes.c_void_p, # NV Sci Platform
    'NvSciSyncFence': ctypes.c_uint64 * 6, # NV Sci Platform
    'NvSciBufAttrList': ctypes.c_void_p, # NV Sci Platform
    'NvSciBufObj': ctypes.c_void_p, # NV Sci Platform
}

macro_values = {
    'VK_NULL_HANDLE': None,
    'VK_USE_64_BIT_PTR_DEFINES': ctypes.sizeof(ctypes.c_void_p) == 8
}

macro_ignore = {
    'VK_DEFINE_HANDLE',
    'VK_DEFINE_NON_DISPATCHABLE_HANDLE'
}