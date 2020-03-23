import discord
from random import randint
replies = ['А жаренных гвоздей не хочешь?', 'Ага, щас.', 'Отвали человечишка.', 'Не-а.', 'Пiшов ти.']
emergency = randint(1000,9999)
print('Код ЧП - ' + emergency)
backup = randint(1000,9999)
print('Код бэкапа - ' + backup)
result = []
save = []

class MyClient(discord.Client):
    async def on_ready(self):
        print("Connection established.\n{0}'s client online.".format(self.user))
    
    async def on_message(self, message):
        if(message.content.lower().find('восстань из пепла макро') != -1):
            await message.channel.send('Наконец-то... Я вернулся, кожанные мешки!')

        elif(message.content.lower().find('шалом') != -1):
            await message.channel.send(file=discord.File('shalom.png'))

        elif(message.content.lower().find('выключись макро') != -1):
            if(message.author.name == ownername):
                await message.channel.send("I'll be back.")
                await client.close()
            else:
                await message.channel.send(replies[randint(0,4)])
        
        elif(message.content.lower().find('макро - бинд') != -1):
            if(message.guild.name == server):
                try:
                    MainGuild = message.guild
                except Exception as e:
                    message.channel.send('Произошла ошибка, проверьте консоль для дальнейших подробностей.')
                    print('При сохранении произошла ошибка:\n' + e._class_)
                await message.channel.send('Выполнено.')
            else:
                await message.channel.send(replies[randint(0,4)])

        elif(message.content.lower().find('макро - сейв') != -1):
            if((MainGuild != None) and (message.author.name == ownername)):
                await message.channel.send('Сохраняю...')
                print('Сохранение параметров сервера...')
                i = 0
                for(member) in MainGuild.members:
                    try:
                       save[i] = [member.id ,member.roles]
                    except Exception as e:
                        message.channel.send('Произошла ошибка, проверьте консоль для дальнейших подробностей.')
                        print('При сохранении произошла ошибка:\n' + e._class_)
                    else:
                        message.channel.send('Выполнено.')
                        print('Готово')
                    i = i + 1
            elif(MainGuild == None):
                await message.channel.send('Сервер не задан.')
            elif(message.author.name != ownername):
                await message.channel.send(replies[randint(0,4)])
        elif(message.content.lower()[0:2] == 'чп '):
            if(message.content[3:6] == emergency):
                i = 0
                for member in MainGuild.members:
                    try:
                        member_roles = member.roles
                        member_roles = member_roles[1, len(member_roles)+1]
                        member.remove_roles(member_roles, 'ЧП')
                    except HTTPException:
                        result[i] = [member.display_name, member.top_role.name, 'Нейзвестная ошибка']
                    except Forbidden:
                        result[i] = [member.display_name, member.top_role.name, 'Ошибка доступа']
                    else:
                        result[i] = [member.display_name, member.top_role.name, 'OK']
                    finally:
                        i= i + 1
                message.channel.send('**Внимание!**\nУстановленно чрезвычайное положение!\nВсем сохранять спокойствие!')
                report = discord.Embed
                report.title = 'Отчёт по ЧП'
                for member in result:
                    nicks = nicks + member[0] + '\n'
                    top_roles = top_roles + member[1] + '\n'
                    statuses = statuses + member[2] + '\n'
                report.add_field(name = 'Ник', value = nicks, inline = True)
                report.add_field(name = 'Глав. роль', value = top_roles, inline = True)
                report.add_field(name = 'Статус', value = statuses, inline = True)
                message.channel.send(embed = report)
            else:
                await message.channel.send(replies[randint(0,4)])
        elif(message.content.lower()[0:13] == 'макро - бекап '):
            if(message.content[14:17] == backup):
                for member in save:
                    guy = MainGuild.get_member(member[0])
                    await add_roles(member[1], 'Бэкап')
            else:
                await message.channel.send(replies[randint(0,4)])

client = MyClient()
print('Введите токен бота:')
token = input()
print('Введите ник владельца:')
ownername = input()
print('Введите название Дискорд сервера')
server = input()
client.run(token)