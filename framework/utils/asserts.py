from assertpy import assert_that

from framework.logger.logger import Logger


def assert_equal(left_part, right_part, message, soft_assert=False):
    logger = Logger.get_logger()
    try:
        assert_that(left_part, message).is_equal_to(right_part)
    except AssertionError as err:
        logger.error(message)
        if not soft_assert:
            raise err


def assert_not_equal(left_part, right_part, message, soft_assert=False):
    logger = Logger.get_logger()
    try:
        assert left_part != right_part, message
    except AssertionError as err:
        logger.error(message)
        if not soft_assert:
            raise err


def assert_true(expression, message, soft_assert=False):
    logger = Logger.get_logger()
    try:
        assert expression, message
    except AssertionError as err:
        logger.error(message)
        if not soft_assert:
            raise err


def assert_false(expression, message, soft_assert=False):
    logger = Logger.get_logger()
    try:
        assert not expression, message
    except AssertionError as err:
        logger.error(message)
        if not soft_assert:
            raise err


def assert_in(left_part, right_part, message, soft_assert=False):
    logger = Logger.get_logger()
    try:
        assert left_part in right_part, message
    except AssertionError as err:
        logger.error(message)
        if not soft_assert:
            raise err


def assert_greater(left_part, right_part, message, soft_assert=False):
    logger = Logger.get_logger()
    try:
        assert left_part > right_part, message
    except AssertionError as err:
        logger.error(message)
        if not soft_assert:
            raise err
