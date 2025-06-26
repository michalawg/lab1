import os
import uuid

print("Witaja w aplikacji To-Do")


def main():
    while True:
        try:
            print('== TODO LIST ==\n[1] show tasks\n[2] add task\n[3] complete task\n[4] exit')
            choice = int(input('Your choice: ').strip())
            if choice == 1:
                nowe.show_tasks()
            elif choice == 2:
                nowe.add_task()
            elif choice == 3:
                nowe.complete_task()
            elif choice == 4:
                break
            else:
                print('Incorrect value')
        except Exception as e:
            print('Exception occurred: ', e)


class TASKS:
    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku
        if not os.path.exists(self.nazwa_pliku):
            nowy = open(self.nazwa_pliku, 'w')
            nowy.close()

    def show_tasks(self):
        print('\n[YOUR TASKS]')
        stream = open(self.nazwa_pliku)
        if len(stream.read()) < 1:
            print('Lista zadań jest pusta\n')
            stream.close()
        else:
            stream.seek(0)
            print(stream.read())
            stream.close()

    def add_task(self):
        try:
            print('\n[ADD TASK]')
            task_name = input('What is the task? ').strip()
            deadline = input('What is the deadline? ').strip()
            new_id = str(uuid.uuid4())
            new_task = ' | '.join([new_id, task_name, deadline])
            with open(self.nazwa_pliku, 'a') as my_file:
                my_file.write(new_task + '\n')
                # my_file.seek(0)
                # print(my_file.readlines())
            print()
            print("Zadanie zostało dodane pomyślnie.\n")

        except Exception as e:
            print('error occurred: ', e)

    def complete_task(self):
        try:
            TASKS.show_tasks(self)
            print('----------------')
            completed = input('Enter id to complete: ').strip()
            with open(self.nazwa_pliku) as stream:
                lines = stream.readlines()
                new_lines = [line for line in lines if line.split(' | ')[0].strip() != completed]

            if len(lines) == len(new_lines):
                print(f'Id, które podałeś: {completed}, nie istnieje\n')
            else:
                with open(self.nazwa_pliku, 'w') as stream:
                    stream.writelines(new_lines)
                    print()

        except Exception as e:
            print('error occurred: ', e)


nowe = TASKS('xwaz.txt')
main()
