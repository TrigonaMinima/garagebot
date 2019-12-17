from utils.db import generic
from utils.fileio import config

from pathlib import Path


def get_text(date_from, date_to=2000000000):
    assets_dir = Path(config["DIR"]["assets"])
    db_path = assets_dir / config["DB"]["file"]

    table_name = config["DB"]["chat_table"]
    bot_username = config["META"]["bot_username"]

    con = generic.get_connection(db_path)
    cur = con.cursor()
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
    return all_text
