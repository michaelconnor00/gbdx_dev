PRO CHGDET, input_location, output_location
    COMPILE_OPT IDL2

    e = ENVI(HEADLESS=1)
    Print, File_Search(input_location, '*')
    ;Assumed that there are only 2 files
    files = File_Search(input_location, '*.TIF', /FULLY_QUALIFY_PATH)
    Print, files
    file_list_size = N_ELEMENTS(files)

    FOR I=1, file_list_size DO BEGIN
        Raster = e.OpenRaster(files[I-1])

        ; From QGIS
        geoRect = [-122.93193, 53.80430, -122.69656, 53.84322]

        ; Get the task from the catalog of ENVITasks
        Task = ENVITask('GeographicSubsetRaster')

        ; Define inputs
        Task.INPUT_RASTER = Raster

        Task.SUB_RECT = geoRect

        ; Run the task
        Task.Execute

        out_put_path = output_location + STRTRIM(STRING(I), 1) + '_output.tif'

        e.ExportRaster, Task.OUTPUT_RASTER, out_put_path, "TIFF"
    ENDFOR

    output_image_dir = Filepath('', ROOT_DIR=output_location)
    files = File_Search(output_image_dir, '*.tif', /FULLY_QUALIFY_PATH)

    file_list_size = N_ELEMENTS(files)

    ; Get the task from the catalog of ENVITasks
    Diff_Task = ENVITask('ImageBandDifference')

    ; Define inputs
    Diff_Task.INPUT_RASTER1 = e.OpenRaster(files[0])
    Diff_Task.INPUT_RASTER2 = e.OpenRaster(files[1])

    ; Define outputs
    ; Diff_Task.OUTPUT_RASTER_URI = e.GetTemporaryFilename()

    ; Run the task
    Diff_Task.Execute

    ; Get the task from the catalog of ENVITasks
    AutoChangeThreshTask = ENVITask('AutoChangeThresholdClassification')

    ; Define inputs
    AutoChangeThreshTask.INPUT_RASTER = Diff_Task.OUTPUT_RASTER

    ; Run the task
    AutoChangeThreshTask.Execute

    out_put_path = output_location + 'cd_output.tif'

    e.ExportRaster, AutoChangeThreshTask.OUTPUT_RASTER, out_put_path, "TIFF"

    e.Close
END
