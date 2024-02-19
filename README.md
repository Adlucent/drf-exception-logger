# drf-exception-logger
Package to catch and log exceptions in django applications

## Setup
1. Install
    - `pip install git+https://github.com/Adlucent/drf-exception-logger.git`
2. Add to middleware
    - Place at the top of the middleware list
    ```python
    MIDDLEWARE = [
        "drf_exception_logger.exception_logger.ExceptionLoggerMiddleware",
        ...
    ]
    ```

3. Turn on Exception Propagation
    - `DEBUG_PROPAGATE_EXCEPTIONS = True`
