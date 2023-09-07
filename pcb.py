class PCB:
    def __init__(self, process_id, arrival_time, CPU_burst, priority=None):
        self.__process_id = int(process_id)
        self.__arrival_time = int(arrival_time)
        self.__CPU_burst = int(CPU_burst)
        self.__priority = int(priority)
        self.__wait_time = 0
        self.__has_run = False
        self.__is_running = False
        self.__last_run = -1

    def increment_wait_time(self, increment):
        self.__wait_time += increment

    def get_wait_time(self):
        return self.__wait_time


    def get_has_run(self):
        return self.__has_run

    def set_has_run(self, has_run):
        if isinstance(has_run, bool):
            self.__has_run = has_run
        else:
            raise ValueError("Error: 'has_run' must be a boolean value.")
        
    def get_last_run(self):
        return self.__last_run

    def set_last_run(self, time):
        self.__last_run = time

    def get_is_running(self):
        return self.__is_running

    def set_is_running(self, is_running):
        if isinstance(is_running, bool):
            self.__is_running = is_running
        else:
            raise ValueError("Error: 'is_running' must be a boolean value.")
    
    def get_process_id(self):
        return self.__process_id
    

    def set_process_id(self, process_id):
        if isinstance(process_id, int) and process_id >= 0:
            self.__process_id = process_id
        else:
            raise ValueError("Error: Process ID must be a non-negative integer.")

    def get_arrival_time(self):
        return self.__arrival_time

    def set_arrival_time(self, arrival_time):
        if isinstance(arrival_time, int) and arrival_time >= 0:
            self.__arrival_time = arrival_time
        else:
            raise ValueError("Error: Arrival time must be a non-negative integer.")

    def get_CPU_burst(self):
        return self.__CPU_burst

    def set_CPU_burst(self, CPU_burst):
        if isinstance(CPU_burst, int) and CPU_burst >= 0:
            self.__CPU_burst = CPU_burst
        else:
            raise ValueError("Error: CPU burst must be a non-negative integer.")

    def get_priority(self):
        return self.__priority

    def set_priority(self, priority):
        if priority is not None:
            if isinstance(priority, int) and priority >= 0:
                self.__priority = priority
            else:
                raise ValueError("Error: Priority must be a non-negative integer.")
        else:
            self.__priority = None

    def __str__(self):
        if self.__priority is not None:
            return f"Process ID: {self.__process_id}, Arrival Time: {self.__arrival_time}, CPU Burst: {self.__CPU_burst}, Wait Time: {self.__wait_time}, Is Running: {self.__is_running}, Priority: {self.__priority}"
        else:
            return f"Process ID: {self.__process_id}, Arrival Time: {self.__arrival_time}, CPU Burst: {self.__CPU_burst}, Wait Time: {self.__wait_time}, Is Running: {self.__is_running}"