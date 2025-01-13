from abc import ABC, abstractmethod
from collections import defaultdict
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4

# Enum for Log Levels
class LogLevel(Enum):
    INFO = "info"
    DEBUG = "debug"
    ERROR = "error"

# Log Class
class Log:
    def __init__(self, content: str, log_level: LogLevel, log_source: str):
        self.log_id = str(uuid4())
        self.content = content
        self.log_level = log_level
        self.log_source = log_source
        self.timestamp = datetime.now(timezone.utc)

    def __repr__(self):
        return f"Log(id={self.log_id}, level={self.log_level.value}, source={self.log_source}, time={self.timestamp})"

# LogDB Class
class LogDB:
    def __init__(self):
        self.logs = {}  # Main storage for logs
        self.time_storage = defaultdict(list)  # Index for time range queries
        self.level_storage = defaultdict(list)  # Index for log level queries
        self.source_storage = defaultdict(list)  # Index for log source queries

# LogService Class
class LogService:
    def __init__(self):
        self.db = LogDB()

    def add_log(self, content: str, log_level: LogLevel, log_source: str) -> Log:
        log = Log(content, log_level, log_source)
        self.db.logs[log.log_id] = log

        # Index by time (hour granularity)
        time_key = log.timestamp.strftime("%Y-%m-%d-%H")
        self.db.time_storage[time_key].append(log.log_id)

        # Index by log level
        self.db.level_storage[log.log_level].append(log.log_id)

        # Index by source
        self.db.source_storage[log.log_source].append(log.log_id)

        return log

    def get_log_by_id(self, log_id: str) -> Log:
        if log_id not in self.db.logs:
            raise ValueError(f"Log with id {log_id} not found.")
        return self.db.logs[log_id]

    def get_logs_by_time_range(self, start: datetime, end: datetime) -> list[Log]:
        if start.tzinfo is None or end.tzinfo is None:
            raise ValueError("Start and end times must be timezone-aware.")
        results = []
        for time_key, log_ids in self.db.time_storage.items():
            timestamp = datetime.strptime(time_key, "%Y-%m-%d-%H").replace(tzinfo=timezone.utc)
            if start <= timestamp <= end:
                results.extend([self.get_log_by_id(log_id) for log_id in log_ids])
        return results

    def get_logs_by_log_level(self, log_level: LogLevel) -> list[Log]:
        log_ids = self.db.level_storage.get(log_level, [])
        return [self.get_log_by_id(log_id) for log_id in log_ids]

    def get_logs_by_log_source(self, log_source: str) -> list[Log]:
        log_ids = self.db.source_storage.get(log_source, [])
        return [self.get_log_by_id(log_id) for log_id in log_ids]

    def delete_logs_before(self, timestamp: datetime):
        if timestamp.tzinfo is None:
            raise ValueError("Timestamp must be timezone-aware.")
        to_delete = []
        for log_id, log in self.db.logs.items():
            if log.timestamp < timestamp:
                to_delete.append(log_id)

        for log_id in to_delete:
            log = self.db.logs.pop(log_id)

            # Remove from indexes
            time_key = log.timestamp.strftime("%Y-%m-%d-%H")
            if log_id in self.db.time_storage[time_key]:
                self.db.time_storage[time_key].remove(log_id)
                if not self.db.time_storage[time_key]:
                    del self.db.time_storage[time_key]

            if log_id in self.db.level_storage[log.log_level]:
                self.db.level_storage[log.log_level].remove(log_id)
                if not self.db.level_storage[log.log_level]:
                    del self.db.level_storage[log.log_level]

            if log_id in self.db.source_storage[log.log_source]:
                self.db.source_storage[log.log_source].remove(log_id)
                if not self.db.source_storage[log.log_source]:
                    del self.db.source_storage[log.log_source]

# Example Usage
if __name__ == "__main__":
    log_service = LogService()

    # Add logs
    log1 = log_service.add_log("System initialized", LogLevel.INFO, "System")
    log2 = log_service.add_log("User logged in", LogLevel.DEBUG, "AuthService")
    log3 = log_service.add_log("Database connection failed", LogLevel.ERROR, "DBService")

    print("All Logs:", log_service.db.logs)

    # Query logs by time range
    start_time = datetime.now(timezone.utc)
    log4 = log_service.add_log("Another log entry", LogLevel.INFO, "System")
    end_time = datetime.now(timezone.utc)

    time_range_logs = log_service.get_logs_by_time_range(start_time, end_time)
    print("Logs in time range:", time_range_logs)

    # Query logs by level
    error_logs = log_service.get_logs_by_log_level(LogLevel.ERROR)
    print("Error logs:", error_logs)
    error_logs = log_service.get_logs_by_log_level(LogLevel.DEBUG)
    print("DEBUG logs:", error_logs)
    error_logs = log_service.get_logs_by_log_level(LogLevel.INFO)
    print("INGO logs:", error_logs)


    # Query logs by source
    auth_logs = log_service.get_logs_by_log_source("AuthService")
    print("AuthService logs:", auth_logs)

    # Delete logs before a certain time
    log_service.delete_logs_before(start_time)
    print("Remaining logs:", log_service.db.logs)
