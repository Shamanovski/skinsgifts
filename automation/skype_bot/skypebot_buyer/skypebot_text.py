WRONG_PROFILE_LINK = ('Неверно задана ссылка на стим профиль. Пример: http://steamcommunity.com/id/shamanovsky/, '
'либо http://steamcommunity.com/profiles/76561198177211015/')

WRONG_PROFILE_ID = 'Неверно задан id стим профиля. Пример: 76561198177211015 или shamanovsky'

NO_PROFILE_LINK = ('Какой у тебя Steam профиль?. Пожалуйста, укажи его. Пример: http://steamcommunity.com/id/shamanovsky/, '
'либо http://steamcommunity.com/profiles/76561198177211015/')

WRONG_NUMBER = 'Неверно задан номер кошелька. Примеры: -purse +79288987371 -purse R394380159465 -purse Z379170664340'

PROFILE_NOT_FOUND = 'Не удалось найти id или имя вашего профиля в базе данных Steam. Проверьте правильность введенных данных.'

OFFER_SCAM = ('Похоже, что вы положили в обмен вещи бота. '
'Введите -sell чтобы попробовать еще раз.')

NO_ITEMS = 'В вашем оффере не обнаружено каких-либо вещей.'

LOW_VALUE = ('Цена твоих вещей на торг. площадке Steam не превышает 500 рублей. '
'Если ты готов провести процесс продажи снова, введи -sell')

GREETING = '''Добрый день, {0}!
Данные будут сохранены в моей базе данных чтобы тебе не приходилось вводить одно и тоже.
Если какая-то информация изменится, ты всегда сможешь внести поправку.

Чтобы совершить первую продажу, пожалуйста, введи данные двумя сообщениями следующим образом:
- Ссылка на твой steam профиль с помощью команды -profile
Примеры: -profile http://steamcommunity.com/id/shamanovsky/ либо -profile http://steamcommunity.com/profiles/76561198177211015/
Для точного соответствия просто скопируй ссылку со своего веб браузера.
Также ты можешь указать идентификатор в голом виде без какой-либо ссылки. Примеры: -profile shamanovsky либо -profile 76561198177211015
- Укажи свой номер QIWI (со знаком + в начале) или номер кошелька Webmoney. Для ввода номера кошелька используй команду -purse.
Примеры: -purse +79288987371 -purse R394380159465 -purse Z379170664340

После ввода своего профиля стим ты сразу же можешь узнать сколько я готов предложить за все твои вещи по отдельности.
Для этого введи команду -rate

Если данные введены, введи -data чтобы подтвердить их и получить ссылку на оффер бота.
Отправь вещи боту и введи -sell, чтобы я назвал тебе цену за предметы.
Если ты согласен, введи -accept; если нет, то -decline
-accept - я приму оффер, отправленный тобою, и совершу мнговенную оплату.
-decline - я отклоню оффер.

Если ты забудешь какую-то команду, введи -help

Примечания:
* Методы оплаты: QIWI, Webmoney (WMR, WMZ).
* Общая стоимость вещей не должна быть ниже 500 рублей
* За вещи, с низким количеством продаж в день на торговой площадке Steam, будет предложена цена относительно самой высокой ставки на торг.площадке. Обычно это сувенирные оружия, непопулярные ножи и т.п.'''

HELP = '''Список команд:

-rate - получить оценку всех вещей CS:GO в инвентаре (для этого Steam профиль должен быть указан)

-profile ваша_ссылка_на_steam_профиль - указать свою ссылку на steam профиль
Примеры:
-profile shamanovsky
-profile 76561198177211015
-profile http://steamcommunity.com/id/shamanovsky/
-profile http://steamcommunity.com/profiles/76561198177211015/

-purse ваш_кошелек - указать ваш кошелек QIWI (со знаком "+" в начале) либо Webmoney
Примеры:
-purse +79288987371
-purse R399262875875
-purse Z379170664340

-data - узнать свои данные, подтвердить данные и получить ссылку на оффер бота
-sell - подтвердить отправку скинов боту и получить цену за них
-accept - согласиться с ценой и получить мгновенную оплату
-decline - отказаться от сделки (ваш оффер будет отклонен ботом)
-balance - узнать доступный баланс'''

NOT_FOUND = ('К сожалению, я не смог определить твои данные. Введи -help, чтобы получить повторную инструкцию. '
'Если ты считаешь, что ввел данные правильно, то отпиши мне об этом в skype shamanovskyi')

UNKNOWN_COMMAND = 'Введи -help для получения списка команд'

NO_PURSE = 'Вы не указали кошелек. Укажите ваш QIWI (со знаком + в начале) или Webmoney WMR кошелек командой -purse ваш_кошелек (ВВОД -purse ПЕРЕД НОМЕРОМ КОШЕЛЬКА ОБЯЗАТЕЛЕН)'

NO_PROFILE = 'Вы не указали вашу ссылку на steam профиль. Укажите ее командой -profile ваш_профиль (ВВОД -profile ПЕРЕД ССЫЛКОЙ НА ПРОФИЛЬ ОБЯЗАТЕЛЕН)'

