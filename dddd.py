
t = int(input())

def get_remote_workers(employees, j_tasks, k_tasks):
    remote_workers = []
    for i, (team, tasks) in enumerate(employees):
        if all(task in j_tasks for task in tasks) and all(task not in k_tasks for task in tasks):
            remote_workers.append((i + 1, team))

    return remote_workers

for _ in range(t):

    i, j, k, l = map(int, input().split())
    j_tasks = input().split()
    k_tasks = input().split()
    employees = []
    for _ in range(l):
        team, m = map(int, input().split())
        tasks = input().split()
        employees.append((team, tasks))


    remote_workers = get_remote_workers(employees, j_tasks, k_tasks)
    

            
    if not remote_workers:
        print("-1")
    else:
        print(" ".join(str(w) for w in remote_workers))
