import re

if __name__ == '__main__':

    number_of_requests = 0
    template = r"\b/Games/mines.+\.gif\b"
    log_file = open("logs", "r")
    result_file = open("result", "w")

    for line in log_file:
        if re.findall(template, line):
            number_of_requests += 1
            result_file.write(line)

    log_file.close()
    print (number_of_requests)

