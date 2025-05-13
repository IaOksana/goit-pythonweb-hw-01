import logging

# init logger
logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler("task_1.log"), logging.StreamHandler()],
)

def info(str):
    logging.info(str)