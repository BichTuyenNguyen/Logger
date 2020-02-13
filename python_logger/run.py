from log4p import Logger, LEVELS
from calculation import Caculation

data = {'name:': 'tuyen', 'age': '23'}
Logger().start_log()
Logger().print_log(LEVELS['info'], "tuyen xinh dep")
Caculation.add(4, 5)
Logger().print_log(20, "add data - " + str(data) )
Logger().finish_log()
