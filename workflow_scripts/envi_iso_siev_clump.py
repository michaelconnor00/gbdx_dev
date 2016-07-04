from gbdxtools import Interface

gbdx = Interface()

isodata = gbdx.Task("ENVI_ISODATAClassification")
isodata.inputs.input_raster = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Denver/aop/055026839010_01"
isodata.inputs.file_types = "tif"

sieve = gbdx.Task("ENVI_ClassificationSieving")
sieve.inputs.input_raster = isodata.outputs.output_raster_uri.value
sieve.inputs.file_types = "hdr"

clump = gbdx.Task("ENVI_ClassificationClumping")
clump.inputs.input_raster = sieve.outputs.output_raster_uri.value
clump.inputs.file_types = "hdr"

workflow = gbdx.Workflow([isodata, sieve, clump])

workflow.savedata(
    isodata.outputs.output_raster_uri,
    location="sieve_clump_test1/isodata"
)

workflow.savedata(
    sieve.outputs.output_raster_uri,
    location="sieve_clump_test1/sieve"
)

workflow.savedata(
    clump.outputs.output_raster_uri,
    location="sieve_clump_test1/clump"
)

print workflow.execute()
