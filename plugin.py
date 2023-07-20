from tqdm.contrib.telegram import tqdm 
from ocrmypdf import hookimpl

# Переменные для хранения параметров token и chat_id
token = None
chat_id = None

@hookimpl
def add_options(parser):
    # Добавляем параметры командной строки token и chat_id
    parser.add_argument(
        "--token",
        type=str,
        help="Telegram bot token for the progress updates."
    )
    parser.add_argument(
        "--chat-id",
        type=int,
        help="Telegram chat ID to send the progress updates."
    )

@hookimpl
def check_options(options):
    global token, chat_id
    token = options.token
    chat_id = options.chat_id

@hookimpl
def get_progressbar_class():
    class TelegramProgress(tqdm):
      def __init__(self, **kwards):
        super(TelegramProgress, self).__init__(
            token=token, chat_id=chat_id, **kwards
        )
    # Возвращаем класс TelegramProgress
    return TelegramProgress
