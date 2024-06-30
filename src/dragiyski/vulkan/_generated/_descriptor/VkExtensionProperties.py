from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExtensionProperties'
_member_list_ = ['extensionName', 'specVersion']
_member_info_ = {
    'extensionName': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'specVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkVideoCapabilitiesKHR',
    'VkVideoSessionCreateInfoKHR',
}
_input_of_ = set()
_output_of_ = {
    'vkEnumerateDeviceExtensionProperties',
    'vkEnumerateInstanceExtensionProperties',
}
