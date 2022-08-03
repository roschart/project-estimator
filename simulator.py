from operator import itemgetter


def run(tasks):
    task_without_id, tasks_with_id = validate(tasks)
    acc_parallel = 0
    groups = []
    works = []
    done = set()
    while (len(tasks) > 0):
        pending = []
        group_done=set()
        for t in tasks:
            if (can_be_executed(t, done,acc_parallel)):
                acc_parallel += t["parallelization"]
                works.append(t["duration"])
                if "id" in t:
                    group_done.add(t["id"])
            else:
                pending.append(t)
        groups.append(works)
        works = []
        done=group_done.union(done)
        acc_parallel = 0
        tasks = pending
    return sum((max(g) for g in groups))

def can_be_executed(task, done, acc_parallel):
    if "after" in task and not task["after"] in done:
       return False
    p = task["parallelization"]
    if (acc_parallel + p > 1):
        return False
    return True



def validate(tasks):
    tasks_with_id = dict()
    task_without_id = []
    for t in tasks:
        if "id" in t:
            id = t["id"]
            if id in tasks_with_id:
                raise Exception(f"Duplicate id '{id}'")

            tasks_with_id[id] = t
        else:
            task_without_id.append(t)
    return (task_without_id, tasks_with_id)
