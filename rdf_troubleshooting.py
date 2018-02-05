import os, glob
import json
import rdflib
# import rdflib-jsonld
from rdflib import Graph, plugin
from rdflib.serializer import Serializer


input_dir = "/Users/njkhan/Projects/web_scraping/scrc_metadata_all"
output_dir = "/Users/njkhan/Projects/web_scraping/json_converted"

# Transform genre fields to {"@value": value} format
# [{@value:Architectural photographs},{@value: Photographs}]

contents = ''

for infile in glob.glob( os.path.join(input_dir, '*.*') ):
   
    with open(infile, "r") as f:
        contents = f.read()
        parsed_json = json.loads(contents)
        print infile
    
        if 'genre' in parsed_json:
            tmp = parsed_json['genre']
            parsed_json['genre'] = [{"@value": a} for a in parsed_json['genre']]
        # print json.dumps(parsed_json)
        
        # write as separate files
        filename = infile.split('/')[-1]
        filepath = output_dir + "/" + filename
        print filepath

        # f2 = open(filepath, "w")
        with open(filepath, "w") as f2:
            json.dump(parsed_json, f2)
    
    # # overwrite the same file
    # with open(infile, "w") as f:
    #     json.dump(parsed_json, f)

