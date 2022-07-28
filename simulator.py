def run(tasks):
    parallel= 0
    groups=[]
    works=[]
    while (len(tasks)>0):
        pending=[]
        for t in tasks:
            p=t["parallelization"]
            if (parallel+p<=1):
                parallel+=p
                works.append(t["duration"])
            else:
                pending.append(t)
        groups.append(works)
        works=[]
        parallel=0
        tasks=pending
    return sum((max(g) for g in groups))
