from gbdxtools import Interface
gbdx = Interface()

ndvi = gbdx.Task('ENVI_SpectralIndex', file_types="TIF,tif", index="Normalized Difference Vegetation Index")
ndvi.inputs.task_name = 'SpectralIndex'
ndvi.inputs.input_raster = 's3://receiving-dgcs-tdgplatform-com/055273824010_01_003/055273824010_01/055273824010_01_P001_MUL/'

classify = gbdx.Task('ENVI_ColorSliceClassification', file_types='hdr')
classify.inputs.task_name = 'ColorSliceClassification'
classify.inputs.input_raster = ndvi.outputs.output_raster_uri.value
classify.inputs.class_ranges = '[0.65, 1.01]'
classify.inputs.class_colors = '[255, 0, 0]'

vector = gbdx.Task('ENVI_ClassificationToShapefile', input_raster=classify.outputs.output_raster_uri.value, file_types='hdr')
vector.inputs.task_name = 'ClassificationToShapefile'

w = gbdx.Workflow([ndvi, classify, vector])
w.savedata(ndvi.outputs.output_raster_uri, location='envi_classtoshape/ndvi')
w.savedata(classify.outputs.output_raster_uri, location='envi_classtoshape/classified')
w.savedata(vector.outputs.output_vector_uri, location='envi_classtoshape/vector')

print w.execute()