CLIENT_DATA = '''Твой Steam профиль: {0}
Твой кошелек: {1}
Если ты хочешь что-то изменить, используй команды:
-profile твой_профиль
-purse твой_кошелек
Ссылка для отправки вещей боту: {2}

Пожалуйста, введи для начала -rate, чтобы получить оценку всех твоих вещей в инвентаре и узнать резервы моих кошельков.
Если данные указаны верно, введи -sell, перед этим отправив скины боту. Я назову цену за них.'''

OFFERED_PRICE = '''Если вы считаете, что бот предложил вам менее 72% от средней цены ваших вещей, то пожалуйста отпишите мне об этом в skype (shamanovskyi), чтобы я оценил ваш инвенитарь по Steam Tools.

Я готов купить твои вещи по цене: {0}₽ рублей ({1}$ долларов).
Вот результат оценки каждого скина по отдельности: {2}

Согласен? Введи -accept; если нет, то -decline'''

DECLINE = ('Твой оффер был отклонен. Возможно, ты обратишься ко мне позже. '
'Любые пожелания можно оставить здесь http://youhack.ru/showthread.php?t=604362')

OFFER_ERROR = ('Steam ответил ошибкой во время принятия оффера. '
'Введи -accept чтобы попробовать снова.')

NO_OFFER = 'Не могу найти какие-либо исходящие офферы от твоего Steam аккаунта.'

MULTIPLE_OFFERS = ('Похоже, что вы отправили боту более одного оффера. Пожалуйста, отмените все офферы за исключением одного. '
'Введите -sell чтобы попробовать еще раз.')

OVERLOADED = ('Инвентарь бота переполнен. Пожалуйста, отправьте количество вещей которое меньше разницы между 1000 '
'и нынешним количеством вещей в инвентаре бота.')

MANY_BOXES = ('В вашем оффере слишком много дешевых ящиков. Бот приинмает их не более 30 штук. '
'Пожалуйста, уберите лишние ящики и заново отправьте обмен.')

OFFER_NEWPRICE = ('Для оплаты ваших вещей недостает не более 3% от имеющихся средств. Вам будет выплачено: {} рублей.\n'
'Если вы согласны, введите -accept; если нет, то -decline')

INSUFFICIENT_FUNDS = ('Недостаточно средств для оплаты твоих вещей. Баланс на данный момент: {} рублей. '
'Проверить резервы всех кошельков всегда можно командой -balance')

CONFIRM_PAYMENT = ('Оплата успешно произведена. Благодарю за продажу! '
'Если тебе понравился мой сервис, то оставь пожалуйста отзыв здесь '
'http://youhack.ru/showthread.php?t=604362')

PAYMENT_FAILED = ('Произошла ошибка. Мне не удалось отправить средства. '
				  'Обратись ко мне в skype shamanovskyi, чтобы я совершил выплату вручную. Извиняюсь за неудобства :(')

PAYMENT_ERROR = ('Произошла ошибка при отправке денежных средств. Ошибка платежной системы: {}. '
'Обратись ко мне в skype shamanovskyi, чтобы я совершил выплату вручную.')

ITEMS_NOPRICE = ('Не удалось определить цену следующих вещей: {}.\nЛибо они не продаются на торг.площадке, '
                 'либо они были созданы недавно и цены на них пока что отсутствуют в моей базе данных.\n'
				 'Ты можешь попытаться совершить продажу без них, отправив повторный оффер.')

WRONG_ITEM = 'В вашем оффере обнаружены вещи, не являющимися скинами CS:GO. Пожалуйста, отправьте новый оффер без них.'

ERROR_ELEVEN = ('Стим ответил ошибкой с кодом 11 во время принятия оффера. Обратись ко мне в skype shamanovskyi, '
                'если твой обмен был принят')

ERROR_TWO = ('Стим ответил ошибкой с кодом 2 во время принятия оффера. Введи -accept, чтобы попробовать еще раз.'
             'Обратись ко мне в skype shamanovskyi, если твой обмен был принят')

RATE_ERROR = ('Не удается получить информацию о твоем инвентаре.\nВозможные проблемы:\n1. Ты его скрыл\n'
'2. В твоем инвентаре нет вещей CS:GO\n3. Steam сервер не отвечает.')

RATE_RESULT = ('Я оцениваю твой CS:GO инвентарь общей стоимостью в {0}₽ рублей ({1}$ долларов). '
               'Вот результат оценки каждого скина по отдельности: {2}')

UNPOPULAR_ITEMS_OFFERED = ('В твоем оффере я обнаружил вещи с низким количеством продаж на торг.площадке Steam: {}\n'
'Пожалуйста, отправь мне вещи без них')

UNPOPULAR_ITEMS_WARNING = 'Внимание! Эти вещи не будут приняты мною из-за слишком низкого количества продаж на торг. площадке: {}'

QIWI_WALLET_NOT_FOUND = 'Не удалось определить резерв кошелька QIWI. Попробуй чуть позже еще раз.'
