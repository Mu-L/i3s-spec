import sys
import os
import glob
import json
import argparse
import re
import errno
import collections
import slpk_validator




def json_to_dom( path ) :
    with open( path, 'r') as f :
      return  json.load(f, object_pairs_hook=collections.OrderedDict)


class Schema_manifest :
    c_path_to_codes = { 'pointclouds' : 'pointcloud',  'meshes' : 'mesh', 'meshpyramids':'3dobject', 'points' : 'point', 'common' : 'common', "meshv2":"meshv2" ,"building":"building"}
    c_code_to_paths = { 'pointcloud'  : 'pointclouds', 'mesh' : 'meshes', '3dobject':'meshpyramids', 'point' : 'points', 'common' : 'common', "meshv2":"meshv2","building":"building"}
    c_code_to_versions = { '0106' : '1.6', '0107' : '1.7', '0200' : '2.0' }
    c_versions_to_code = { '1.6' : '0106', '1.7' : '0107', '2.0' : '0200' }

    """ Keep track of all the schemas to avoid parsing sub-schema multiple times"""
    def __init__(self, schema_reference_path, version) :
        self.ref_path = schema_reference_path
        self.types = {} # key: schema name, value : type object
        self.include_stack = []
        self.version = version

    def get_abs_path_from_schema_name( self, name ) :
        #if len(tok) > 1 :
        #    assert( tok[0] in Schema_manifest.c_code_to_paths)
        #fn = os.path.join( Schema_manifest.c_code_to_paths[tok[0]], "schema", fn ) 
        return os.path.realpath( os.path.join( self.ref_path, "schema", name ) );
     
    def get_relative_output_path_from_schema_name( self, name, abs_ref_path=None ) :
        tok = name.split('::')
        assert( len(tok) <= 2 )
        name = tok[-1].split('.')
        fn = name[0] + '.' + name[1] + '.md'
        version_num = Schema_manifest.c_code_to_versions[version]
        if len(tok) > 1 :
            assert( tok[0] in Schema_manifest.c_code_to_paths)
            fn = os.path.join( Schema_manifest.c_code_to_paths[tok[0]], "docs", version_num, fn ) 
        #if abs_ref_path != None :
        #    fn = os.path.relpath( os.path.join(self.ref_path, "docs", version_num, fn,), os.path.dirname( abs_ref_path) )
        return fn

    def get_output_path_from_schema_name( self, name ) :
        name = name.split('.')
        fn = name[0] + '.' + name[1] + '.md'
        #check if output directory exists
        dir = os.path.join( self.ref_path, "docs", Schema_manifest.c_code_to_versions[version] )
        if ( not os.path.isdir(dir) ) :
            try:
                os.mkdir(dir)
            except OSError:
                print("Could not create %s" % dir)
        return os.path.realpath( os.path.join(dir, fn ) )
       

    def read_href_resource( self, href) :
        assert( len( self.include_stack) > 0 )
        path = os.path.realpath(  os.path.join(self.include_stack[-1], '..', href) )
        with open(path, 'r') as f :
            return f.read()
        
    def get_schema_name_from_abs_path( self, abs_path ) :
        rel_path = os.path.relpath(abs_path,start=self.ref_path  );
        return Schema_manifest.get_schema_name_from_relative_path( rel_path );


    def get_schema_name_from_relative_path( rel_path, default_namespace="" ):
        #pointclouds/schema/pcsl_attributeInfo_schema.json
        tok = rel_path.replace('\\','/').split('/')
        if ( len(tok) > 1 ):
            name = tok[1]
        else:
            name = tok[0]
        if name.endswith('.json') :
            name = name[:-5]
        #if name.endswith('_schema') :
        #    name = name[:-7]
        #if len(tok) ==1 :
        #    assert( default_namespace in Schema_manifest.c_code_to_paths)
        #    tok.insert(0, Schema_manifest.c_code_to_paths[ default_namespace])
        #while( len(tok) > 0 and tok[0] == ".."):
        #    del tok[0]
        #assert( tok[0] in Schema_manifest.c_path_to_codes)
        #return "%s::%s" % (Schema_manifest.c_path_to_codes[tok[0]], name )
        return name

    def get_docs_href_from_schema_name( href) :
        return Schema_manifest._get_href_from_schema_name( href, 'docs')

    #def get_example_href_from_schema_name( abs_path_doc, href) :
    #    return Schema_manifest._get_href_from_schema_name( abs_path_doc, href, 'examples')

    def _get_href_from_schema_name( href, replace_by) :
        folders = []
        while 1:
            href, folder = os.path.split(href)
            if folder != "":
                folders.append(folder)
            else:
                if href != "":
                    folders.append(href)
                break

        folders.reverse()
        folders = [ (x if x !='schema' else replace_by ) for x in folders ]
        #folders[-1] = folders[-1].replace('_schema.json', '.md')
        folders[-1] = folders[-1].replace('.json', '.md')
        #if 'schema' in folders :
        #    folders = folders.replace( 'schema', 'docs')
        rel_path  = os.path.join(*folders )
        return rel_path;

    def add_dependency( self, child_href ) :
        #instanciate the type:
        assert( len(self.include_stack) > 0 )
        print( "reference:", child_href)
        abs_path =  os.path.realpath(  os.path.join( self.include_stack[-1], "..", child_href ) )
        if not os.path.exists( abs_path ) :
            raise BaseException( "Schema %s references %s but file %s doesnt exists. Please check href" %( self.include_stack, child_href, abs_path  ))
        #print("Dependency:",child_href)
        child_type = self.get_type_from_abs_path( abs_path)
        return child_type;

    def load_schema( self, abs_path ) :
        print("Loading schema file:",abs_path )
        sch = Schema_type( self )
        sch.parse_from_file(abs_path ) # os.path.join( self.ref_path, rel_path ) )
        #register it:
        assert( sch.name not in self.types )
        self.types[sch.name] = sch
        return sch;

    def get_type_from_abs_path( self, abs_path ) :
        # have it already ?
        name = self.get_schema_name_from_abs_path( abs_path )
        if name in self.types :
            return self.types[name]
        else :
            self.include_stack.append( abs_path )
            ret = self.load_schema( abs_path)
            self.include_stack.pop()
            return ret;

    def dom_to_schema(self) :
        dom = {}
        properties = {}
        is_required = []
        for key,value in self.types.items() :
            for prop in value.props :
                properties[prop.name] = {}
                if (prop.is_required) :
                    is_required.append(prop.name)
                if (prop.type.json_type == 'array') :
                    properties[prop.name]["type"] = "array"
                    properties[prop.name]['items'] = {}
                    properties[prop.name]['items']['type'] = prop.type.item_prop.type.json_type
                    if (prop.type.enum) :
                        properties[prop.name]['items']['enum'] =  prop.type.enum
                elif (prop.type.json_type == 'object') :
                    properties[prop.name]['type'] = 'object'
                    properties[prop.name]['$ref'] = prop.type.name + '.json'
                else:
                    properties[prop.name]['type'] = prop.type.json_type
                    if (prop.type.enum) :
                        properties[prop.name]["enum"] =  prop.type.enum
        dom['properties'] = properties
        dom['required'] = is_required
        dom['additionalProperties'] = False
        dom = json.dumps(dom)
        return dom


