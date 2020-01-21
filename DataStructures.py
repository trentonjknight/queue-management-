class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        pass
    def dequeue(self):
        pass
    def get_queue(self):
        pass
    def size(self):
        return len(self._queue) 

# class List:
#     def __init__(self):
#         self.x = []
#         pass
#     def add(self, param1):
#         pass
#     def delete(self):
#         pass
#     def print(self):
#         pass
