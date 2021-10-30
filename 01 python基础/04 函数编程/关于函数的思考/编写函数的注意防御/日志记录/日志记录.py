import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler

handler.setLevel(logging.WARNING)
handler.setLevel(logging.ERROR)

format_c = logging.Formatter('%(name)-%(levelname)-%(message)')
handler.setFormatter(format_c)

logging.addHandler()


def division(divident, divisor):
    try:
        return divident / divisor
    except ZeroDivisionError:
        logger.error('Zero Division Error')


num = division(4, 0)
