from gbdxtools import Interface
gbdx = Interface()

data = "s3://receiving-dgcs-tdgplatform-com/055026839010_01_003/055026839010_01/055026839010_01_P004_MUL/"

envitask = gbdx.Task("ENVI_GaussianStretchRaster")
envitask.inputs.task_name='GaussianStretchRaster'
envitask.inputs.file_types='til'
# envitask.inputs.min="[180.0, 210.0, 120.0, 90.0]"
# envitask.inputs.max="[800.0, 1300.0, 1055.0, 1100.0]"
envitask.inputs.min = "180.0"
envitask.inputs.max = "800.0"
envitask.inputs.input_raster = data

workflow = gbdx.Workflow([envitask])
workflow.savedata(envitask.outputs.output_raster_uri, location='ENVI/Denver/gaussian/til')

print workflow.execute()
