import prefect
from prefect import flow, task, get_run_logger


@task
def log_task(name):
    logger = get_run_logger()
    logger.info("Hello %s!", name)
    logger.info("Prefect Version = %s 🚀", prefect.__version__)


@flow()
def log_flow(name: str = "Oscar"):
    log_task(name)
