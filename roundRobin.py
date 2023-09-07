from fcfs import first_come_first_serve
from readyList import ReadyList
from pcb import PCB
from sjf import shortest_job_first

def round_robin(ready_queue, type):
    if len(ready_queue) == 0:
        return None
    if len(ready_queue) == 1:
        return ready_queue.get(0)
    furthest_runtime = ReadyList()
    furthest_runtime.append(ready_queue.get(0))
    for i in ready_queue[1:]:
        furthest_run = furthest_runtime.get(0).get_last_run()
        i_time = i.get_last_run()
        if i_time < furthest_run:
            furthest_runtime = ReadyList()
            furthest_runtime.append(i)
        elif i_time == furthest_run:
            furthest_runtime.append(i)
    if len(furthest_runtime) == 1:
        return furthest_runtime.get(0)
    match type:
        case "fcfs":
            return first_come_first_serve(furthest_runtime)
        case "sjf":
            return shortest_job_first(furthest_runtime, "pr")