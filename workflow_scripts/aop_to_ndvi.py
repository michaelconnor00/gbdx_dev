"""
Run AOP task, Run AOP_ENVI_HDR to add hdr file,
then run ENVI NDVI.
"""
from gbdxtools import Interface
gbdx = Interface()

# launch workflow AOP -> ENVI -> S3
# data = "s3://receiving-dgcs-tdgplatform-com/054813633050_01_003"
data = "s3://insight-cloud-scratch/Wes/foliage-workflow/1a-source-image-seattle/055273824010_01_003"
aoptask = gbdx.Task(
    "AOP_Strip_Processor",
    data=data,
    bands='MS',
    enable_acomp=True,
    enable_pansharpen=False,
    enable_dra=False
)

aop2envi = gbdx.Task("AOP_ENVI_HDR")
aop2envi.inputs.image = aoptask.outputs.data.value

envi_ndvi = gbdx.Task("ENVI_SpectralIndex")
envi_ndvi.inputs.input_raster = aop2envi.outputs.output_data.value
envi_ndvi.inputs.file_types = "hdr"
envi_ndvi.inputs.index = "Normalized Difference Vegetation Index"

workflow = gbdx.Workflow([ aoptask, aop2envi, envi_ndvi ] )
workflow.savedata(aoptask.outputs.data, location='aopseattle')
workflow.savedata(aop2envi.outputs.output_data, location='aopseattle_hdr')
workflow.savedata(envi_ndvi.outputs.output_raster_uri, location='aopseattle_ndvi')

print workflow.execute()
