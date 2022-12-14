# puzzle

Алгоритм нахождения решения игры пятнашки.

Результатом работы программы является дерево рассмотренных вариантов решения и выделенный правильный путь решения задачи. 
![изображение](https://user-images.githubusercontent.com/65676590/194096021-8d2d2fe1-a1ee-476d-ad77-9d2487d6862c.png)



Реализуется алгоритм A*

Агентом, который мы будем разрабатывать, выполняется поиск в пространстве состояний (пространстве всех возможных конфигураций игрового поля) с использованием информированного поиска A*. Поиск «информируется» при выборе следующего шага с учётом знаний предметной области, которые представлены значением функции, связанной с каждым состоянием задачи. Возможные состояния (вверх, вниз, влево и вправо) соответствуют направлениям перемещения пустой клетки:
![00405149ceed4163beb21dd18754fbe7](https://user-images.githubusercontent.com/65676590/194056352-535bb391-9349-4fac-ade0-090488acddb0.jpg)

Ключевой элемент A* находится в значении, которое присваивается каждому состоянию и даёт возможность резко сократить время на поиск целевого состояния из заданного начального состояния (рис. 6). Функция, которой выводится значение, привязанное к каждому состоянию s, раскладывается так:
f(s) = g(s) + h(s)
где g — это стоимость достижения s из начального состояния (число ходов от начального состояния до s), h — рациональный компонент агента (эвристика), позволяющий определять стоимость всех возможных путей, начинающихся в s

Подробнее про алгоритм можно почитать здесь
[ссылка](https://ru.wikipedia.org/wiki/A*)
