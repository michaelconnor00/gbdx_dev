import json

def export_workflow(gbdx_workflow):
    """
    Takes an Interface object from gbdxtools
    and builds the workflow json
    """
    temp_wf = {"name": gbdx_workflow.name, "tasks": []}

    for task in gbdx_workflow.tasks:
        temp_wf['tasks'].append(task.generate_task_workflow_json())

    return json.dumps(temp_wf, sort_keys=True, indent=4, separators=(',', ': '))
