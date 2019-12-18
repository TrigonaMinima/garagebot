from utils.db import generic
from utils.fileio import config

from pathlib import Path


def get_users():
    assets_dir = Path(config["DIR"]["assets"])
    db_path = assets_dir / config["DB"]["file"]
    con = generic.get_connection(db_path)
    cur = con.cursor()

    table_name = config["DB"]["chat_table"]
    query = f"""
        SELECT DISTINCT FROM_ID, FROM_NAME
        FROM {table_name}
    """
    all_users = cur.execute(query)
    all_users = dict(all_users)
    con.close()
    return all_users


def get_text(date_from, date_to=2000000000):
    assets_dir = Path(config["DIR"]["assets"])
    db_path = assets_dir / config["DB"]["file"]
    con = generic.get_connection(db_path)
    cur = con.cursor()

    table_name = config["DB"]["chat_table"]
    bot_username = config["META"]["bot_username"]
    query = f"""
        SELECT MESSAGE
        FROM {table_name}
        WHERE TIMESTAMP > {date_from}
            AND TIMESTAMP < {date_to}
            AND FROM_NAME <> '{bot_username}'
            AND CHAT_TYPE = 'group'
            AND MESSAGE IS NOT NULL
    """
    all_text = cur.execute(query)
    all_text = " ".join([i[0] for i in all_text])
    con.close()
    return all_text


def get_counts(col, date_from, date_to=2000000000):
    assets_dir = Path(config["DIR"]["assets"])
    db_path = assets_dir / config["DB"]["file"]
    con = generic.get_connection(db_path)
    cur = con.cursor()

    table_name = config["DB"]["chat_table"]
    bot_username = config["META"]["bot_username"]
    query = f"""
        SELECT FROM_ID, SUM({col})
        FROM {table_name}
        WHERE TIMESTAMP > {date_from}
            AND TIMESTAMP < {date_to}
            AND FROM_NAME <> '{bot_username}'
            AND CHAT_TYPE = 'group'
        GROUP BY FROM_ID
        HAVING SUM({col}) > 0
        ORDER BY 2 DESC;
    """
    counts = cur.execute(query)
    counts = dict(counts)
    con.close()
    return counts


def get_cuss_counts(date_from, date_to=2000000000):
    return get_counts("NUM_GAALIYA", date_from, date_to)


def get_command_counts(date_from, date_to=2000000000):
    return get_counts("IS_COMMAND", date_from, date_to)
