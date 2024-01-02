#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
    tasks = [wait_random(max_delay) for task_delay in range(n)]
    completed, pending = await asyncio.wait(tasks)
    return [task.result() for task in completed]
