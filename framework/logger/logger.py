import inspect
import json
import os
from json.decoder import JSONDecodeError

import loguru

import framework.utils.utils as helpers


class Logger:
    _instance = None
    _worker_id = None
    _root_dir = helpers.get_root_dir()

    def __init__(self):
        self.logger = loguru.logger
        with open(os.path.join(Logger._root_dir, "configs", "logger_config.json")) as config_file:
            self.config = json.load(config_file)
        if Logger._worker_id == "master":
            log_file = os.path.join(Logger._root_dir, "logs", f"{Logger._worker_id}.log")
        else:
            log_file = os.path.join(Logger._root_dir, "logs", f"worker_{Logger._worker_id}.log")
        self.logger.add(
            sink=log_file,
            format=self.config["format"],
            level=self.config["level"],
            rotation=self.config["rotation"],
            retention=self.config["retention"],
            compression=self.config["compression"],
            encoding="utf-8",
        )
        self.step_counter = 0

    @staticmethod
    def get_logger():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def test_name(self, **kwargs) -> None:
        self.step_counter = 0
        test_name = inspect.stack()[1][3]
        self.logger.info(f"START TEST: {test_name}, {kwargs}" + "\n")

    def step(self, step_desc: str) -> None:
        self.step_counter += 1
        self.logger.info("\n" + f"{'~' * 50}")
        self.logger.info(f"STEP {self.step_counter}: {step_desc}")
        self.logger.info(f"{'~' * 50}" + "\n")

    def debug(self, msg: str) -> None:
        self.logger.debug(f'{"*" * 50}')
        self.logger.debug(msg)
        self.logger.debug(f'{"*" * 50}' + "\n")

    def error(self, msg: str) -> None:
        self.logger.error(f'{"x" * 50}')
        self.logger.error(msg)
        self.logger.error(f'{"x" * 50}' + "\n")

    def api(self, response) -> None:
        self.logger.info(f"{'*' * 50}")
        self.logger.info(f"HTTP Method: {response.request.method} - {response.url}")
        self.logger.debug(f"req_headers: {response.request.headers}")
        self.logger.debug(f"req_body: {response.request.body}")
        self.logger.debug("-" * 50)
        self.logger.debug(f"res_status_code: {response.status_code}")
        self.logger.debug(f"res_headers: {response.headers}")
        try:
            self.logger.debug(f"res_body: {response.json()}")
        except JSONDecodeError:
            self.logger.debug("Response without json_data")
        self.logger.info(f"{'*' * 50}" + "\n")
