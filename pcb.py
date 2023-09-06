class PCB:
    def __init__(self, process_id, arrival_time, CPU_burst, priority=None):
        self.process_id = int(process_id)
        self.arrival_time = int(arrival_time)
        self.CPU_burst = int(CPU_burst)
        self.priority = int(priority)

    def __str__(self):
        if self.priority is not None:
            return f"Process ID: {self.process_id}, Arrival Time: {self.arrival_time}, CPU Burst: {self.CPU_burst}, Priority: {self.priority}"
        else:
            return f"Process ID: {self.process_id}, Arrival Time: {self.arrival_time}, CPU Burst: {self.CPU_burst}"