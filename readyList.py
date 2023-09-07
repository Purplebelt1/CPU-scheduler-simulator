from pcb import PCB

class ReadyList:
    def __init__(self):
        # Initialize an empty list to store PCB instances
        self.__process_list = []

    def insert(self, index, pcb):
        # Insert a PCB instance at the specified index
        if isinstance(pcb, PCB):
            self.__process_list.insert(index, pcb)
        else:
            # Raise a ValueError if the input is not a PCB instance
            raise ValueError("Error: Only PCB instances can be inserted.")
        
    def reorder_by_process_ids(self, new_order):
        # Check if the input list has the same elements as the current process IDs
        if sorted(new_order) != sorted([pcb.get_process_id() for pcb in self.__process_list]):
            raise ValueError("Error: Input list must contain the same process IDs as the current list.")

        # Create a new list to hold the reordered PCBs
        reordered_list = []

        # Iterate through the input list of process IDs
        for process_id in new_order:
            # Find the PCB with the matching process ID in the current list
            pcb_index = self.__find_index_by_process_id(process_id)
            if pcb_index is not None:
                # Add the found PCB to the reordered list
                reordered_list.append(self.__process_list[pcb_index])

        # Update the process_list with the reordered list
        self.__process_list = reordered_list
        
    def get_running_pcb(self):
        running_pcb = None

        for pcb in self.__process_list:
            if pcb.get_is_running():
                if running_pcb is not None:
                    raise ValueError("Error: Multiple running PCBs found in the list.")
                running_pcb = pcb
        return running_pcb
    
    def increment_process_waiting(self, increment):
        for pcb in self.__process_list:
            if not pcb.get_is_running():
                pcb.increment_wait_time(increment)
        
    
    def find_index_by_process_id(self, target_process_id):
        for index, pcb in enumerate(self.__process_list):
            if pcb.get_process_id() == target_process_id:
                return index
        raise ValueError("Error: Process ID not found in the list.")

    def append(self, pcb):
        # Append a PCB instance to the end of the list
        if isinstance(pcb, PCB):
            self.__process_list.append(pcb)
        else:
            # Raise a ValueError if the input is not a PCB instance
            raise ValueError("Error: Only PCB instances can be appended.")

    def pop(self, index=-1):
        # Remove and return an element at the specified index (default is the last element)
        if index < 0:
            index += len(self.__process_list)

        if 0 <= index < len(self.__process_list):
            return self.__process_list.pop(index)
        else:
            # Raise an IndexError if the index is out of range
            raise IndexError("Error: Index out of range.")

    def get(self, index):
        # Get an element at the specified index
        if 0 <= index < len(self.__process_list):
            return self.__process_list[index]
        else:
            # Raise an IndexError if the index is out of range
            raise IndexError("Error: Index out of range.")

    def set(self, index, pcb):
        # Set an element at the specified index to a PCB instance
        if index < 0:
            index += len(self.__process_list)

        if 0 <= index < len(self.__process_list):
            if isinstance(pcb, PCB):
                self.__process_list[index] = pcb
            else:
                # Raise a ValueError if the input is not a PCB instance
                raise ValueError("Error: Input must be a PCB instance.")
        else:
            # Raise an IndexError if the index is out of range
            raise IndexError("Error: Index out of range.")

    def get_process_list(self):
        # Get the entire list of PCB instances
        return self.__process_list
    
    def __iter__(self):
        self.__index = 0  # Initialize the index when starting iteration
        return self

    def __next__(self):
        if self.__index < len(self.__process_list):
            current_pcb = self.__process_list[self.__index]
            self.__index += 1
            return current_pcb
        else:
            raise StopIteration
        
    def __len__(self):
        return len(self.__process_list)

    def is_empty(self):
        # Check if the list is empty
        return len(self.__process_list) == 0
    
    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.__process_list):
                return self.__process_list[index]
            else:
                raise IndexError("Index out of range")
        elif isinstance(index, slice):
            return self.__process_list[index]
        else:
            raise TypeError("Unsupported index type")
    
    def __str__(self):
        pcb_strings = [str(pcb) for pcb in self.__process_list]
        return "\n".join(pcb_strings)