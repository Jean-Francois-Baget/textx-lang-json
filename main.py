from textx import metamodel_for_language


parser = metamodel_for_language('textxjson')


#from textx.export import metamodel_export
#
#metamodel_export(parser, 'json.dot')

some_json = r'''
{
    "name" : "textx-lang-json",
    "authors" : [
        "Jean-François Baget"
    ],
    "year" : 2024,
    "tested" : true
}
'''

model = parser.model_from_str(some_json)

from textx.export import model_export

model_export(model, 'model.dot')

