from readyList import ReadyList

def first_come_first_serve(ready_queue):
    if len(ready_queue) == 0:
        return None
    running = ready_queue.get_running_pcb()
    if running != None:
        return running
    first_arrive = ready_queue.get(0)
    for i in ready_queue[1:]:
        if int(i.get_arrival_time()) > first_arrive.get_arrival_time():
            first_arrive = i
    return first_arrive