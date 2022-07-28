def run(tasks):
    parallel= 0
    groups=[]
    works=[]
    for t in tasks:
        parallel+=t["parallelization"]
        if (parallel<=1):
            works.append(t["duration"])
        else:
            groups.append(works)
            works=[t["duration"]]
    groups.append(works)
    return sum((max(g) for g in groups))
