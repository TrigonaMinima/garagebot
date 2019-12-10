import sqlite3

from pathlib import Path

from utils.fileio import config


def get_connection(dbname):
    con = sqlite3.connect(dbname)
    return con


def check_db(db_path):
    if not db_path.exists():
        return 0
    return 1


def check_table(db_path, table):
    con = get_connection(db_path)
    cur = con.cursor()

    q = f"""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
            AND name='{table}';
    """
    rows = [i for i in cur.execute(q)]
    if not rows:
        return 0
    return 1


def create_db(db):
    if not check_db(db):
        sqlite3.connect(db)


def generate_create_table_query(table_name):
    q = f"""
        CREATE TABLE IF NOT EXISTS "{table_name}" (
            "TIMESTAMP" INTEGER,
            "CHAT_ID" TEXT,
            "CHAT_TYPE" TEXT,
            "CHAT_NAME" TEXT,
            "MESSAGE" TEXT,
            "IS_COMMAND" INTEGER,
            "FROM_ID" TEXT,
            "FROM_NAME" TEXT,
            "IS_BOT" INTEGER,
            "QUOTED" TEXT,
            "QUOTED_PERSON_ID" TEXT,
            "QUOTED_PERSON_NAME" TEXT,
            "QUOTED_TEXT" TEXT,
            "LINKS" TEXT,
            "NUM_LINKS" INTEGER,
            "GAALIYA" TEXT,
            "NUM_GAALIYA" INTEGER,
            "IS_SCREAM" INTEGER,
            "CORRECTIONS" TEXT,
            "NUM_CORRECTIONS" INTEGER,
            "TOT_WORDS" TEXT,
            "UNIQ_WORDS" TEXT,
            "ADDED_TOT_WORDS" TEXT,
            "ADDED_UNIQ_WORDS" TEXT,
            "CODE_SWITCH" TEXT,
            "RAW_JSON" TEXT
        );
    """
    return q


def create_db_tables(db, db_config):
    con = get_connection(db)
    cur = con.cursor()

    table_name = config["DB"]["chat_table"]
    q = generate_create_table_query(table_name)

    cur.execute(q)
    con.commit()
    con.close()


def get_table_cols():
    table_cols = [
        "TIMESTAMP", "CHAT_ID", "CHAT_TYPE", "CHAT_NAME", "MESSAGE",
        "IS_COMMAND", "FROM_ID", "FROM_NAME", "IS_BOT", "QUOTED",
        "QUOTED_PERSON_ID", "QUOTED_PERSON_NAME", "QUOTED_TEXT", "LINKS",
        "NUM_LINKS", "GAALIYA", "NUM_GAALIYA", "IS_SCREAM", "CORRECTIONS",
        "NUM_CORRECTIONS", "TOT_WORDS", "UNIQ_WORDS", "ADDED_TOT_WORDS",
        "ADDED_UNIQ_WORDS", "CODE_SWITCH", "RAW_JSON"
    ]
    return table_cols


def construct_insert_query(table_name, table_cols):
    query = (
        f"INSERT INTO {table_name} "
        f"({','.join(table_cols)}) "
        f"VALUES ({','.join('?'*len(table_cols))})"
    )
    return query


def insert_row(row_dict):
    assets_dir = Path(config["DIR"]["assets"])
    db_path = assets_dir / config["DB"]["file"]
    table_name = config["DB"]["chat_table"]

    con = get_connection(db_path)
    cur = con.cursor()

    query = construct_insert_query(table_name, get_table_cols())
    row = [row_dict[col] for col in get_table_cols()]
    cur.execute(query, row)

    con.commit()
    con.close()
    return row
