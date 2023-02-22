# Подключаем библиотеки
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'keys.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API
spreadsheetId = '1VvrrbiLpZieQ_5nLawUV5224s4C14LjKq9xxNaGvq_A'
def write(chanel, crypto, tipe, side, start_price, end_price):
    f = open("last_index.txt", "r")
    last_index = int(f.readline())
    f.close()
    results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
        "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
        "data": [
            {"range": "Лист номер один!A"+str(last_index)+":F400100",
            "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
            "values": [
                        [chanel, crypto, tipe, side, start_price, end_price]  # Заполняем вторую строку
                    ]}
        ]
    }).execute()
    last_index += 1
    f = open("last_index.txt", "w")
    f.write(str(last_index))
    f.close()