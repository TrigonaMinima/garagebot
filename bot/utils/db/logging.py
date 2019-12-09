from utils.regexps import url_regex
from utils.db.generic import insert_row


def get_quoted_data(quoted_dict):
    if not quoted_dict:
        return 0, None, None, None

    quoted = 1
    quoted_user = str(quoted_dict.from_user.id)
    quoted_user_name = quoted_dict.from_user.username
    quoted_text = quoted_dict.text
    return (quoted, quoted_user, quoted_user_name, quoted_text)


def get_common_values(update):
    row = {}
    row["TIMESTAMP"] = int(update.effective_message.date.strftime("%s"))

    # Chat details
    row["CHAT_ID"] = str(update.effective_chat.id)
    row["CHAT_TYPE"] = update.effective_chat.type
    row["CHAT_NAME"] = update.effective_chat.username or update.effective_chat.title

    # Message details
    row["MESSAGE"] = update.effective_message.text
    row["IS_COMMAND"] = 0

    row["FROM_ID"] = update.effective_user.id
    row["FROM_NAME"] = update.effective_user.username
    row["IS_BOT"] = 0

    quoted = get_quoted_data(update.effective_message.reply_to_message)
    row["QUOTED"] = quoted[0]
    row["QUOTED_PERSON_ID"] = quoted[1]
    row["QUOTED_PERSON_NAME"] = quoted[2]
    row["QUOTED_TEXT"] = quoted[3]

    urls = "" if row["MESSAGE"] is None else row["MESSAGE"]
    urls = list(url_regex.findall(urls))
    row["LINKS"] = "|".join(urls)
    row["LINKS"] = row["LINKS"] if row["LINKS"] else None
    row["NUM_LINKS"] = len(urls)

    row["GAALIYA"] = None
    row["NUM_GAALIYA"] = 0
    row["IS_SCREAM"] = 0

    row["CORRECTIONS"] = None
    row["NUM_CORRECTIONS"] = 0

    row["TOT_WORDS"] = 0
    row["UNIQ_WORDS"] = 0
    row["ADDED_TOT_WORDS"] = 0
    row["ADDED_UNIQ_WORDS"] = 0
    row["CODE_SWITCH"] = 0

    row["RAW_JSON"] = None
    return row


def log_command(update):
    row_dict = get_common_values(update)
    row_dict["IS_COMMAND"] = 1
    row_dict["RAW_JSON"] = update.to_json()

    row = insert_row(row_dict)
    print(row[:-1])


def log_bot_reply(update):
    update.effective_message = update
    update.effective_chat = update.chat
    update.effective_user = update.bot
    row_dict = get_common_values(update)

    del update.effective_chat
    del update.effective_user
    del update.effective_message
    row_dict["RAW_JSON"] = update.to_json()
    row_dict["IS_BOT"] = 1

    row = insert_row(row_dict)
    print(row[:-1])


def log_text_replies(update):
    row_dict = get_common_values(update)

    row_dict["GAALIYA"] = "|".join(update.gaaliya) if update.gaaliya else None
    row_dict["NUM_GAALIYA"] = len(update.gaaliya) if update.gaaliya else 0
    row_dict["IS_SCREAM"] = 1 if update.scream else 0

    update.corrections = [f"s/{w1}/{w2}/g" for w1, w2 in update.corrections]
    row_dict["NUM_CORRECTIONS"] = len(update.corrections)

    update.corrections = "|".join(update.corrections)
    row_dict["CORRECTIONS"] = update.corrections if update.corrections else None

    del update.scream
    del update.corrections
    del update.gaaliya
    row_dict["RAW_JSON"] = update.to_json()

    row = insert_row(row_dict)
    print(row[:-1])
