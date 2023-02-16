from aiogram.dispatcher.filters.state import StatesGroup, State


class AbibasForm(StatesGroup):
    re_evaluation = State()
    stock = State()
