Необходимо разработать программу, которая умеет анализировать данные из трех разных источников.
На вход подаются 3 файла, которые содержат результаты тестирования.
Файл 1 и Файл 2 содержат логи выполнения тестов, а Файл 3 содержит проверки этих тестов.
Результатом работы программы должен быть JSON файл, являющийся результатом слияния трех файлов по общему ключу.
JSON файл, должен содержать массив объектов. В объекте должны быть следующие поля:

название теста
статус теста
ожидаемое значение проверки
реальное значение проверки

Файл 1
{
    "logs": [
        {
            "time": "946684810",
            "test": "Test output A",
            "output": "fail"
        }
    ]
}
Файл 2
{
    "suites": [
        {
            "name": "suite1",
            "tests": 1,
            "cases": [
                {
                    "name": "Test output B",
                    "errors": 0,
                    "time": "Saturday, 01-Jan-00 00:00:20 UTC"
                }
            ]
        }
    ]
}
Файл 3
{
    "captures": [
        {
            "expected": "B"
            "actual": "B",
            "time": "2000-01-01T00:00:20+00:00"
        },
        {
            "expected": "A"
            "actual": "B",
            "time": "2000-01-01T00:00:10+00:00"
        }
    ]
}
Усложнения:

Входные и выходные данные валидируются по JSON Schema
Решение покрыто автотестами
Решение задачи поставляется в виде Docker-образа