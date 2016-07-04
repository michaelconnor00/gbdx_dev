from gbdxtools import Interface

gbdx = Interface()

idltask = gbdx.Task("IDL_Task")

"""
Port for providing the IDL program (*.idl or *.pro).

Example:
    PRO MYPRO, input_location, output_location
        COMPILE_OPT IDL2
        e = ENVI(HEADLESS=1)

        Magic happens here...

        e.Close
"""
idltask.inputs.idl_program_data='s3://test-tdgplatform-com/data/idl_src/idl_scripts/isodata.pro'

# Input source (image files). Single input to the IDL program.
idltask.inputs.input_location='s3://test-tdgplatform-com/data/idl_src/005606990010_01_P011_MUL'

workflow = gbdx.Workflow([idltask])

# Output_location is the single output. Anything required to be output
# needs to be written here in the IDL program code.
workflow.savedata(
    idltask.outputs.output_location,
    location='idl_test'
)

print workflow.execute()
