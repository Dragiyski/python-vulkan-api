import pathlib, logging, os, pycparser.c_ast
from setuptools import Command
from .node import parse_xml
from .xml import get_data
from . import c_types

class VulkanRegistryGenerateCommand(Command):
    description = 'generate vulkan binding source files and meta information'

    user_options = [
        ('xml-dir=', 's', 'directory containing xml registry files'),
        ('target-dir=', 't', 'directory containing xml registry files'),
    ]

    def initialize_options(self) -> None:
        self.logger = logging.getLogger('vulkan.registry')
        self.xml_dir = pathlib.Path(__file__).resolve().parent.parent.joinpath('var')
        self.target_dir = pathlib.Path(__file__).resolve().parent.parent.joinpath('src')

    def finalize_options(self) -> None:
        self.xml_dir = pathlib.Path(self.xml_dir).resolve()
        self.target_dir = pathlib.Path(self.target_dir).resolve()
        if self.distribution.verbose:
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.CRITICAL)

    @classmethod
    def _xml_iterator(cls, dir: pathlib.Path):
        for entry in os.scandir(dir):
            entry: os.DirEntry
            if entry.is_dir(follow_symlinks=False):
                yield from cls._xml_iterator(dir.joinpath(entry.name))
            elif entry.is_file():
                path = dir.joinpath(entry.name)
                if path.suffix.lower() == '.xml':
                    yield path

    def run(self) -> None:
        files = [file for file in self._xml_iterator(self.xml_dir)]
        metadata = get_data(*files)
        metadata.ctypes = {
            'void': None,
            'char': c_types.CIntType('c_char'),
            'float': c_types.CFloatType('c_float'),
            'double': c_types.CFloatType('c_double'),
            'int8_t': c_types.CIntType('c_int8'),
            'uint8_t': c_types.CIntType('c_uint8'),
            'int16_t': c_types.CIntType('c_int16'),
            'uint16_t': c_types.CIntType('c_uint16'),
            'uint32_t': c_types.CIntType('c_uint32'),
            'uint64_t': c_types.CIntType('c_uint64'),
            'int32_t': c_types.CIntType('c_int32'),
            'int64_t': c_types.CIntType('c_int64'),
            'size_t': c_types.CIntType('c_size_t'),
            'int': c_types.CIntType('c_int'),
            'bool': c_types.CBooleanType('c_bool'),
            'unsigned int': c_types.CIntType('c_uint'),
            'unsigned long': c_types.CIntType('c_ulong'),
            'unsigned long int': c_types.CIntType('c_ulong'),
            'unsigned short': c_types.CIntType('c_ushort'),
            'unsigned short int': c_types.CIntType('c_ushort'),
            'unsigned char': c_types.CIntType('c_ubyte'),
            'unsigned long long': c_types.CIntType('c_ulonglong'),
            'unsigned long long int': c_types.CIntType('c_ulonglong'),
            'long': c_types.CIntType('c_long'),
            'long int': c_types.CIntType('c_long'),
            'short': c_types.CIntType('c_short'),
            'short int': c_types.CIntType('c_short'),
            'long long': c_types.CIntType('c_longlong'),
            'long long int': c_types.CIntType('c_longlong'),
            'VisualID': c_types.CIntType('c_uint32'),  # X11/Xlib.h: CARD32
            'Window': c_types.CIntType('c_uint32'),  # X11/Xlib.h: CARD32 => XID
            'RROutput': c_types.CIntType('c_uint32'),  # X11/extensions/Xrandr.h
            'xcb_window_t': c_types.CIntType('c_uint32'),  # xcb/xcb.h
            'xcb_visualid_t': c_types.CIntType('c_uint32'), # xcb/xcb.h
            'HINSTANCE': c_types.CPointerType(type=None, input=True),  # windows.h
            'HWND': c_types.CPointerType(type=None, input=True),  # windows.h
            'HMONITOR': c_types.CPointerType(type=None, input=True),  # windows.h
            'HANDLE': c_types.CPointerType(type=None, input=True),  # windows.h
            'DWORD': c_types.CIntType('c_uint32'),  # windows.h
            'LPCSTR': c_types.CStringPointerType(char_type=c_types.CIntType('c_char'), input=True),  # windows.h
            'LPCTSTR': c_types.CStringPointerType(char_type=c_types.CIntType('c_char'), input=True),  # windows.h
            'LPCWSTR': c_types.CStringPointerType(char_type=c_types.CIntType('c_uint16'), encoding='utf-16', input=True),  # windows.h
            'zx_handle_t': c_types.CIntType('c_uint32'),  # zircon/types.h (Fuschia?)
            'GgpStreamDescriptor': c_types.CIntType('c_uint32'),  # Google games platform?
            'GgpFrameToken': c_types.CIntType('c_uint32'),  # Google games platform?
            'NvSciSyncAttrList': c_types.CPointerType(type=None, input=True), # NV Sci Platform
            'NvSciSyncObj': c_types.CPointerType(type=None, input=True), # NV Sci Platform
            'NvSciSyncFence': c_types.CArrayType(element_type=c_types.CIntType('c_uint64'), length=6), # NV Sci Platform
            'NvSciBufAttrList': c_types.CPointerType(type=None, input=True), # NV Sci Platform
            'NvSciBufObj': c_types.CPointerType(type=None, input=True), # NV Sci Platform
        }
        cparser = CParser()
        cparser.c_types.update(native_types.keys())
        cparser.c_types.update(platform_types.keys())
        for name in metadata.labels['basetype']:
            for node in metadata.nodes[name]:
                if len(node.children) > 0:
                    c_code = node.get_text_before(node.get('name')).split('\n')[-1] + name + node.get_text_after(node.get('name')).split('\n')[0]
                    if c_code.split()[0] in ['typedef', 'struct']:
                        c_ast = cparser.parse(c_code)
                        if c_ast.ext[0].__class__ == pycparser.c_ast.Decl and c_ast.ext[0].type.__class__ == pycparser.c_ast.Struct:
                            # A struct declaration defines opaque struct type defined in another library, a.k.a. external type
                            # external types cannot be used directly anywhere, but pointer to an external type is considered valid
                            # and it should be declared result in ctypes.c_void_p.
                            assert name not in metadata.ctypes
                            metadata.ctypes[name] = { 'class': 'external', 'name': name }
                        elif c_ast.ext[0].__class__ == pycparser.c_ast.Typedef:
                            c_type = get_type_dict_from_ast(c_ast.ext[0].type)
                            assert name not in metadata.ctypes
                            metadata.ctypes[name] = c_type
                            # typedef struct <some external name>* <used by vulkan name>
                            # is okay, as any unknown name should be considered external name, but
                            # referring to any non-declared external name should never be done by vulkan API
                            # For example:
                            # typedef __IOSurface* IOSurfaceRef;
                            # should allow using IOSurfaceRef in types, but it should not allow __IOSurface
                            # however, when determining the ctype for IOSurfaceRef, because __IOSurface is "class": "type",
                            # not in metadata.ctypes, it should be considered an external opaque type (struct),
                            # which we cannot determined the corresponding ctype, but we can determine the pointer to that type being ctypes.c_void_p.
                        else:
                            raise NotImplementedError(f'Unexpected node c_ast.{c_ast.ext[0].type.__class__.__name__}')
        for name in metadata.labels['enum']:
            assert name not in metadata.ctypes
            metadata.ctypes[name] = { 'class': 'ctypes', 'name': 'c_int' }
        for name in metadata.labels['bitmask']:
            for node in metadata.nodes[name]:
                if node.node_name == 'type' and node.get('type') is not None:
                    bitmask_type = node.get('type').get_text()
                    assert name not in metadata.ctypes
                    metadata.ctypes[name] = { 'class': 'type', 'name': bitmask_type }
        # The following two category of types are just placeholders, the actual type
        # will be generated subclass of ctypes.Structure/ctypes.Union which should be initialized
        # with specified _fields_.
        metadata.ctypes.update({ k: { 'class': 'vulkan.struct', 'name': k } for k in metadata.labels['struct'] })
        metadata.ctypes.update({ k: { 'class': 'vulkan.union', 'name': k } for k in metadata.labels['union'] })
        # The following set handle placeholders. The actual handle types would be:
        # ctypes.c_void_p if dispatchable
        # ctypes.c_void_p if not dispatchable, but ctypes.sizeof(ctypes.c_void_p) is 8
        # ctypes.c_uint64 if not dispatchable and not on 64-bit system
        for name in metadata.labels['handle']:
            for node in metadata.nodes[name]:
                if node.node_name == 'type' and node.get_attribute('category') == 'handle' and node.get('name') is not None and node.get('name').get_text() == name and node.get('type') is not None and node.get('type').get_text() in ['VK_DEFINE_HANDLE', 'VK_DEFINE_NON_DISPATCHABLE_HANDLE']:
                    dispatchable = node.get('type').get_text() == 'VK_DEFINE_HANDLE'
                    assert name not in metadata.ctypes
                    metadata.ctypes[name] = {
                        'class': 'vulkan.handle',
                        'dispatchable': dispatchable,
                        'parent': node.get_attribute('parent'),
                        'value': node.get_attribute('objtypeenum')
                    }
        metadata.c_types.update({ k: { 'class': 'type', 'name': n.get_attribute('alias') } for k in metadata.labels['alias'] for n in metadata.nodes[k] if n.has_attribute('alias') and n.get_attribute('alias') in metadata.ctypes })
        # At this point all types should be known, this include:
        # * Native C types used in the XML, mapped to ctypes;
        # * Platform specific C types that maps to specific ctypes;
        # * Platform specific opaque C types and structs that cannot be used directly, but pointers maps to c_void_p;
        # * Vulkan specific basetypes, usually a typedef to external or known C type;
        # * All Vulkan enumeration and bitmaps mapping to the corresponding integer type;
        # * All Vulkan complex type placeholders for the generated subclass of ctypes.Structure/ctypes.Union
        # * All Vulkan handles type placeholders for mapping to approriate ctypes type;
        # NOTE: In the above mapping, types with 'class': 'array' may have length specified by a constant.
        # Such length must be resolved after resolving enum and values maps.
        cparser.c_types.update(metadata.ctypes.keys())
        cparser.c_types.update({ k: { 'class': 'type', 'name': v } for k, v in metadata.bit_enum_map.items() })

        # All parsed data must be stored as dict(), so no C parsing occurs at runtime.
        # Enum, Bitmask, Non-enum values, macro values should be computed here and directly used at runtime.
        # Potentially also compute functional macros to python functions to be used at runtime.
        
        # Complex types can be computed to dictionaries here and stored as data for processing at runtime.
        # Complex types should be generated as follows:
        # 1. First Generate the empty class: `class <NAME>(ctypes.Structure): pass`
        # 2. Include any classes that are required by this class:
        # 2.1. Ignore if the same class
        # 2.2. Examine all <member>/<type> nodes for types that are in labels['struct'] or labels['union']
        # 2.3. Add appropriate relative imports for the classes
        # 3. Once everything is included generate _fields_ which should resolve ctypes: include ctypes of enum/bitmask, handles, etc.
        #   - enum/bitmask should be ctypes.c_int, unless bitmask is overridden by another ctype
        #   - handles should be ctype selected as shown in the "handle" description above;
        #   - pointer to external or unknown types (not in metadata.ctypes) should be c_void_p for the inner-most pointer (and ctypes.POINTER(...) for any subsequent pointers)
        #   - any complex types should already be included in the relative import in step 2, and used directly.
        # 4. Additional _vulkan_ should contain:
        #   - sync key containing a set of members that should be externally synchronized (must be handles)
        #   - fields: OrderedDict(can be initialized as list of 2-element tuples) - per field information
        #       - ctype: the same ctype as the _fields_. Used as somehow ctypes fails to provide access to the field type.
        #       - type: the class of the type that ctype refers to, None otherwise. If ctype is ctypes.POINTER(<vulkan subclass of ctypes.Structure>) this will be <vulkan subclass of ctypes.Structure>,
        # providing direct access to the referred type without unwrapping the ctype.
        #       - output: bool/None - whether it is an output member/parameter:

        # Any function signature and complex type member fields are considered input by default, unless chained to be an output, where:
        # Any P.O.D. type will be input only as functions receives a copy of the value in a register so it is not modified for the caller.
        # Any P.O.D. in a structure is be None output, indicating it inherits the output parameter from the calling function.
        # Any pointer type in a structure or function without const keyword will be considered an output, regardless of inherited output.
        # Any const pointer type will be considered non-output regardless of the inherited output.

        # For example:
        # struct Test {
        #     int data;
        # }
        # Will make `data` member output: None. That is a function defined as:
        # void mutable(Test *foo);
        # will have `data` as output = True;
        # where:
        # void immutable(Test foo);
        # and
        # void immutable(const Test *foo);
        # will have `data` as output = False;

        # Identifying output parameters is really important, as at runtime those data will be used to:
        # 1. Identify output handles for each command, thus determine

        # The goal of this script is NOT to be run AT INSTALLATION TIME,
        # instead it should be MANUALLY RUN at pre-deploy time and generated sources should be included
        # as a version.

        generator = Generator(metadata)

        pass

