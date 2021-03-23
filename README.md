# Testnet
Тут содержится информация о будущих обновлниях (которые доступны пока только в тестовой сети)

IP: 172.104.243.180
Port: 9999
Explorer: 8008

# MJOB
Хотите получить несколько блоков за раз? В этом вам поможет команда MJOB. Предлагаю разобрать как она работает:

С -> MJOB,katant,2

S -> diff,block_hash_1:result_hash_1,block_hash_2:result_hash_2,block_hash_3:result_hash_3;

C -> result_1,result_2,result_3;

S -> GGB,0.1;

Сервер отпрвит блоки, которые разделены запятой, сами же хеши разделены двоеточием

В конце большинства команд есть ;, он позволяет понять серверу/клиенту что все данные уже пришли.

Так-же результат поможет понять какие блоки вы решили верно, а какие нет. Он по порядку отправит G (GOOD) и B (BAD), по которым уже и можно будет понять, какие решения были верными. В конце этого сообщения будет общая награда за блок (рандомная награда * количество верных решений)

Пример майнера на Python: https://github.com/MHCoinPublic/Testnet/blob/master/multiminer.py

Максимальное количество блоков сейчас 1000, оно может быть уменьшено и увеличено в будущем
