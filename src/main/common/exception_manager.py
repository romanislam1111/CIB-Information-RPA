from src.main.common.log_manager import application_logger

class ExceptionManager():

    def handle_exceptions(self, f):

        
        def wrapper(*args, **kw):
            logger = application_logger
            try:
                logger.info(f" Trying to execute .... {f.__name__} " )
                return f(*args, **kw)

            except Exception as e:
                # return
                logger.warning(f"Failed to execute function *{f.__name__}* {args} {kw} due to : {e}", exc_info=True)
                # logging.critical(f"{e}\n{'-'*90}", exc_info=True)
                # logging.error(f"Failed to execute function *{f.__name__}* {args} {kw} due to : {e}", exc_info=True)
                raise Exception
            finally:
                logger.info(f" Finished Execution  for function  {f.__name__} " )
       
        return wrapper
