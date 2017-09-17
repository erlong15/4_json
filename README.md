# Prettify JSON

Чтение json из файла.  Вывод json в читаемом отформатированном  виду в консоль.

# Как запускать

Пример запуска и вывода
```
[lucky@lucky 4_json]$ python3 pprint_json.py alco_shops.json 
{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "properties": {
                "Attributes": {
                    "Address": "улица Академика Павлова, дом 10",
                    "AdmArea": "Западный административный округ",
                    "ClarificationOfWorkingHours": null,
                    "District": "район Кунцево",
                    "IsNetObject": "да",
                    "Name": "Ароматный Мир",
                    "OperatingCompany": "Ароматный Мир",
                    "PublicPhone": [
                        {
                            "PublicPhone": "(495) 777-51-95"
                        }
                    ],
                    "TypeService": "реализация продовольственных товаров",
                    "WorkingHours": [
                        {
                            "DayOfWeek": "понедельник",
                            "Hours": "09:30-22:30"
                        },
```

# Цель проекта

Тренировочный код для курса devman - [DEVMAN.org](https://devman.org)
