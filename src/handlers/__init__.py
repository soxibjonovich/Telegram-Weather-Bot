from src.handlers.user.default import main_router

from aiogram import Router
from typing import NoReturn, List

routers: List[Router] = [main_router]


def register_handlers(main_router: Router) -> NoReturn:
    for router in routers:
        main_router.include_router(router)
