from gbdxtools import Interface
from utils import export_workflow

gbdx = Interface()

rx = gbdx.Task("ENVI_RXAnomalyDetection")
rx.inputs.input_raster = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Denver/aop/055026839010_01/"
rx.inputs.file_types = "tif"

per_thres = gbdx.Task("ENVI_PercentThresholdClassification")
per_thres.inputs.input_raster = rx.outputs.output_raster_uri.value
per_thres.inputs.file_types = "hdr"
per_thres.inputs.threshold_percent = "0.200000000"

workflow = gbdx.Workflow([rx, per_thres])

workflow.savedata(
    rx.outputs.output_raster_uri,
    location='perThres_test1/rx/raster'
)

workflow.savedata(
    per_thres.outputs.output_raster_uri,
    location='perThres_test2/per_thres'
)

print export_workflow(workflow)
