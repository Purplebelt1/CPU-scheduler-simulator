from fcfs import first_come_first_serve
from readyList import ReadyList
from pcb import PCB
from sjf import shortest_job_first

def round_robin(ready_queue, type):

    # If ready queue is empty then return that no program should run.
    if len(ready_queue) == 0:
        return None
    
    # If only one thing is in ready queue return that.
    if len(ready_queue) == 1:
        return ready_queue.get(0)
    
    # Create a PCB containing object and put the first PCB in input PCB container into it to use to compare for lowwest last run
    furthest_runtime = ReadyList()
    furthest_runtime.append(ready_queue.get(0))

    # Loop through all excpet first object of input PCB container
    for i in ready_queue[1:]:

        # Get last run of current lowwest last run and last run of loop PCB
        furthest_run = furthest_runtime.get(0).get_last_run()
        i_time = i.get_last_run()

        # If loop PCB has lowwer last run than current lowwest, reset PCB containing object for all lowwest last run PCB to just loop PCB
        if i_time < furthest_run:
            furthest_runtime = ReadyList()
            furthest_runtime.append(i)

        # If loop PCB has same last run as current lowwest, add loop PCB to lowwest last run PCB container
        elif i_time == furthest_run:
            furthest_runtime.append(i)

    # If PCB container for lowwest last run only has one PCB then return that as the to be run process
    if len(furthest_runtime) == 1:
        return furthest_runtime.get(0)
    
    # If not check what type of secondary priority for choosing to be run process is and run that.
    match type:
        case "fcfs":
            return first_come_first_serve(furthest_runtime)
        case "sjf":
            return shortest_job_first(furthest_runtime, "pr")