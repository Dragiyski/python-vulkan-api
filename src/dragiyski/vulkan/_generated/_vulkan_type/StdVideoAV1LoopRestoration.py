import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('FrameRestorationType', ctypes.ARRAY(ctypes.c_int, 3)),
        ('LoopRestorationSize', ctypes.ARRAY(ctypes.c_uint16, 3)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoDecodeAV1PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'FrameRestorationType': {'python_name': ['frame', 'restoration', 'type'], 'type': 'StdVideoAV1FrameRestorationType'},
        'LoopRestorationSize': {'python_name': ['loop', 'restoration', 'size']},
    }
}
