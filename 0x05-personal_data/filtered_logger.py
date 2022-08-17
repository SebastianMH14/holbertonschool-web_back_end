#!/usr/bin/env python3
""" This module creates a filter_datum function """

import re
import os
import logging
import mysql.connector

from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the record into specified self.FORMAT """
        mesagge = super().format(record)
        mesagge_formatter = filter_datum(
            self.fields, self.REDACTION, mesagge, self.SEPARATOR)
        return mesagge_formatter


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ returns the log message """
    for fld in fields:
        message = re.sub(f"(?<={fld}=).*?(?={separator})", redaction, message)
    return message


def get_logger() -> logging.Logger:
    """
    Return: Instances of the Logger class represent a single logging channel.
    A "logging channel" indicates an area of an application
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    connect to the MySQL database
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    host = os.getenv('PERSONAL_DATA_DB_HOST')
    db = os.getenv('PERSONAL_DATA_DB_NAME')

    conect = mysql.connector.connection.MySQLConnection(
            host=host,
            user=username,
            password=password,
            database=db
        )
    return conect


def main():
    """ get data from database """
    data = get_db()
    myCursor = data.cursor()
    myCursor.execute("SELECT * FROM users")
    description = [desc[0] for desc in myCursor.description]

    logger = get_logger()

    for user in myCursor:
        userInfo = "".join(
                f'{des}={str(usr)}; ' for usr, des in zip(user, description)
            )
        logger.info(userInfo)

    myCursor.close()
    data.close()


if __name__ == '__main__':
    main()
