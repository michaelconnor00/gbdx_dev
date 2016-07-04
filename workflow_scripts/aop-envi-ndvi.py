"""
Run AOP_ENVI_HDR on an AOP image to add a header file, then
run NDVI on the output of that task.
"""
from gbdxtools import Interface

gbdx = Interface()

aop2envi = gbdx.Task("AOP_ENVI_HDR")
aop2envi.inputs.image = 's3://gbd-customer-data/a157fdce-bb1d-42b3-96a9-66942896a787/denver_aop'

envi_ndvi = gbdx.Task("ENVI_SpectralIndex")
envi_ndvi.inputs.input_raster = aop2envi.outputs.output_data.value
envi_ndvi.inputs.file_types = "hdr"
envi_ndvi.inputs.index = "Normalized Difference Vegetation Index"

workflow = gbdx.Workflow([aop2envi, envi_ndvi])


workflow.savedata(
    aop2envi.outputs.output_data,
    location='aop2envi_test1/output_data'
)
workflow.savedata(
    envi_ndvi.outputs.output_raster_uri,
    location='aop2envi_test1/output_raster_uri'
)

print workflow.execute()
