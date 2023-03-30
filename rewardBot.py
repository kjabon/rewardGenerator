import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand


API_TOKEN = 'Your_token_here' # You need to acquire a Telegram API token, and a bot with Telegram, e.g. using the "BotFather," 

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class RewardGenerator():
    def __init__(self):
        self.initReward = 0
        self.reward = self.initReward
        self.rewardInc = 1
        self.maxReward = 30

    def reset(self):
        self.reward = self.initReward
        return "Reset"

    def getAndInc(self):
        rng = random.uniform(0, 1)
        if rng > 1-self.pRewardInc:
            self.reward += self.rewardInc
            if self.reward > self.maxReward:
                self.reward = self.maxReward
        return "Reward: {}".format(self.reward)

rgen = RewardGenerator()


@dp.message_handler(commands='getreward')
async def start_cmd_handler(message: types.Message):
    reward = rgen.getAndInc()
    await message.reply(reward,reply=False)


@dp.message_handler(commands='reset')
async def start_cmd_handler(message: types.Message):
    m = rgen.reset()
    await message.reply(m,reply=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
