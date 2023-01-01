# Подключаем библиотеки
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'keys.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API
spreadsheetId = '1VvrrbiLpZieQ_5nLawUV5224s4C14LjKq9xxNaGvq_A'
def write(crypto, usdt, busd, percent):
    f = open("last_index.txt", "r")
    last_index = int(f.readline())
    f.close()
    results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
        "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
        "data": [
            {"range": "Лист номер один!A"+str(last_index)+":D400100",
            "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
            "values": [
                        [crypto, usdt, busd, percent]  # Заполняем вторую строку
                    ]}
        ]
    }).execute()
    last_index += 1
    f = open("last_index.txt", "w")
    f.write(str(last_index))
    f.close()