class Dummy_type :
    """used only for custom_related"""
    def __init__(self, manifest ):
        self.name = ""
        self.manifest = manifest

class Schema_type :
    def __init__(self, manifest) :
        # init data members:
        self.json_type ='' # array, number, object, string, ...
        self.name =''
        self.title=''
        self.desc=''
        self.props = [] # array of Property object.
        self.examples = []
        self.enum = {} # for "enum", {  enum_value : description of this value }
        #self.href='' #externaly defined object type
        self.item_prop = None #array only.
        self.manifest = manifest
        self.back_refs = [] #for navigation purposes
        self.range = ["",""]
        self.example_dom=[];
        self.desc_href=''
        self.custom_related = []
        self.oneOf = []
        self.include = ''
        self.properties = {}

    def parse_from_file(self, abs_path) :
        """ parse schema definition from json-schema file"""
        self.name = self.manifest.get_schema_name_from_abs_path( abs_path )
        #self.name = os.path.basename( schema_path ).replace( "_schema.json", "" )
        self.parse_from_dom( json_to_dom( abs_path ) )

    def parse_from_dom( self, dom, parent_type=None  ) :
        """ Parse a schema definition """
        if 'title' in dom :
            self.title = dom['title']
        self.parse_type( dom, parent_type )
        # todo: parse example & external md doc if any

    def parse_property( self, field, sub_dom, parent_type=None ) :
        prop = Property()
        prop.name = field
        if '$ref' in sub_dom :
            #tmp = Schema_manifest.get_schema_name_from_relative_path( sub_dom['$ref'], self.name.split('::')[0] );
            tmp = Schema_manifest.get_schema_name_from_relative_path( sub_dom['$ref'], "" if parent_type is None else parent_type.name.split('::')[0] );
            if tmp != self.name and ( parent_type is None or tmp != parent_type.name ):
                prop.href = sub_dom['$ref']
                if 'description' in sub_dom :
                    prop.prop_desc = sub_dom['description']
                prop.type =  self.manifest.add_dependency(  sub_dom['$ref'])
            else:
                prop.href = sub_dom['$ref']
                if 'description' in sub_dom :
                    prop.prop_desc = sub_dom['description']
                prop.type = self if tmp == self.name else parent_type

        else :
            prop.type = Schema_type( self.manifest)
            prop.type.parse_from_dom( sub_dom, self )
        return prop

    def get_properties(self, dom) :
        if '$include' in dom :
            self.include = dom['$include']
            abs_path_to_include = Schema_manifest.get_abs_path_from_schema_name(self.manifest, self.include)
            print("Including schema file: %s" % abs_path_to_include)
            old_schema = json_to_dom( abs_path_to_include )
            self.get_properties( old_schema )
        
        if ( 'properties' in dom ) :
            for entry in dom['properties'] :
                self.properties[entry] = dom['properties'][entry]
            #old_schema = self.parse_from_dom( json_to_dom( abs_path_to_include ) )
            #props = self.get_properties(old_schema)



    def parse_type(self, dom, parent_type=None ) :
        if 'type' in dom :
            self.json_type = dom['type']
        if 'related' in dom :
            if not isinstance( dom['related'], list) :
                dom['related'] = [dom['related']]
            for related in dom['related'] :
                obj = Dummy_type( self.manifest);
                obj.name = related
                self.custom_related.append( obj )
        #print("Parsing type '%s' of type %s" % (self.name, self.json_type ) )

        if '$include' in dom :
            include = dom['$include']

        if 'description' in dom :
            self.desc = dom['description']

        if 'items' in dom :
            assert( self.json_type == 'array')
            item_dom =  dom['items'] 
            self.item_prop = self.parse_property( 'items', item_dom, parent_type )
            if 'minItems' in dom :
                self.range[0] = str(dom['minItems'])
            if 'maxItems' in dom :
                self.range[1] = str(dom['maxItems'])

        if 'properties' in dom :
            self.get_properties(dom)

            #for field,sub_dom in dom['properties'].items() :
            for field,sub_dom in self.properties.items() :
                prop = self.parse_property( field, sub_dom, self )
                prop.is_required = True if 'required' in dom and field in dom['required'] else False
                if prop.type.json_type == 'array' :
                    prop.type.item_prop.type.back_refs.append( self)
                else :
                    prop.type.back_refs.append( self)
                self.props.append( prop )
        
        if self.json_type == 'string' and 'enum' in dom :
            for en in dom['enum'] :
                self.enum[en]=''
            if 'enum-description' in dom :
                for k, v in dom['enum-description'].items() :
                    assert( k in self.enum )
                    self.enum[k]= v
        if 'esriDocumentation' in dom and 'examples' in dom['esriDocumentation'] :
            self.example_dom  = dom['esriDocumentation']['examples']
        if 'description-href' in dom :
            self.desc ="%s\n\n%s" % (self.desc, self.manifest.read_href_resource( dom['description-href'] ) )

        if 'oneOf' in dom :
            for schema in dom['oneOf']:
                for field, sub_dom in schema.items():
                    prop = self.parse_property(field, schema)
                    prop.type.back_refs.append( self)
                    self.oneOf.append( {field: sub_dom} )


