PRO ISODATA, input_location, output_location
    COMPILE_OPT IDL2

    e = ENVI(HEADLESS=1)

    files = File_Search(input_location, '*.TIF', /FULLY_QUALIFY_PATH)

    raster = e.OpenRaster(files[0])

    ; Docs: https://www.harrisgeospatial.com/docs/enviisodataclassificationtask.html
    task = ENVITask("ISODATAClassification")

    task.Input_Raster = raster

    task.Execute

    out_filename = output_location + 'isodata_output.tif'

    ; Export output as tif
    e.ExportRaster, task.Output_Raster, out_filename, "TIFF"

    e.Close
END
