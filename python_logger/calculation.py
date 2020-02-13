from log4p import Logger, LEVELS


class Caculation:

    @staticmethod
    def add(a, b):
        Logger().print_log(LEVELS['info'], 'start add function - result: {result}'.format(result=str(a+b)))
        return a + b