class Property :
    def __init__(self) :
        self.type = None;
        self.name=''
        self.prop_desc=''
        self.is_required=False
        self.out = None
        self.href = ''

    def get_desc( self ) :
       if self.href != '' and self.prop_desc != ''  :
            return self.prop_desc.replace('\n', " ")
       else :
            return self.type.desc.replace('\n', " ")
    
    def get_type_name(self, doc_path) :
        if self.href != '' :
            return Schema_manifest.get_docs_href_from_schema_name( self.href )
        else :
            return self.type.json_type


class Markdown_writer  :
    def __init__(self, output_path ):
        self.output_folder = output_path

    def write_line( self, line='' ) :
        if line != '' :
            self.out.write( line )
        self.out.write('\n') #on all platforms 

    def write_table_row(self, cols ) :
        self.write_line( "| %s |" % " | ".join( cols ) )

    def write_table_header(self, hd ) :
        self.write_table_row( hd )
        self.write_table_row( [ "---" for x in hd ] ) 


    #def get_filename(self, typename ) :
    #    return os.path.join( self.output_folder, "%s.md" % typename )

    def get_property_name( self, prop ) :
        return ("**%s**" % prop.name) if prop.is_required else prop.name


    def get_property_type( self, prop, postfix='') :
        if isinstance(prop.type.json_type,list) :
            return ", ".join( [ "%s%s" %( x , postfix ) for x in prop.type.json_type] )
        if prop.type.json_type == 'array' :
            range = ''    
            if prop.type.range[0] == prop.type.range[1] and prop.type.range[0] != '':
                range = prop.type.range[0] 
            if prop.type.range[0] != prop.type.range[1] :
                range = "%s:%s" % (prop.type.range[0], prop.type.range[1]) 
            postfix ='[%s]' % range
            return self.get_property_type( prop.type.item_prop, postfix)
        
        typename = prop.type.json_type
        if prop.type.json_type == 'object' :
            if prop.href != '' :
                #print a link to the type:
                tn = prop.get_type_name(self.output_path)
                obj = tn.split('.')
                link = obj[0]
                fn = obj[0] + '.' + obj[1] + ".md"
                typename = "[%s](%s)" % (link, "%s" % fn )
            else :
                typename = prop.type.name
        return "%s%s" % (typename, postfix )


    def get_property_type_old( self, prop ) :
        postfix = '';
        if prop.type.json_type == 'array' :
            range = ''    
            if prop.type.range[0] == prop.type.range[1] and prop.type.range[0] != '':
                range = prop.type.range[0] 
            if prop.type.range[0] != prop.type.range[1] :
                range = "%s:%s" % prop.type 
            postfix ='[%s]' % range
            prop = prop.type.item_prop
        
        typename = prop.type.json_type
        if prop.type.json_type == 'object' :
            if prop.href != '' :
                #print a link to the type:
                tn = prop.get_type_name(self.output_path)
                typename = "[%s](%s)" % (prop.type.name, "%s" % tn.replace('\\','/') )
            else :
                typename = prop.type.name

        return "%s%s" % (typename, postfix )

    def get_one_enum_md( key, val) :
        return ("`%s`" % key ) if val == ''  else ("`%s`: %s" % (key,val) )
 
    def get_unordered_list_http( enum ) :
        return "<ul><li>%s</li></ul>" % ( "</li><li>".join( [ Markdown_writer.get_one_enum_md( k,v ) for k,v in  enum.items() ] ) )

    def get_property_desc( self, prop ) :
        postfix = ''
        if len( prop.type.enum ) > 0 :
            if len( prop.type.enum ) ==1 :
                postfix = "<div>Must be:%s</div>" % Markdown_writer.get_unordered_list_http( prop.type.enum  )
            else :
                postfix = "<div>Possible values are:%s</div>" % Markdown_writer.get_unordered_list_http( prop.type.enum  )
        if prop.type.json_type == 'array' and len( prop.type.item_prop.type.enum ) > 0 :
            postfix = "<div>Possible values for each array string:%s</div>" % Markdown_writer.get_unordered_list_http( prop.type.item_prop.type.enum ) 
        return prop.get_desc() + postfix;
    
     
    def get_example_code( self, ex_dom ) :
        if 'code' in ex_dom :
           return json.dumps( ex_dom['code'], ensure_ascii=False, indent=2, separators=(',', ': '))
        if 'code_href' in ex_dom :
            #load from relative path:
            #path = os.path.realpath( os.path.join( self.output_folder, "..", ex_dom[ 'code_href' ]) )
            #rel_path = Schema_manifest.get_example_href_from_schema_name( self.output_path, ex_dom[ 'code_href' ] )
            abs_path = os.path.abspath(os.path.join(os.path.dirname( output_path), 'schema', ex_dom[ 'code_href' ]))
            #abs_path =  os.path.realpath( os.path.join(self.output_path, '..', ex_dom[ 'code_href' ])) 
            if not os.path.exists( abs_path ) :
                raise BaseException( "Example 'href=%s' is missing (file %s not found )" %(ex_dom[ 'code_href' ], abs_path)  )
            with open( abs_path, 'r') as f :
                return f.read()

    def write_to_md( self, manifest, schema_doc ):
        self.output_path  = manifest.get_output_path_from_schema_name( schema_doc.name )

        #output_path  = os.path.join( self.output_folder, "%s.md" % schema_doc.name)
        print( "Writing %s" % self.output_path )
        with open( self.output_path,'w') as output:
            self.out = output
            self.write_line( "# %s\n" % schema_doc.title )
            self.write_line( schema_doc.desc )
            self.write_line()
            #remove list duplicates:
            schema_doc.back_refs = list( set(schema_doc.back_refs + schema_doc.custom_related) )
            if len( schema_doc.back_refs ) > 0:
                # print the related documents (i.e. navigation parents)
                self.write_line( "### Related:\n" )
                self.write_line( ", ".join( [ "[%s](%s)" %( x.name.split('.')[1] +'::'+x.name.split('.')[0], manifest.get_relative_output_path_from_schema_name(x.name, self.output_path).replace('\\','/') ) for x in schema_doc.back_refs ] ) )
            
            # only print properties if any exist
            if ( len(schema_doc.props) ) :
                self.write_line( "### Properties\n" )
                self.write_table_header( ["Property", "Type", "Description" ]);
                # to property table:
                for prop in  schema_doc.props :
                    self.write_table_row( [ self.get_property_name( prop ), self.get_property_type(prop), self.get_property_desc(prop) ] );
                self.write_line()
                self.write_line( "*Note: properties in **bold** are required*" )
                self.write_line()

            # only print oneOf option if it exists
            if ( len(schema_doc.oneOf) ) :
                self.write_line( "### oneOf:\n" )
                for item in schema_doc.oneOf :
                    for key, value in item.items() :
                        namespace =  schema_doc.name.split('::')[0]
                        name = Schema_manifest.get_schema_name_from_relative_path( value, namespace )
                        link = manifest.get_relative_output_path_from_schema_name(name, self.output_path)
                        self.write_line("- [%s](%s)" % (name.split('.')[0], link))
                self.write_line()
                self.write_line()

            # Examples:
            if len( schema_doc.example_dom ) :
                self.write_line( "### Examples \n" )
                for ex in schema_doc.example_dom  :
                    self.write_line( "#### Example: %s \n" % (ex['title'] if 'title' in ex else '' ))
                    # validate example code if it exists in the current schema
                    if 'description' in ex :
                        self.write_line( "%s \n" % ex['description'] )
                    self.write_line( "```json\n %s \n```\n" % self.get_example_code( ex ))

