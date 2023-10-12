'''
# Алгоритм Дейкстры
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# Поиск в ширину
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person +" is а mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
search("you")

# Пример кэширования
cache = {}
def get_page(url) :
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

# Хеш-таблицы
voted = {}
def check_voter(name):
    if voted.get(name):
        print ("kick them out!")
    else :
        voted[name] = True
        print ("let them vote!")

# Быстрая сортировка
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1 :] if i <= pivot]

        greater = [i for i in array [ 1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

# Рекурсия вызовом функции самой себя
def look_for_key(bох):
    for item in bох:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key!")

# Рекурсия с циклом while
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        bох = pile . grab_a_box()
        for item in bох:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")

# Бинарный поиск
def binary_search(list, item): # В переменньх low и high хранятся границы той части списка, в которой выпопняется поиск
    low = 0
    high = len(list)-1

    while low <= high:      # Пока эта часть не сократится до одного элемента...
        mid = (low + high)  # ...проверяем средний элемент
        guess = list[mid]
        if guess == item:   # Значение найдено
            return mid
        if guess > item:    # Много
            high = mid - 1
        else:               # Мало
            low = mid + 1
    return None             # Значения не существует


my_list = [1, 3, 5, 7, 9]   # А теперь протестируем функцию!

print(binary_search(my_list, 3))    # Вспомните: нумерация элементов начинается с О. Второй ячейке соответствует индекс 1
print(binary_search(my_list, -1))   # "None" в Python означает "ничто". Это признак того, что элемент не найден
'''