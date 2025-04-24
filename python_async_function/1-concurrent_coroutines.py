#!/usr/bin/env python3
import importlib.util
import asyncio
from typing import List


module_name = "wait_random"
file_path = "0-basic_async_syntax.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine qui exécute `wait_random` n fois de manière asynchrone
    et retourne
    la liste des délais obtenus, triée dans l'ordre croissant
    grâce à la concurrence.

    Parameters:
    n (int): Le nombre de tâches à exécuter.
    max_delay (int): La valeur maximale du délai pour chaque tâche.

    Returns:
    List[float]: Liste triée des délais retournés par chaque appel
    de `wait_random`.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
