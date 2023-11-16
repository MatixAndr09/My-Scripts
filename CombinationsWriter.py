import itertools,time,sys,os

try:
    def seconds_to_hms(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)
        months, weeks = divmod(weeks, 4)
        return months, weeks, days, hours, minutes, seconds

    def bytes_to_gb(bytes):
        return bytes / (1024 ** 3)

    def write_combinations_to_file(filename_i, max_length):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}:?<>|"

        with open(filename_i, "w") as file:
            total_combinations = sum(len(characters) ** length for length in range(1, max_length + 1))
            progress = 0
            start_time = time.time()

            for length in range(1, max_length + 1):
                for combination in itertools.product(characters, repeat=length):
                    word = ''.join(combination)
                    file.write(word + '\n')
                    progress += 1
                    elapsed_time = time.time() - start_time
                    completion_percentage = (progress / total_combinations) * 100
                    
                    if elapsed_time > 0:
                        estimated_time = (elapsed_time / progress) * (total_combinations - progress)
                    else:
                        estimated_time = 0
                    
                    months, weeks, days, hours, minutes, seconds = seconds_to_hms(estimated_time)

                    sys.stdout.write(f"\rProgress: {progress}/{total_combinations} ({completion_percentage:.2f}%), ETA: {months}mo {weeks}w {days}d {hours}h {minutes}m {round(seconds, 1)}s, ")
                    sys.stdout.flush()

        print(f"\nCombinations have been written to {filename_i}")

    filename_i = input("File name: ")
    max_length = int(input("Max length of combinations: "))
    write_combinations_to_file(filename_i, max_length)
    
except KeyboardInterrupt:
    print(f"\n\nKeyboard Interrupted deleting {filename_i}\n")
    os.remove(filename_i)
    