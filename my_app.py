from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QTextEdit, QLineEdit
import json

app = QApplication([])
window = QWidget()

#Создание виджетов
list_countries = QListWidget()
text_countries = QTextEdit()
name_countries = QLineEdit()
name_countries.setPlaceholderText('BBeдитe cтpaнy...')
add_country_button = QPushButton('Добавить страну')
del_country_button = QPushButton('Удалить страну')
edit_country_button = QPushButton('Изменить страну')

#Создание лайуты
buttons_layout = QHBoxLayout()
right_layout = QVBoxLayout()
left_layout = QVBoxLayout()
main_layout = QHBoxLayout()

#Заполняем лайуты
buttons_layout.addWidget(add_country_button)
buttons_layout.addWidget(edit_country_button)
buttons_layout.addWidget(del_country_button)

right_layout.addWidget(text_countries)
right_layout.addWidget(name_countries)
right_layout.addLayout(buttons_layout)

left_layout.addWidget(list_countries)

main_layout.addLayout(left_layout, 3) 
main_layout.addLayout(right_layout, 7)

window.setLayout(main_layout)

window.resize(700, 500)
window.setWindowTitle('Информация про страны')
window.setStyleSheet('background-color: #00021f')
list_countries.setStyleSheet('border: 4px solid cyan; font-size: 22px; color: aqua; font-style: italic')
text_countries.setStyleSheet('border: 4px solid cyan; font-size: 22px; color: aqua; font-style: italic')
name_countries.setStyleSheet('border: 4px solid cyan; font-size: 16px; color: aqua; font-style: italic')
add_country_button.setStyleSheet('border: 4px solid cyan; font-size: 16px; color: aqua; font-style: italic')
del_country_button.setStyleSheet('border: 4px solid cyan; font-size: 16px; color: aqua; font-style: italic')
edit_country_button.setStyleSheet('border: 4px solid cyan; font-size: 16px; color: aqua; font-style: italic')

#Функциональная часть
def fill_countries():
    list_countries.clear()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
        for country in countries:
            list_countries.addItem(country)

def add_country():
    country = name_countries.text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    if not(country in countries):
        countries [country] = ''
    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(countries, file)
    fill_countries()

def del_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems()[0].text()
        with open('countries.json', 'r', encoding='utf-8') as file: 
            countries = json.load(file)
        del countries[country]
        with open('countries.json', 'w', encoding='utf-8') as file: 
            json.dump(countries, file)
        fill_countries()

def edit_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems() [0].text()
        text_country = text_countries.toPlainText()
        with open('countries.json', 'r', encoding='utf-8') as file:
            countries = json.load(file)
        countries[country] = text_country
        with open('countries.json', 'w', encoding='utf-8') as file:
            json.dump(countries, file)

def info_country():
    country = list_countries.selectedItems()[0].text()
    with open('countries.json', 'r', encoding='utf-8') as file: 
        countries = json.load(file)
    text_countries.setText(countries[country])

#countries = {
#    'Россия': '',
#    'Китай': ''
#}

#with open('countries.json', 'w', encoding='utf-8') as file:
#    json.dump(countries, file)

fill_countries()

# Обработчики событий

add_country_button.clicked.connect(add_country) 
del_country_button.clicked.connect(del_country) 
edit_country_button.clicked.connect(edit_country) 
list_countries.itemClicked.connect(info_country)

window.show()
app.exec()



