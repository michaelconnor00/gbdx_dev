"""
Workflow to run the ENVI_GeojsonToROI Task.

Name: ENVI_RasterMetadataItem

description: This task retrieves the value of a given raster metadata key.

inputPorts:
  name: file_types
    required: false
    type: string
    description: GBDX Option. Comma seperated list of permitted file type extensions. Use this to filter input files -- Value Type: STRING[*]
  name: input_raster
    required: true
    type: directory
    description: Specify an raster to retrieve a metadata item from. -- Value Type: ENVIRASTER
  name: key
    required: true
    type: string
    description: Specify the string key of the metadata to retrieve. -- Value Type: STRING.

outputPorts:
  name: task_meta_data
    required: false
    type: directory
    description: GBDX Requirement. Output location for task meta data such as execution log and output JSON
  name: value
    required: true
    type: string
    description: The value of the specified metadata key. -- Value Type: VARIANT

"""

from gbdxtools import Interface

gbdx = Interface()

ras_meta = gbdx.Task("ENVI_RasterMetadataItem")

ras_meta.inputs.input_raster = 's3://gbd-customer-data/a157fdce-bb1d-42b3-96a9-66942896a787/aopseattle_hdr/'
ras_meta.inputs.file_types = 'tif'
ras_meta.inputs.key = 'wavelength'

workflow = gbdx.Workflow([ras_meta])

# NOTE: the output port `value` is essentially a STRING, thus can be found in the output
#  file `task_output.json` or look at the stdout for the task.
workflow.savedata(
    ras_meta.outputs.task_meta_data,
    location='RasterMetaData/'
)

# from utils import export_workflow
# print export_workflow(workflow)

print workflow.execute()
