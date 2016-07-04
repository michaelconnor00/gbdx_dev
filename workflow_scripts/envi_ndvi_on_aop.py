"""
Run NDVI on an AOP image
"""
from gbdxtools import Interface
gbdx = Interface()

envitask = gbdx.Task("ENVI_SpectralIndex")
envitask.inputs.task_name='SpectralIndex'
envitask.inputs.index='Normalized Difference Vegetation Index'
envitask.inputs.file_types='tif'
data = 's3://gbd-customer-data/a157fdce-bb1d-42b3-96a9-66942896a787/denver_aop'
envitask.inputs.input_raster=data
workflow = gbdx.Workflow([envitask])
workflow.savedata(envitask.outputs.output_raster_uri, location='aop_to_envi/output')
print workflow.execute()
