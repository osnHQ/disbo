import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class DisboBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix='!',
            intents=intents,
            help_command=None,
        )

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    async def on_member_join(self, member):
        developer_channel = discord.utils.get(member.guild.channels, name=os.getenv("DEVELOPER_CHANNEL"))

        if developer_channel:
            await developer_channel.send(f'Welcome {member.mention} to the \'{os.getenv("DEVELOPER_CHANNEL")}\' channel!')
            await developer_channel.send(f"{os.getenv('FIRST_CONTRIBUTION_MESSAGE')}")

        else:
            print("Test channel not found!")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = DisboBot()
bot.run(os.getenv("TOKEN"))