def get_type_dict_from_ast(c_ast: pycparser.c_ast.Node):
    if c_ast.__class__ == pycparser.c_ast.PtrDecl:
        return { 'class': 'pointer', 'quals': list(c_ast.quals), 'type': get_type_dict_from_ast(c_ast.type) }
    if c_ast.__class__ == pycparser.c_ast.ArrayDecl:
        length = None
        if c_ast.dim.__class__ == 'Constant':
            # length is specified directly by constant:
            length = { 'type': c_ast.dim.type, 'value': c_ast.dim.value }
        elif c_ast.dim.__class__ == pycparser.c_ast.ID:
            # length is specified indirectly, propbably by constant or preprocessor value.
            # Should be able to resolve later, once all values have been processed.
            length = { 'type': 'identifier', 'value': c_ast.dim.name }
        else:
            raise NotImplementedError('Expected c_ast.ID or c_ast.Constant for c_ast.ArrayDecl')
        return { 'class': 'array', 'length': length, 'type': get_type_dict_from_ast(c_ast.type) }
    if c_ast.__class__ == pycparser.c_ast.TypeDecl:
        if c_ast.type.__class__ == pycparser.c_ast.IdentifierType:
            return { 'class': 'type', 'quals': list(c_ast.quals), 'name': ' '.join(c_ast.type.names) }
        if c_ast.type.__class__ in [pycparser.c_ast.Struct, pycparser.c_ast.Union]:
            return { 'class': 'type', 'quals': list(c_ast.quals), 'name': c_ast.type.name }
        raise NotImplementedError('Expected c_ast.TypeDecl to contain one of [c_ast.IdentifierType, c_ast.Struct, c_ast.Union]')
    raise NotImplementedError(f'Unexpected node c_ast.{c_ast.__class__.__name__}')

class Generator:
    def __init__(self, metadata):
        self.metadata = metadata
    
    def resolve_alias(self, name):
        if name in self.metadata['alias']:
            for node in self.metadata.nodes[name]:
                if node.has_attribute('alias'):
                    return self.resolve_alias(node.get_attribute('alias'))
        return name

    def generate_enum(self, name, base_class):
        name = self.resolve_alias(name)
        if name in self.metadata.enum_bit_map:
            name = self.resolve_alias

# Do not use function here, combine everything into a single class containing:
# alias_map
# nodes
# labels
# etc.

