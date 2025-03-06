from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Router
from bot.buttons.reply import reply_button_builder
from bot.states import States
from dp.model import User
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from bot.middilwares import is_number,uzbekistan_viloyatlari
register=Router()





@register.message(F.text==__('Registration'))
async def register_handler(message:Message,state:FSMContext):
    user_id=message.chat.id
    await state.update_data(user_id=user_id)
    await state.set_state(States.username)
    await message.answer(text=_("Enter username:"))

@register.message(States.username)
async def username_handler(message:Message,state:FSMContext):
    username=message.text
    text=[_('🧑 Man'),_('👩‍🦰 Women')]
    await state.update_data(username=username)
    await state.set_state(States.gender)
    markup=reply_button_builder(text,(2,))
    await message.answer(text=_('Enter gender:'),reply_markup=markup)

@register.message(States.gender)
async def gender_handler(message:Message,state:FSMContext):
    gender=message.text
    await state.update_data(gender=gender)
    await state.set_state(States.password)
    await message.answer(text=_('Enter password:'))

@register.message(States.password)
async def password_handler(message:Message,state:FSMContext):
    password=message.text
    await state.update_data(password=password)
    await state.set_state(States.region)
    text = uzbekistan_viloyatlari
    markup = reply_button_builder(text, (2, 2, 2, 2, 2, 2))
    await message.answer(text=_('Enter city:'),reply_markup=markup)

@register.message(States.region)
async def city_handler(message:Message,state:FSMContext):
    texts=[_('◀️ Back'),_('💬 Chats')]
    city_id=is_number(message.text)
    print(city_id)
    await state.update_data(city_id=city_id)
    data =await state.get_data()
    markup=reply_button_builder(texts,(2,))
    users = {
        'user_id': data.get('user_id'),
        'username': data.get('username'),
        'password': data.get('password'),
        'gender': data.get('gender'),
        'city_id': data.get('city_id'),
    }
    check=User.check_user(users.get('user_id'))
    if not check:
        User.save(users)
    else:
        await message.answer(text=_('You are already registered'))
        return
    await state.clear()
    await message.answer(text=_('Data saved'),reply_markup=markup)






