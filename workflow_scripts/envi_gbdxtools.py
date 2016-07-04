from gbdxtools import Interface
gbdx = Interface()


# launch workflow ENVI -> S3
envitask = gbdx.Task("ENVI_RXAnomalyDetection")
envitask.inputs.task_name='RXAnomalyDetection'
envitask.inputs.file_types='til'
envitask.inputs.kernel_size='3'
data = "s3://receiving-dgcs-tdgplatform-com/054813633050_01_003/054813633050_01/054813633050_01_P001_MUL/"
envitask.inputs.input_raster=data

workflow = gbdx.Workflow([ envitask ] )
workflow.savedata(envitask.outputs.task_meta_data, location='envi_task_output')
workflow.savedata(envitask.outputs.output_raster_uri, location='envi_task_output')

print workflow.execute()
