import xml.etree.ElementTree as ET
import csv
from pcb import PCB

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

    traces = []
    with open(trace_file_path, "r") as traces_file:
        next(traces_file)
        traces_csv = csv.reader(traces_file, delimiter=",")
        for row in traces_csv:
            traces.append(PCB(*row))

    print("Algorithm:", algorithm)
    print("Trace File Path:", trace_file_path)
    for i in traces:
        print(i)




if __name__ == "__main__":
    main()