from gbdxtools import Interface
gbdx = Interface()
envitask = gbdx.Task("ENVI_QUAC")
envitask.inputs.task_name='QUAC'
envitask.inputs.file_types='tif'
# data = "s3://test-tdgplatform-com/data/Denver/055026839010_01/"
data = "s3://test-tdgplatform-com/data/idl_src/005606990010_01_P011_MUL"
envitask.inputs.input_raster=data
workflow = gbdx.Workflow([envitask])
workflow.savedata(envitask.outputs.output_raster_uri, location='s3://test-tdgplatform-com/tempENVI/NDVI/')
print workflow.execute()