def validate_examples(manifest) :
    ## validate examples before writing to schema
    successful_validation = True
    for profile in manifest.types:
        examples = manifest.types[profile].example_dom
        if ( len(examples) ) :
            schema = os.path.join(manifest.ref_path, 'schema', (profile + '.json') )
            for example in examples:
                successful_validation = True
                ex_code = Markdown_writer.get_example_code(example, example)
                if (ex_code and ex_code != "") :                                   
                    try:
                        successful_validation = slpk_validator.validate_json_string(schema, ex_code, profile)[0]    # first returned argument return success or failure
                        if (not successful_validation) :
                            raise BaseException(("Example in %s did not successfully validate against schema" % profile))
                    except BaseException as e:
                        print(e)
                        return False
    return True

def get_entry_points_from_dom( manifest_dom ) :
    entry_points = []
    for profile in manifest_dom['profile'] :
        for paths in profile['schemas'] :
            path, schema = paths.items()
            entry_points.append(schema[1])
    return entry_points


if __name__ == "__main__" :

    ## argument parsing: 
    parser = argparse.ArgumentParser(description='This program creates md files.',
                                    epilog='',
                                    add_help=True,
                                    argument_default=None, # Global argument default
                                    usage=__doc__)
    #parser.add_argument('-i', '--input', action='store', dest='json_schema_path', required=True, help='The path to the input JSON schema folder.')
    #parser.add_argument('-s', '--schemas', action='store', dest='schema_names', required=True, help='comma separated list of schemas to process')
    
    parser.add_argument('-p', '--profile', action='store', dest='profiles', default='pointclouds', nargs='+', help='List of input profile folder names  (e.g: -p pointclouds points)' )

    args = parser.parse_args();

    #schema_files = []

    #try:
    #    os.makedirs(arguments.md_output_path)

    #except OSError as e:
    #    if e.errno != errno.EEXIST:
    #        raise

    ##assumes relative path:
    #output_path = os.path.realpath(  os.path.join(os.path.dirname(__file__), arguments.md_output_path) )
    #input_path  = os.path.realpath(  os.path.join(os.path.dirname(__file__), arguments.json_schema_path) )
    #schema_names     = arguments.schema_names.split(',')

    #find 'root' path:
    print(args.profiles );
    root = os.path.realpath(__file__ + "../../../../") 
    print( "Profile root folder is:", root )
    assert( os.path.exists(root))

    search_folder = os.path.join(root, "schema")
    manifest_folder = os.path.join(root, "manifest")
    output_path = os.path.realpath(__file__ + "../../../../docs")

    manifest = {}   # {version : Schema_manifest}

    #for profile in args.profiles :
    #scan the manifest:
    for file in os.listdir( manifest_folder) :
        if file.endswith(".json"):
            version = file.split('.')[1]
            if (Schema_manifest.c_code_to_versions[version] in args.profiles ):
                manifest[version] = Schema_manifest(root, version);
                dom = json_to_dom( os.path.join(manifest_folder, file) )
                entry_points = get_entry_points_from_dom( dom)
                for entry_point in entry_points :
                    if ('.testing.' in entry_point) :
                        None
                    abs_path = os.path.join(search_folder, entry_point)
                    manifest[version].get_type_from_abs_path( abs_path )
    
    successful_validation = True

    ##validate examples
    print("\nNow validating examples")
    for version in manifest:
        if (not validate_examples(manifest[version]) ) :
            successful_validation = False
    print()


    #write all profiles:
    if (successful_validation) :
        for version in manifest :
            writer = Markdown_writer( output_path );
            for name, obj  in manifest[version].types.items() :
                writer.write_to_md( manifest[version], obj )
    else:
        print("\nFix errors before docs can be generated")
