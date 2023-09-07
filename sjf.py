from readyList import ReadyList

def shortest_job_first(ready_queue, type):
    if len(ready_queue) == 0:
        return None
    if type == "co":
        if ready_queue.get_running_pcb() != None:
            return ready_queue.get_running_pcb()
    # Sort the ready queue based on CPU burst time (shortest first)
    sorted_queue = sorted(ready_queue, key=lambda pcb: pcb.get_CPU_burst())

    # Return the PCB with the shortest burst time (first in the sorted queue)
    return sorted_queue[0]