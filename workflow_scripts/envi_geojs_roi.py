"""
Workflow to run the ENVI_GeojsonToROI Task.

Name: ENVI_GeoJSONToROI

description: This task converts GeoJSON features to a region of interest (ROI).

inputPorts:
  name: file_types
      required: false
      type: string
      description: GBDX Option. Comma seperated list of permitted file type extensions. Use this to filter input files -- Value Type: STRING[*]
  name: output_roi_uri_filename
      required: false
      type: string
      description: Outputor OUTPUT_ROI. -- Value Type: ENVIURI
  name: input_geojson
      required: true
      type: string
      description: Specify an input GeoJSON object. -- Value Type: ENVIGEOJSON

outputPorts:
  name: task_meta_data
      required: false
      type: directory
      description: GBDX Option. Output location for task meta data such as execution log and output JSON
  name: output_roi_uri
      required: true
      type: directory
      description: Outputor OUTPUT_ROI. -- Value Type: ENVIURI

"""
import json
from gbdxtools import Interface


gbdx = Interface()

geojson = """
{"type": "GeometryCollection", "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::4326"}}, "geometries": [{"type": "MultiPolygon", "coordinates": [[[[-105.20418905,40.00161644], [-105.20579077,39.99951061], [-105.20243658,39.99929828], [-105.20418905,40.00161644]], [[-105.22100219,39.99188934], [-105.22120192,39.99157745], [-105.22077586,39.99159722], [-105.22100219,39.99188934]]], []], "properties": {"name": "water", "color": [0,0,255]}}, {"type": "MultiPolygon", "coordinates": [[[[-105.21645204,39.98990144], [-105.21706805,39.98894798], [-105.21554790,39.98946003], [-105.21645204,39.98990144]]], []], "properties": {"name": "grass", "color": [0,255,0]}}, {"type": "MultiPolygon", "coordinates": [[[[-105.20932273,40.00311630], [-105.20942141,40.00299338], [-105.20909107,40.00295165], [-105.20900897,40.00309994], [-105.20932273,40.00311630]]], []], "properties": {"name": "roof", "color": [255,255,0]}}]}
"""

geojson_roi = gbdx.Task("ENVI_GeoJSONToROI")
geojson_roi.inputs.input_geojson = geojson#json.dumps(geojson_roi)
geojson_roi.inputs.output_roi_uri_filename = 'roi.xml' # Required else the output file will be converted and error

workflow = gbdx.Workflow([geojson_roi])
workflow.savedata(
    geojson_roi.outputs.output_roi_uri,
    location='s3://test-tdgplatform-com/tempENVI/GeoJSONToROI/'
)
workflow.savedata(
    geojson_roi.outputs.task_meta_data,
    location='s3://test-tdgplatform-com/tempENVI/GeoJSONToROI/'
)

# from utils import export_workflow
# print export_workflow(workflow)

print workflow.execute()
