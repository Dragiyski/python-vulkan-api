from collections.abc import Collection
from ..xml.taxonomy import Taxonomy
from ..xml.node import Node

def enumerate_vulkan_names(taxonomy: Taxonomy, *, skip_names: Collection = ()):
    # VK_DEFINE_HANDLE and VK_DEFINE_NON_DISPATCHABLE_HANDLE only make sense in C preprocessor
    skip_names = set(skip_names) | {
        'VK_DEFINE_HANDLE',
        'VK_DEFINE_NON_DISPATCHABLE_HANDLE'
    }
    skip_callbacks = set()

    # Remove structures that are parsed, but their VkStructureType enum value was excluded.
    # The XML may specify some VK_STRUCTURE_* enums as vulkansc, but fail to specify the structures are vulkansc,
    # thus parsing the structure that do not belong to the current API
    skip_structure_types = {
        member_node.get_attribute('values')
        for name in taxonomy.category['complex']
        for node in taxonomy.nodes[name]
        for member_node in node.get_all('member')
        if (
            'name' in member_node.children
            and
            member_node.get('name').get_text() == 'sType'
            and
            member_node.has_attribute('values')
        )
    }.difference(taxonomy.group_value_map['VkStructureType'])

    # Exclude structure that refer to excluded structures
    skip_structures = {
        name
        for name in taxonomy.category['complex']
        for node in taxonomy.nodes[name]
        for member_node in node.get_all('member')
        if (
            'name' in member_node.children
            and
            member_node.get('name').get_text() == 'sType'
            and
            member_node.has_attribute('values')
            and
            member_node.get_attribute('values') in skip_structure_types
        )
    }
    skip_structures_len = len(skip_structures)

    while True:
        # Cascade exclude callback that refer to excluded structures, and then...
        skip_callbacks |= {
            name
            for name in taxonomy.category['callback']
            for node in taxonomy.nodes[name]
            for type_node in node.get_all('type')
            if type_node.get_text() in skip_structures
        }
        # Cascade exclude strctures that refer to excluded structures or callbacks.
        skip_structures |= {
            name
            for name in taxonomy.category['complex']
            for node in taxonomy.nodes[name]
            for member_node in node.get_all('member')
            if (
                'type' in member_node.children
                and (
                    member_node.get('type').get_text() in skip_structure_types
                    or
                    member_node.get('type').get_text() in skip_callbacks
                )
            )
        }
        # Keep cascading until no new results are added.
        if skip_structures_len == len(skip_structures):
            break
        skip_structures_len = len(skip_structures)
    skip_structure_callback = skip_structures | skip_callbacks

    # Exclude commands that refer to excluded structures or callbacks.
    skip_commands = set()
    for command_name, command_node in (
        (name, node)
        for name in taxonomy.category['command']
        for node in taxonomy.nodes[name]
        if 'proto' in node.children
    ):
        command_types = set(
            [command_node.get('proto').get('type').get_text()]
        ) | {
            param_node.get('type').get_text()
            for param_node in command_node.get_all('param')
        }
        if len(command_types & skip_structure_callback) > 0:
            skip_commands.add(command_name)
    
    # Collect all names to be excluded.
    skip_names |= skip_callbacks
    skip_names |= skip_commands
    skip_names |= skip_structures
    skip_names |= {x[4:] for x in skip_callbacks if x.startswith('PFN_')}

    names = set(taxonomy.nodes.keys()).difference(skip_names)
    # Replace all names starting with PFN_. We will refer to the function pointer by their direct name:
    # i.e., vkDebugReportCallbackEXT instead of PFN_vkDebugReportCallbackEXT
    pfn_names = {x for x in (names & taxonomy.category['callback']) if x.startswith('PFN_')}
    names = names.difference(pfn_names).union({x[4:] for x in pfn_names})

class AliasMap:
    def __init__(self, taxonomy: Taxonomy):
        self._taxonomy = taxonomy
    
    def __getitem__(self, name: str):
        if name not in self.__dict__:
            self.__dict__[name] = self._resolve_alias(name)
        return self.__dict__[name]
    
    def _resolve_alias(self, name: str):
        while name in self._taxonomy.category['alias']:
            for node in self._taxonomy.nodes[name]:
                node: Node
                if node.has_attribute('alias'):
                    name = node.get_attribute('alias')
        return name

class PreprocessorMetadata:
    def __init__(self, taxonomy: Taxonomy, names: set, alias_map: AliasMap):
        for name in self.taxonomy.category['define']:
            name = alias_map[name]
            if name not in names:
                continue
            

class AstMetadata:
    def __init__(self, taxonomy: Taxonomy):
        self._taxonomy = taxonomy
    

