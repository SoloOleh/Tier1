from queue import Queue

queue = Queue()
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    queue.put(f"Заявка {request_id}")
    print("Заявка додана")

def process_request():
    if not queue.empty():
        queue.get()
        print("Заявка оброблена")
    else:
        print("Черга пуста")

def main():
    while True:
        print("1. Створити нову заявку")
        print("2. Обробити заявку")
        print("3. Вийти")

        choice = input("Зробіть вибір: ")

        if choice == '1':
            generate_request()
        elif choice == '2':
            process_request()
        elif choice == '4':
            print(queue.queue)
        elif choice == '3':
            print("Завершення роботи програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()