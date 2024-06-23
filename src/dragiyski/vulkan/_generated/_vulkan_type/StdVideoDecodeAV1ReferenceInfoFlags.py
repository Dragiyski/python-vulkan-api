import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('disable_frame_end_update_cdf', ctypes.c_uint32, 1),
        ('segmentation_enabled', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoDecodeAV1ReferenceInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'disable_frame_end_update_cdf': {'python_name': ['disable', 'frame', 'end', 'update', 'cdf']},
        'segmentation_enabled': {'python_name': ['segmentation', 'enabled']},
        'reserved': {'python_name': ['reserved']},
    }
}
