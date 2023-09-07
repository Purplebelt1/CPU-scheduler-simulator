import xml.etree.ElementTree as ET
import csv
from pcb import PCB
from readyList import ReadyList
from fcfs import first_come_first_serve

def main():

    # Parse the XML config file
    tree = ET.parse('./input/conf.xml')
    root = tree.getroot()

    # Find and extract the values of algorithm and trace_file_path elements
    algorithm = root.find('algorithm').text
    trace_file_path = root.find('trace_file_path').text


    # Check if algorithm name is valid
    match algorithm:
        case "fcfs":
            pass
        case _:
            ValueError("Algorithm [" + algorithm + "] is not supported.")

    traces = ReadyList()
    with open(trace_file_path, "r") as traces_file:
        next(traces_file)
        traces_csv = csv.reader(traces_file, delimiter=",")
        for row in traces_csv:
            traces.append(PCB(*row))

    print("Algorithm:", algorithm)
    print("Trace File Path:", trace_file_path)
    for i in traces:
        print(i)


    write_output_file_header('./output/waittime.csv', ["Process ID", "Wait Time"])

    burst_time = 0
    ready_queue = ReadyList()
    while len(traces) > 0:
        for i in traces:
            if i.get_arrival_time() == burst_time:
                ready_queue.append(i)
        running_process = ready_queue.get_running_pcb()

        # Delete process if it is finished
        if running_process != None:
            if running_process.get_CPU_burst() == 0:
                del_p_id = running_process.get_process_id()
                write_to_output_file('./output/waittime.csv', [del_p_id, running_process.get_wait_time()])
                traces.pop(traces.find_index_by_process_id(del_p_id))
                ready_queue.pop(ready_queue.find_index_by_process_id(del_p_id))

                if len(traces) == 0:
                    break


        match algorithm:
            case "fcfs":
                new_running_process = first_come_first_serve(ready_queue)
        

        if running_process != None:
            running_process.set_is_running(False)
        if new_running_process != None:
            new_running_process.set_is_running(True)
            new_running_process.set_CPU_burst(new_running_process.get_CPU_burst()-1)
            new_running_process.set_last_run(burst_time)

        ready_queue.increment_process_waiting(1)
        running_process = new_running_process



        burst_time += 1
    print("FINISHED")

def write_output_file_header(path, headers):
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

def write_to_output_file(path, vars):
    with open(path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(vars)

if __name__ == "__main__":
    main()