# Graph_network
  Анализ социальных сетей – это процесс исследования различных систем с использованием теории сетей. 
  
  
  Cуществуют модели, которые оценивают вероятность сбоя программного обеспечения, некоторые из них рассматривают людей как источник для прогнозов – ведь именно люди разрабатывают и тестируют продукты до релиза. Их взаимодействия образуют сеть: можно представить разработчиков как узлы, а то, работали ли они вместе над одним и тем же файлом в рамках одного релиза, как рёбра сети. Понимание взаимодействий и информация о ранее произошедших сбоях позволит многое сказать о надёжности конечного продукта и укажет на файлы, в которых риск сбоя наиболее вероятен.
  
  
  Репозиторий состоит из 3 файлов с кодом, 3 изображений и одного датасета. email-Eu-core.txt - датасет переписки посредством электронной почты от крупного европейского университета, где содержится анонимная информация обо всех входящих и исходящих электронных сообщениях между членами исследовательского учреждения.
Датасет содержит файл формата txt, где на каждой строке перечисляются пары узлов, которые связаны друг с другом. В файлах с кодом изпользуются библиотеки networkx, предназначенная для работы с графами, библиотека matplotlib для визуализации и библиотека community для выделения сообществ внутри сети.
  
  
  В коде graph_visual.py мы последовательно выводит основные параметры графа: количество узлов, рёбер и среднее количество соседей у узлов в графе. Также проводим проверку на направленность и связность графа, сильная и слабая связность. А также визуализация самого графа в виде файла graph_visual.png:
            
            
            Количество вершин: 1005
            Количество рёбер: 25571
            Среднее количество соседей у узлов в графе: 25.4438
            Граф является направленным и состоит из нескольких компонент.
            Количество вершин: 986
            Количество рёбер: 25552
            Среднее количество соседей у узла в графе: 25.9148
            Количество вершин: 803
            Количество рёбер: 24729
            Среднее количество соседей у узла в графе: 30.7958 
            
  
  
  В коде graph_hist.py мы получаем распределение степеней в графе с информацией обо всех входящих и исходящих электронных сообщениях между членами исследовательского учреждения в виде гистограммы hist.png:
            
            
            Диаметр:  6
            Среднее расстояние в компоненте сильной связности:  2.5474824768713336
            Среднее расстояние в компоненте слабой связности:  2.164486568301397
  
  
  В коде graph_cluster.py мы получаем распределение участников по сообществам, где цвет узлов описывает принадлежность тому или иному сообществу. А также получаем:
            
            
            Кластеризация:  0.2328022090200813
            Кластерный коэффициент:  0.3905903756516427
            Количество центральных узлов:  46
            Количество узлов на периферии:  3
            Количество сообществ:  7
            Количество элементов в выделенных сообществах: 5, 5, 5, 5, 5, 5, 5
            
Подробности по ссылки: https://habr.com/ru/post/516514/  
  
