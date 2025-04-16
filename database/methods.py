from sqlalchemy import insert, select, update

from database.models.words import Words
from database.models.user import User
from database.db import session_maker

cat_rus = {'weather': 'Погода',
           'food': 'Еда',
           'family': 'Семья'}

async def create_word(cat, eng, rus):
    async with session_maker() as session:
        await session.execute(insert(Words).values(category=cat,
                                           word_eng=eng,
                                           word_rus=rus))
        await session.commit()


async def choose_category(cat):
    async with session_maker() as session:
        res = await session.scalars(select(Words).where(Words.category == cat_rus[cat]))
        return res.all()


async def select_user(tg_id):
    async with session_maker() as session:
        res = await session.scalar(select(User).where(User.tg_id == tg_id))
        return res


async def register_user(tg_id):
    async with session_maker() as session:
        res = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not res:
            await session.execute(insert(User).values(tg_id=tg_id, score=0))
            await session.commit()


async def new_score(tg_id, new):
    async with session_maker() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(score=User.score + new))
        await session.commit()
