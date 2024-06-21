from enum import IntFlag

class Value(IntFlag):
    VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT = 1
    VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT = 2
    VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT = 4
    VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT_KHR = VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT
    VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT_KHR = VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT
    VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT_KHR = VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT
