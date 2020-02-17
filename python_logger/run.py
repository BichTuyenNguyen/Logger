from log4p import Logger, LEVELS
from calculation import Caculation

# start log
Logger().start_log()

# log String type
Logger().print_log(LEVELS['info'], "this is a log.")

# Log Integer type
Caculation.add(4, 5)

# Log Dictionary type
data = {'name:': 'tuyen', 'age': '23'}
Logger().print_log(20, "add data - " + str(data))

# end log
Logger().finish_log()
