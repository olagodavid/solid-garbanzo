# todo.py
""" All parameters are explicit. For update_task, for example, I have three arguments, instead of a single dictionary with three keys.
In add_task, I anticipate that sometimes I will want to create a task with just a summary field - “get milk” doesn’t really need elaboration, for example - so give description a sensible default."""

def get_tasks():
    pass
def describe_task(task_id):
    pass
def add_task(summary, description=""):
    pass
def task_done(task_id):
    pass
def update_task(task_id, summary, description):
    pass
