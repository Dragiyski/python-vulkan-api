import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('headerSize', ctypes.c_uint32),
        ('headerVersion', ctypes.c_int),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('driverVersion', ctypes.c_uint32),
        ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('applicationNameOffset', ctypes.c_uint32),
        ('applicationVersion', ctypes.c_uint32),
        ('engineNameOffset', ctypes.c_uint32),
        ('engineVersion', ctypes.c_uint32),
        ('apiVersion', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'headerSize': {'python_name': ['header', 'size']},
        'headerVersion': {'python_name': ['header', 'version'], 'type': 'VkDeviceFaultVendorBinaryHeaderVersionEXT'},
        'vendorID': {'python_name': ['vendor', 'id']},
        'deviceID': {'python_name': ['device', 'id']},
        'driverVersion': {'python_name': ['driver', 'version']},
        'pipelineCacheUUID': {'python_name': ['pipeline', 'cache', 'uuid']},
        'applicationNameOffset': {'python_name': ['application', 'name', 'offset']},
        'applicationVersion': {'python_name': ['application', 'version']},
        'engineNameOffset': {'python_name': ['engine', 'name', 'offset']},
        'engineVersion': {'python_name': ['engine', 'version']},
        'apiVersion': {'python_name': ['api', 'version']},
    }
}
