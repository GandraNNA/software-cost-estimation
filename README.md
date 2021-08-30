### Оценка трудомкости проекта 

Методы: 
- PERT, 
- FPA IFPUG,
- COCOMO II

Формочки отрисованы через Qt Designer
Используемая библиотека для работы с ui: PyQt5

## PERT
Тремя оценками можно описать диапазон неопределенности:
- Mi — наиболее вероятная оценка трудозатрат;
- Oi — минимально возможные трудозатраты на реализацию пакета работ. Ни один риск не реализовался. Быстрее не сделать. Возможность укладывания в эти затраты, равна 0;
- Pi — пессимистическая оценка трудозатрат. Все риски реализовались.

Оценка средней трудоемкости по каждому элементарному пакету считается по формуле:
![изображение](https://user-images.githubusercontent.com/36998396/131418739-cf8c55ce-4112-4b6d-a319-b52222a2aa39.png)

Среднеквадратичное отклонение считается по формуле:
![изображение](https://user-images.githubusercontent.com/36998396/131418783-3d1538ef-d4fb-47b5-a99d-4d4c0c4a9fdb.png)

При не испорченных (к примеру, излишним оптимизмом) оценках - оценки трудоемкости элементарных пакетов работ статистически независимы, а суммарная трудоёмкость проекта высчитывается в соответствии с центральной предельной теоремой вероятностей:
![изображение](https://user-images.githubusercontent.com/36998396/131418840-1aa6e928-42f3-40b1-988d-d47e67883839.png)

Среднеквадратичное отклонение для оценки суммарной трудоемкости высчитывается по формуле:
![изображение](https://user-images.githubusercontent.com/36998396/131418898-81943cd0-5077-48a4-9ca5-db3d9cb06330.png)

Для оценки суммарной трудоемкости проекта, которая не превысится с вероятностью 95%, применяется формула:
![изображение](https://user-images.githubusercontent.com/36998396/131419025-8fdf5d13-c7a2-41f2-b4fc-697b81f82347.png)

Соответственно,  проект превысит данную оценку трудоемкостис вероятностью всего 5%, что означает, что оценку можно считать приемлемой. Под ней вполне может расписаться профессиональный менеджер. Список элементарных пакетов работ, который используется при оценке трудоемкости, обычно берется из нижнего уровня иерархической структуры работ проекта. Однако возможно использование накопленного опыта аналогичных разработок.
Суммарная трудоёмкость проекта в итоге будет равна:
![изображение](https://user-images.githubusercontent.com/36998396/131419055-fae98273-cd84-4008-8855-08e662a8ee5d.png)
                                                                                                  
Если сотрудник занимается только одним проектом, это обычно не означает, что он все 40 часов в неделю будет тратить на проектные работы. 	Приблизительно в месяц он будет заниматься проектом:
![изображение](https://user-images.githubusercontent.com/36998396/131419120-11d69d82-3d94-4bab-bc4c-03e085f80bf8.png)
                                       
А оптимальная продолжительность проекта, согласно формуле Б. Боэма, составит:
![изображение](https://user-images.githubusercontent.com/36998396/131419159-7e617548-dd42-4df4-abd0-af55922375e1.png)
