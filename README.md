# lab8
Ответы на контрольные вопросы:
1. Дайте определение термину "внутренняя сортировка"?

-Внутренняя сортировка (англ. internal sort) — разновидность алгоритмов сортировки или их реализаций, при которой объема оперативной памяти достаточно для помещения в неё сортируемого массива данных с произвольным доступом к любой ячейке и, собственно, для выполнения алгоритма.

2. Перечислите методы сортировки, основанные на рекурсии?

-Сортировка слиянием
-Быстрая сортировка
-Сортировка выбором 

3. В чем суть метода Шелла?

-Суть метода Шелла в том, что он построен на основе метода вставки с минимизацией промежуточных шагов. Сначала выполняется сортировка элементов, отстоящих друг от друга на три позиции. После этого сортируются элементы, отстоящие друг от друга на две позиции. Наконец выполняется сортировка смежных элементов. 
Точная последовательность изменения приращений может изменяться. Единственным требованием остается равенство последнего приращения 1.

4. В чем суть шейкерной сортировки?

-Суть в том, что шейкерная сортировка (cocktail sort, shaker sort), или сортировка перемешиванием - усовершенствованная разновидность сортировки пузырьком, при которой сортировка производиться в двух направлениях, меняя направление при каждом проходе.

5. В чем суть метода простых вставок?

-Суть метода заключается в том, что из сортируемой последовательности выбирается и анализируется каждый элемент, который помещается «на свое место» в уже отсортированной части последовательности.

6. В чем суть метода простым выбором?

-Метод простого выбора. Метод заключается в последовательном нахождении минимального или максимального элемента (в зависимости от того сортируем ли мы массив по возрастанию или по убыванию) и перестановке его в начало или конец массива. 

7.В чем суть сортировки слиянием?

-Сортировка слиянием - это алгоритм, который используется для сортировки последовательности элементов. Сначала массив разделяется на несколько подгрупп меньшего размера. 
Сначала задача разбивается на несколько подзадач меньшего размера. Затем эти задачи решаются с помощью рекурсивного вызова или непосредственно, если их размер достаточно мал. Наконец, их решения комбинируются, и получается решение исходной задачи.

8.В чем суть быстрой сортировки?

-Быстрая сортировка (англ. quicksort), часто называемая qsort по имени реализации в стандартной библиотеке языка Си. Один из быстрых известных универсальных алгоритмов сортировки массивов (в среднем O(n log n) обменов при упорядочении n элементов), хотя и имеющий ряд недостатков. Он работает, выбирая «поворотный» элемент из массива и разделяя другие элементы на два подмассива, в зависимости от того, меньше они или больше, чем стержень. По этой причине ее иногда называют сортировкой обмена разделами. Затем подмассивы рекурсивно сортируются. Похож на сортировку слиянием, но принципы и ключевые моменты другие.  
