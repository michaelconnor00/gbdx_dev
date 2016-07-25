from gbdxtools import Interface

gbdx = Interface()

task = gbdx.Task(__task_type="ENVI_ImageThresholdToROI")
task.inputs.input_raster = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Denver/aop/055026839010_01/"
task.inputs.file_types = "tif"
task.inputs.roi_name = "[\"Water\", \"Land\"]"
task.inputs.roi_color = "[[0,255,0],[0,0,255]]"
task.inputs.threshold = "[[138,221,0],[222,306,0]]"
task.inputs.output_roi_uri_filename = "roi.xml" # Otherwise the file would be named 'outputfile'

workflow = gbdx.Workflow([task])

workflow.savedata(
    task.outputs.output_roi_uri,
    location='imgthresroi_test1'
)

print workflow.execute()
