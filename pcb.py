class PCB:
    def __init__(self, process_id, arrival_time, CPU_burst, priority=None):
        self.process_id = int(process_id)
        self.arrival_time = int(arrival_time)
        self.CPU_burst = int(CPU_burst)
        self.priority = int(priority)
        self.wait_time = 0
        self.has_run = False
        self.is_running = False

    def increment_wait_time(self, increment):
        self.wait_time += increment


    def get_has_run(self):
        return self.has_run

    def set_has_run(self, has_run):
        if isinstance(has_run, bool):
            self.has_run = has_run
        else:
            raise ValueError("Error: 'has_run' must be a boolean value.")

    def get_is_running(self):
        return self.is_running

    def set_is_running(self, is_running):
        if isinstance(is_running, bool):
            self.is_running = is_running
        else:
            raise ValueError("Error: 'is_running' must be a boolean value.")
    
    def get_process_id(self):
        return self.process_id
    

    def set_process_id(self, process_id):
        if isinstance(process_id, int) and process_id >= 0:
            self.process_id = process_id
        else:
            raise ValueError("Error: Process ID must be a non-negative integer.")

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, arrival_time):
        if isinstance(arrival_time, int) and arrival_time >= 0:
            self.arrival_time = arrival_time
        else:
            raise ValueError("Error: Arrival time must be a non-negative integer.")

    def get_CPU_burst(self):
        return self.CPU_burst

    def set_CPU_burst(self, CPU_burst):
        if isinstance(CPU_burst, int) and CPU_burst >= 0:
            self.CPU_burst = CPU_burst
        else:
            raise ValueError("Error: CPU burst must be a non-negative integer.")

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        if priority is not None:
            if isinstance(priority, int) and priority >= 0:
                self.priority = priority
            else:
                raise ValueError("Error: Priority must be a non-negative integer.")
        else:
            self.priority = None

    def __str__(self):
        if self.priority is not None:
            return f"Process ID: {self.process_id}, Arrival Time: {self.arrival_time}, CPU Burst: {self.CPU_burst}, Priority: {self.priority}"
        else:
            return f"Process ID: {self.process_id}, Arrival Time: {self.arrival_time}, CPU Burst: {self.CPU_burst}"