from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1LoopRestoration'
_member_list_ = ['FrameRestorationType', 'LoopRestorationSize']
_member_info_ = {
    'FrameRestorationType': {
        'type': CArrayType(CIntType('c_int'), 3),
        'type_name': 'StdVideoAV1FrameRestorationType',
        'enum': 'StdVideoAV1FrameRestorationType',
        'is_string': False,
    },
    'LoopRestorationSize': {
        'type': CArrayType(CIntType('c_uint16'), 3),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoDecodeAV1PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
