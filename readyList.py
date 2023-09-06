from pcb import PCB

class ReadyList:
    def __init__(self):
        # Initialize an empty list to store PCB instances
        self.process_list = []

    def insert(self, index, pcb):
        # Insert a PCB instance at the specified index
        if isinstance(pcb, PCB):
            self.process_list.insert(index, pcb)
        else:
            # Raise a ValueError if the input is not a PCB instance
            raise ValueError("Error: Only PCB instances can be inserted.")

    def append(self, pcb):
        # Append a PCB instance to the end of the list
        if isinstance(pcb, PCB):
            self.process_list.append(pcb)
        else:
            # Raise a ValueError if the input is not a PCB instance
            raise ValueError("Error: Only PCB instances can be appended.")

    def pop(self, index=-1):
        # Remove and return an element at the specified index (default is the last element)
        if index < 0:
            index += len(self.process_list)

        if 0 <= index < len(self.process_list):
            return self.process_list.pop(index)
        else:
            # Raise an IndexError if the index is out of range
            raise IndexError("Error: Index out of range.")

    def get(self, index):
        # Get an element at the specified index
        if 0 <= index < len(self.process_list):
            return self.process_list[index]
        else:
            # Raise an IndexError if the index is out of range
            raise IndexError("Error: Index out of range.")

    def set(self, index, pcb):
        # Set an element at the specified index to a PCB instance
        if index < 0:
            index += len(self.process_list)

        if 0 <= index < len(self.process_list):
            if isinstance(pcb, PCB):
                self.process_list[index] = pcb
            else:
                # Raise a ValueError if the input is not a PCB instance
                raise ValueError("Error: Input must be a PCB instance.")
        else:
            # Raise an IndexError if the index is out of range
            raise IndexError("Error: Index out of range.")

    def set_full_list(self, pcb_list):
        # Set the entire list to the input list of PCB instances
        if isinstance(pcb_list, list) and all(isinstance(pcb, PCB) for pcb in pcb_list):
            self.process_list = pcb_list
        else:
            # Raise a ValueError if the input is not a list of PCB instances
            raise ValueError("Error: Input must be a list of PCB instances.")

    def get_full_list(self):
        # Get the entire list of PCB instances
        return self.process_list

    def is_empty(self):
        # Check if the list is empty
        return len(self.process_list) == 0




