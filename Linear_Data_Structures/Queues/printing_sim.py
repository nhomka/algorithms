from Queue import Queue
from random import randrange


class Printer():

    def __init__(self, ppm):
        """Initialize a printer"""
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
        self.queue = Queue()
        self.wait_times = []

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None
    
    def busy(self):
        return self.current_task is not None
        
    def start_next(self, current_second):
        if not self.queue.is_empty():
            self.current_task = self.queue.dequeue()
            self.time_remaining = self.current_task.get_pages() * 60 / self.page_rate
            self.wait_times.append(self.current_task.wait_time(current_second))

    def queue_task(self, task):
        self.queue.enqueue(task)

    def queue_size(self):
        return self.queue.size()

    def get_wait_times(self):
        return self.wait_times


class PrintTask():

    def __init__(self, time):
        """Initialize a printing task"""
        self.timestamp = time
        self.pages = randrange(1, 21)

    def get_time(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp

def new_print_task(num_students, docs_per_hour):
    seconds = 3600/(num_students*docs_per_hour)
    num = randrange(1, seconds+1)
    return num == seconds

def simulation(num_seconds, pages_per_minute, students, dph):
    printer = Printer(pages_per_minute)

    for current_second in range(num_seconds):
        if new_print_task(students, dph):
            task = PrintTask(current_second)
            printer.queue_task(task)

        if not printer.busy():
            printer.start_next(current_second)

        printer.tick()

    average_wait = sum(printer.get_wait_times()) / len(printer.get_wait_times())
    print (f"Average Wait {average_wait:6.2f} secs {printer.queue_size():3d} tasks remaining.")

for i in range(10):
    simulation(3600, 10, 30, 2)