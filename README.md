##ТЗ на программу «Квазиреальный эксперимент»

1. Программа должна содержать 9 вкладок:
  *  Задание входного сигнала
  *  Вычисление Фурье-образа входного сигнала
  *  Задание аппаратной функции
  *  Вычисление Фурье-образа аппаратной функции
  *  Вычисление выходного сигнала при отсутствии в системе шумов
  *  Генерация шумов с пуассоновским распределением
  *  Спектральные распределения сигнала и шума
  *  Определение минимально возможных ошибок восстановления на основании информационного подхода
  *  Реконструкция входного сигнала по выходному методом регуляризации Тихонова
2. Вкладка «Задание входного сигнала»:
  *  Входной сигнал по умолчанию задаётся формулой 0.8*[exp^(-x^p)+ exp(-(x+3.5)^p) + exp(-(x-3.5)^p) + exp(-(x+7)^p) + exp(-(x-7)^p)]+0.2, соответствующей 5 штрихам миры и изображается в окне в виде непрерывного графика, значения по оси x – от -10 до 10, по y – от 0 до 1.2
  *  Пользователем задаются следующие параметры:
  *  Количество штрихов миры (в формулу добавляются слагаемые exp(-(x+3.5^n)^p) + exp(-(x-3.5^n)^p)
  *  Параметр масштабирования p (пробегает значения 2, 4, 8, 16, 40)
  *  Длина реализации X (по умолчанию принимает значение 20 (от -10 до 10), величина неотрицательная – ограничение)
  *  Число отсчётов по шкале функции L (пробегает значения 256, 1024, 4096)
  *  Кнопка «Вычислить», применяющая указанные пользователем параметры при нажатии на неё и вывод полученного дискретизированного сигнала (шкала x – от 0 до m-1, шкала y – произведение значений, полученных в результате построения графика входного сигнала, и L) 
  *  Вычисление количества информации, содержащейся в сигнале (формулу нужно проверить)
3. Вкладка «Вычисление Фурье-образа входного сигнала»
  *  Вычисление Фурье-образа (FFT) при нажатии на кнопку «Вычислить» 
  *  Подавление частот в Фурье-образе (зануление) при нажатии на кнопку «Подавить»; пользователь выбирает диапазон частот, ограничения – неотрицательные значения
  *  Вычисление обратного преобразования Фурье для просмотра полученного после подавления частот сигнала (ещё одна кнопка «Вычислить»)
  *  Вычисление количества информации, содержащейся в модифицированном входном сигнале
4. Вкладка «Задание аппаратной функции»
  *  Задание полуширины аппаратной функции β
  *  Привязка количества точек к количеству точек во входном сигнале (m штук)
  *  Изображение дискретных значений аппаратной функции (нормирование на 1?)
5. Вкладка «Вычисление Фурье-образа аппаратной функции»
  *  Применение FFT к вектору из m значений, полученных на предыдущем шаге
  *  Вывод результат на график, масштабирование
6. Вкладка «Вычисление Фурье-образа выходного сигнала при отсутствии в системе шумов»
  *  Реализовать двумя способами и сравнить результаты: 
        1.  выполнить свёртку вектора из m значений входного сигнала с вектором из m значений аппаратной функции
        2.  провести операцию свёртки значений Фурье-образа входного сигнала с Фурье-образом аппаратной функции
  *  Вывести графический результат при нажатии на кнопку «Выполнить» (для Фурье-образов – с предварительным применением обратного преобразования Фурье; можно посмотреть, что получится в Фурье-пространстве без применения обратного FFT)
7. Вкладка «Генерация шумов с пуассоновским распределением»
  *  Разыграть случайную величину с пуассоновским распределением (дисперсия задаётся пользователем)
  *  Вычислить значения «наигранного» шума, перемножив вектор случайных величин (m штук – по количеству значений вектора входных данных) и вектор sqrt(выходных данных) почленно
  *  Сложение почленно вектора выходных данных с вектором полученных значений шума
  *  Вычисление среднего значения выходного сигнала
  *  Вывод значения соотношения «сигнал/шум» (среднее значение вектора выходных данных/дисперсию шума)
  *  Вывод результирующего графика: выходное изображение + шум – по оси y, число отсчётов (m) – по оси x
  *  Вся последовательность описанных выше действий происходит при нажатии кнопки «Вычислить» 
8. Вкладка «Спектральные распределения сигнала и шума»
  *  Отображение на одном поле Фурье-образов сигнала и шума при нажатии кнопки «Вычислить»:
  *  Масштабирование как по оси x, так и по оси y
  *  Просмотр значений по шкале частот: двигаешься вдоль кривой – отображается значение частоты
9. Вкладка «Определение минимально возможных ошибок восстановления на основании информационного подхода»
  *  Вводится критическая частота (в перспективе – можно состыковать с предыдущим шагом, когда это значение выбирается при нажатии графика, и вычисление всех ниже описанных параметров происходит автоматически)
  *  Вычисляются параметры:
        1.  коэффициент потери мощности по Шеннону
        2.  отношение «сигнал/шум» (или «шум/сигнал»)
        3.  значение функции Q, характеризующей потери информации
        4.  минимально возможная ошибка восстановления входного сигнала
        5.  количество информации, содержащейся в выходном сигнале
10. Вкладка «Реконструкция входного сигнала по выходному методом регуляризации Тихонова»
  *  Вывод на одном графике результатов реконструкции входного изображения и самого входного изображения
  *  Поле для задания коэффициента регуляризации, по которому и выстраивается модель восстановленного сигнала
  *  График зависимости абсолютной ошибки восстановления от коэффициента регуляризации (в перспективе – график зависимости количества информации, содержащейся в сигнале, от коэффициента регуляризации)
  *  Таблица с данными, по которым строится график (3 столбца: коэффициент регуляризации, абсолютная ошибка восстановления, относительная ошибка восстановления)

##ТЗ на программу «Восстановление исходных изображений, полученных при работе с ЭОП»

1. Программа должна содержать 7 вкладок:
  *  Выходной сигнал
  *  Задание аппаратной функции
  *  Вычисление Фурье-образа аппаратной функции
  *  Генерация шумов с пуассоновским распределением
  *  Спектральные распределения сигнала и шума
  *  Определение минимально возможных ошибок восстановления на основании информационного подхода
  *  Реконструкция входного сигнала по выходному методом регуляризации Тихонова
2. Вкладка «Выходной сигнал»:
  *  Загрузка файла в формате CSV
  *  Функция обрезки лишних значений – до кратного степени 2 (возможно, не потребуется – нужно посмотреть, как себя ведёт FFT в Python’е)
  *  Графическое отображение миры
  *  Вычисление количества информации, содержащейся в сигнале 
3. Вкладка «Задание аппаратной функции»
  *  Задание полуширины аппаратной функции β
  *  Привязка количества точек к количеству точек во входном сигнале (m штук)
  *  Изображение дискретных значений аппаратной функции
4. Вкладка «Вычисление Фурье-образа аппаратной функции»
  *  Применение FFT к вектору из m значений, полученных на предыдущем шаге
  *  Вывод результат на график, масштабирование
5. Вкладка «Генерация шумов с пуассоновским распределением»
  *  Способы «наигрывания» шумов и их реализацию - найти
  *  Вычисление среднего значения выходного сигнала
  *  Вывод значения соотношения «сигнал/шум» (среднее значение вектора выходных данных/дисперсию шума)
  *  Вывод графика шума (количество отсчётов?)
6. Вкладка «Спектральные распределения сигнала и шума»
  *  Отображение на одном поле Фурье-образов сигнала и шума при нажатии кнопки «Вычислить»:
  *  Масштабирование как по оси x, так и по оси y
  *  Просмотр значений по шкале частот: двигаешься вдоль кривой – отображается значение частоты
7. Вкладка «Определение минимально возможных ошибок восстановления на основании информационного подхода»
  *  Вводится критическая частота (в перспективе – можно состыковать с предыдущим шагом, когда это значение выбирается при нажатии графика, и вычисление всех ниже описанных параметров происходит автоматически)
  *  Вычисляются параметры:
        1.  коэффициент потери мощности по Шеннону
        2.  отношение «сигнал/шум» (или «шум/сигнал»)
        3.  значение функции Q, характеризующей потери информации
        4.  минимально возможная ошибка восстановления входного сигнала
        5.  количество информации, содержащейся в выходном сигнале
8. Вкладка «Реконструкция входного сигнала по выходному методом регуляризации Тихонова»
  *  Вывод на одном графике результатов реконструкции входного изображения и самого входного изображения
  *  Поле для задания коэффициента регуляризации, по которому и выстраивается модель восстановленного сигнала
  *  График зависимости абсолютной ошибки восстановления от коэффициента регуляризации (в перспективе – график зависимости количества информации, содержащейся в сигнале, от коэффициента регуляризации)
  *  Таблица с данными, по которым строится график (3 столбца: коэффициент регуляризации, абсолютная ошибка восстановления, относительная ошибка восстановления)