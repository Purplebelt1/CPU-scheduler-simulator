from readyList import ReadyList

def first_come_first_serve(ready_queue):
    if len(ready_queue) == 0:
        return None

    # Sort the ready queue based on arrival time (earliest first)
    sorted_queue = sorted(ready_queue, key=lambda pcb: pcb.get_arrival_time())

    # Return the PCB that arrived first (first in the sorted queue)
    return sorted_queue[0]