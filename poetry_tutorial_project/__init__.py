__version__ = '0.1.0'
import psutil
from datetime import datetime
from loguru import logger
from .util.size import get_size


def main():
    logger.info(system_boot_time())
    logger.info(system_cpu_usage())
    logger.info(system_virtual_mem_usage())
    logger.info(system_disk_usage())


def system_boot_time():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"


def system_cpu_usage():
    physical_cores = psutil.cpu_count(logical=False)
    total_cores = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent()
    return f'CPU: {cpu_usage}% utilized of {physical_cores} physical CPU cores ({total_cores} total).'


def system_virtual_mem_usage():
    svmem = psutil.virtual_memory()
    total_mem = get_size(svmem.total)
    available_mem = get_size(svmem.available)
    used_mem = get_size(svmem.used)
    pct_mem = svmem.percent
    return f'Virtual Memory: {pct_mem}% of {total_mem} total system memory available ({used_mem} used with {available_mem} remaining).'


def system_disk_usage():
    partition = psutil.disk_partitions()[0]
    partition_usage = psutil.disk_usage(partition.mountpoint)
    total_disk = get_size(partition_usage.total)
    free_disk = get_size(partition_usage.free)
    pct_disk = partition_usage.percent
    return f'Disk: {pct_disk}% used of {total_disk} total, with {free_disk} remaining.'
