import pymysql
import secret

from models.base_model import SQLModel
from models.session import Session
from models.user import User
from models.weibo import Weibo
from models.comment import Comment


def recreate_table(cursor):
    cursor.execute(User.sql_create)
    cursor.execute(Session.sql_create)
    cursor.execute(Weibo.sql_create)
    cursor.execute(Comment.sql_create)


def recreate_database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=secret.mysql_password,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'DROP DATABASE IF EXISTS `{}`'.format(
                secret.db_name
            )
        )
        cursor.execute(
            'CREATE DATABASE `{}` DEFAULT CHARACTER SET utf8mb4'.format(
                secret.db_name
            )
        )
        cursor.execute('USE `{}`'.format(secret.db_name))

        recreate_table(cursor)

    connection.commit()
    connection.close()


def test_data():
    SQLModel.init_db()


if __name__ == '__main__':
    recreate_database()
    test_data()
