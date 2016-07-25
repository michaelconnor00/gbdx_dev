from gbdxtools import Interface

gbdx = Interface()

geojson = """
{"type": "GeometryCollection", "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::4326"}}, "geometries": [{"type": "MultiPolygon", "coordinates": [[[[-105.20418905,40.00161644], [-105.20579077,39.99951061], [-105.20243658,39.99929828], [-105.20418905,40.00161644]], [[-105.22100219,39.99188934], [-105.22120192,39.99157745], [-105.22077586,39.99159722], [-105.22100219,39.99188934]]], []], "properties": {"name": "water", "color": [0,0,255]}}, {"type": "MultiPolygon", "coordinates": [[[[-105.21645204,39.98990144], [-105.21706805,39.98894798], [-105.21554790,39.98946003], [-105.21645204,39.98990144]]], []], "properties": {"name": "grass", "color": [0,255,0]}}, {"type": "MultiPolygon", "coordinates": [[[[-105.20932273,40.00311630], [-105.20942141,40.00299338], [-105.20909107,40.00295165], [-105.20900897,40.00309994], [-105.20932273,40.00311630]]], []], "properties": {"name": "roof", "color": [255,255,0]}}]}
"""

geojson_roi = gbdx.Task("Multiplex_GeoJSONToROI_MC")

# Multi geojson
geojson_roi.inputs.input_geojson1 = geojson
geojson_roi.inputs.input_geojson2 = geojson

# Multi Filenames
geojson_roi.inputs.output_roi_uri_filename1 = 'roi1.xml' # Required else the output file will be converted and error
geojson_roi.inputs.output_roi_uri_filename2 = 'roi2.xml' # Required else the output file will be converted and error

workflow = gbdx.Workflow([geojson_roi])
workflow.savedata(
    geojson_roi.outputs.output_roi_uri1,
    location='GeoJSONToROI/1'
)
workflow.savedata(
    geojson_roi.outputs.output_roi_uri2,
    location='GeoJSONToROI/2'
)
workflow.savedata(
    geojson_roi.outputs.task_meta_data1,
    location='GeoJSONToROI/1'
)
workflow.savedata(
    geojson_roi.outputs.task_meta_data2,
    location='GeoJSONToROI/2'
)

from utils import export_workflow
print export_workflow(workflow)

print workflow.execute()
