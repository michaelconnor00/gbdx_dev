from gbdxtools import Interface
gbdx = Interface()

# launch workflow AOP -> ENVI -> S3
data = "s3://receiving-dgcs-tdgplatform-com/054813633050_01_003"
aoptask = gbdx.Task("AOP_Strip_Processor", data=data, enable_acomp=True, enable_pansharpen=True)

envitask = gbdx.Task("ENVI_RXAnomalyDetection")
envitask.inputs.task_name='RXAnomalyDetection'
envitask.inputs.kernel_size='3'
envitask.inputs.input_raster = aoptask.outputs.data.value

workflow = gbdx.Workflow([ envitask, aoptask ] )
workflow.savedata(envitask.outputs.task_meta_data, location='envi_task_output')

print workflow.execute()
