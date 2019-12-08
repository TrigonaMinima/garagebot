import sqlite3

from pathlib import Path


def get_connection(dbname):
    con = sqlite3.connect(dbname)
    return con


def check_db(db_path):
    if not db_path.exists():
        return 0
    return 1


def check_table(db_path, table):
    q = f"""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
            AND name='{table}';
    """
    con = get_connection(db_path)
    cur = con.cursor()
    rows = [i for i in cur.execute(q)]
    if not rows:
        return 0
    return 1


def create_db(db):
    if not check_db(db):
        sqlite3.connect(db)


def create_chats_table(cursor, table_name):
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
    cursor.execute(q)


def create_db_tables(db, db_config):
    con = get_connection(db)
    cur = con.cursor()

    chats_table = db_config["chat_table"]
    create_chats_table(cur, chats_table)

    con.commit()
    con.close()
