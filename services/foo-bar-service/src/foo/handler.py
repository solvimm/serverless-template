import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    try:
        logger.info(event)
        return 'Success'
    except Exception as e:
        logger.error(e)
        raise e