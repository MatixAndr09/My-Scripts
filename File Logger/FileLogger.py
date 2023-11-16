from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from colorama import Fore,Style
import psutil
import time
import os

good_ = f"{Fore.WHITE + Style.BRIGHT}[{Fore.GREEN}+{Fore.WHITE + Style.RESET_ALL}] "
error_ = f"{Fore.WHITE + Style.BRIGHT}[{Fore.RED}-{Fore.WHITE + Style.RESET_ALL}] "
warn_ = f"{Fore.WHITE + Style.BRIGHT}[{Fore.YELLOW}!{Fore.WHITE + Style.RESET_ALL}] "
info_ = f"{Fore.WHITE + Style.BRIGHT}[{Fore.BLUE}={Fore.WHITE + Style.RESET_ALL}] "

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.processes = set()

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'{warn_}Modified: {event.src_path}')

    def on_created(self, event):
        if event.is_directory:
            return
        print(f'{good_}New: {event.src_path}')

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f'{error_}Deleted: {event.src_path}')

    def on_executed(self, process):
        print(f'{info_}Executed:  {process.name()} (PID: {process.pid})')

def monitor_disk(disk_path):
    event_handler = MyHandler()
    observer = Observer()

    observer.schedule(event_handler, path=disk_path, recursive=True)

    print(f'{info_}Tracking changes on disk: {disk_path}')
    observer.start()

    try:
        while True:
            # Monitorowanie nowo uruchomionych procesów
            current_processes = {p.name() for p in psutil.process_iter()}
            new_processes = current_processes - event_handler.processes
            for process_name in new_processes:
                process = psutil.Process(os.getpid())
                event_handler.on_executed(process)
            event_handler.processes = current_processes

            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    disk_to_watch = "/"

    monitor_disk(disk_to_watch)
