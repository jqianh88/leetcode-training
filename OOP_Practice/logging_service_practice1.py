'''
Problem Statement
Design a Logging Service that supports the following functionalities:

Log messages at different levels: INFO, DEBUG, ERROR.
Retrieve logs based on time range or log level.
Support filtering by log source (e.g., a specific service or component).
Allow deletion of logs older than a certain time.
'''
'''
Classes:
- Log
-- Abstract class
--- properties: log_id, log_level, timestamp, source, content
- LogService
-- Methods
- get_logs_by_time_range, get_logs_by_log_level, get_logs_by_log_source, delete_logs(before_time)
- LogDB
--> logs: {log_id: log}
--> inverted_index: log_level+log_source: []
'''

from abc import ABC, abstractmethod
from collections import defaultdict
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4

class LogLevel(Enum):
    INFO = "info"
    DEBUG = "debug"
    ERROR = "error"

class LogException(Exception):
    pass

class LogDBException(LogException):
    pass

class Log(ABC):
    def __init__(self, content: str, log_source: str):
        self.log_id = uuid4()
        self.content = content
        self.log_level = ""
        self.log_source = log_source
        self.timestamp = datetime.now(timezone.utc)

class InfoLog(Log):
    def __init__(self, content: str, log_source: str):
        super().__init__(content=content, log_source=log_source)
        self.log_level = LogLevel.INFO

    def __repr__(self):
        return f"{self.log_id}: {self.content} for {self.log_level} from {self.log_source} at {self.timestamp}."

class DebugLog(Log):
    def __init__(self, content: str, log_source: str):
        super().__init__(content=content, log_source=log_source)
        self.log_level = LogLevel.DEBUG

    def __repr__(self):
        return f"{self.log_id}: {self.content} for {self.log_level} from {self.log_source} at {self.timestamp}."

class ErrorLog(Log):
    def __init__(self, content: str, log_source: str):
        super().__init__(content=content, log_source=log_source)
        self.log_level = LogLevel.ERROR

    def __repr__(self):
        return f"{self.log_id}: {self.content} for {self.log_level} from {self.log_source} at {self.timestamp}."

class LogService:
    def __init__(self):
        self.log_db = LogDB()


    def add_log(self, content: str, log_level: str, log_source: str) -> Log:
        if log_level == LogLevel.DEBUG:
            log = DebugLog(content=content, log_source=log_source)
        elif log_level == LogLevel.INFO:
            log = InfoLog(content=content, log_source=log_source)
        else:
            log = ErrorLog(content=content, log_source=log_source)
        # log storage
        self.log_db.logs[log.log_id] = log

        # log storage inverted index by log level
        self.log_db.log_level_storage[log.log_level.value.lower()].append(log.log_id)

        # log storage inverted index by log level and source
        log_level_source = log.log_level.value + log.log_source
        self.log_db.log_level_source_storage[log_level_source.lower()].append(log.log_id)

        # log storage inverted index by time
        split_time = str(log.timestamp).split()
        day = split_time[0]
        hour = split_time[1].split(':')[0]
        timebracket = timebracket = f'{day}-{hour}'
        self.log_db.time_storage[timebracket].append(log.log_id)
        return log

    def get_log_by_log_id(self, log_id: str) -> Log:
        return self.log_db.logs[log_id]

    def get_logs_by_time_range(self, start: str, end: str) -> list[Log]:
        result = []
        for timebracket, log_list in self.log_db.time_storage.items():
            if start < timebracket < end:
                for log_id in log_list:
                    result += self.get_log_by_log_id(log_id=log_id)
        return result

    def _extract_time_range(self, time):
       split_time = str(time).split()
       day = split_time[0]
       hour = split_time[1].split(':')[0]
       return f'{day}-{hour}'

    def get_logs_by_log_level(self, log_level: str) -> list[Log]:
        log_list = self.log_db.log_level_storage[log_level]
        result = []
        for log_id in log_list:
            result += self.get_log_by_log_id(log_id=log_id)
    def get_logs_by_log_source(self, log_source: str):
        result = []
        for log_level_source, log_list in self.log_db.log_level_source_storage.items():
            if log_source.lower() in log_level_source:
                result += log_list
        return result
    def delete_logs(self, log_id: str):
        if log_id not in self.log_db.logs:
            raise LogDBException(f"{log_id} not found.")
        log = self.get_log_by_log_id(log_id=log_id)
        del self.log_db.logs[log_id]
        self.delete_log_level_storage_log(log.log_level.value, log.log_id)
        log_level_source = log.log_level.value + log.log_source
        self.delete_log_level_source_storage_log(log_level_source, log.log_id)
        timestamp = self._extract_time_range(log.timestamp)
        self.delete_time_storage_log(timestamp, log.log_id)
        return f"Removed {log} from all storage"


    def delete_log_level_storage_log(self, log_level: str, log_id: str):
        for i, id in enumerate(self.log_db.log_level_storage[log_level]):
            if log_id == id:
                self.log_db.log_level_storage[log_level].pop(i)
        return True

    def delete_log_level_source_storage_log(self, log_level_source: str, log_id: str):
        for i, id in enumerate(self.log_db.log_level_storage[log_level_source]):
            if log_id == id:
                self.log_db.log_level_storage[log_level_source].pop(i)
        return True
    def delete_time_storage_log(self, timestamp: str, log_id: str):
        for i, id in enumerate(self.log_db.log_level_storage[timestamp]):
            if log_id == id:
                self.log_db.log_level_storage[timestamp].pop(i)
        return True

class LogDB:
    def __init__(self):
        self.logs = {}
        self.log_level_storage =  defaultdict(list)
        self.log_level_source_storage = defaultdict(list)
        self.time_storage =  defaultdict(list)


if __name__ == "__main__":
    log_db = LogDB()
    log_service = LogService()
    log1 = log_service.add_log("thisisbad", "error", "abadplace")
    log2 = log_service.add_log("thisisbad", "info", "agoodplace")
    log3 = log_service.add_log("thisisgood", "debug", "someotherplace")
    log4 = log_service.add_log("thisisbad", "error", "foobar")
    log_service.get_logs_by_time_range('2025-01-11-21', '2025-01-11-23')
    log_service.get_logs_by_log_level('info')
    log_service.get_logs_by_log_source('abadplace')
    log_service.delete_logs(log1.log_id)