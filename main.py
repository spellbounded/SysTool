# AutoTracker version 0.0
# Author:  Bryan May
# AutoTracker is used to monitor system and network logs for an application or an entire system

import wmi

menu_items = ['Please select an option', '1. Show all processes', '2. Show running processes', '3. Show OS version',
              '4. List specific processes', '5. Show CPU Usage']


def show_all_services():
    f = wmi.WMI()

    print("PID    Processs Name")

    for process in f.Win32_Process():
        print(f"{process.ProcessID:<10} {process.Name}")


def show_running_services():
    f = wmi.WMI()

    print("PID    Processs Name")

    for process in f.Win32.Process():
        if process.status == 'running':
            print(f"{process.ProcessID:<10} {process.Name}")


def show_os_version():
    c = wmi.WMI()
    for os in c.Win32_OperatingSystem():
        print(os.caption)


def list_specific_processes(app):
    c = wmi.WMI()
    for process in c.Win32_process(name=app):
        print(process.ProcessID, process.Name)


def fix_app_input(app) -> object:
    # since we're expecting an application, we check the last 4 characters for ".exe"
    suffix = ".exe"
    file_type = app[-4:]
    if file_type != '.exe':
        app = app + suffix

    return app


def destroy_process(app):
    c = wmi.WMI()
    print("Action   PID   Process Name")
    for process in c.Win32_process(name=app):
        print("Deleted ", process.ProcessID, process.Name)
        process.Terminate()


def process_response():
    response = "nothing"
    while (response != 'Y') and (response != 'N'):
        response = input("Would you like to make another query? (Y or N)")

        if response != 'Y' and (response != 'N'):
            print(response, " Is not a valid response, please try again")

    return response


def show_menu():
    for string in menu_items:
        print(string)


def is_valid_selection(selection: int) -> bool:
    return selection in range(1, len(menu_items) + 1)


def get_response() -> str:
    while True:
        try:
            response = input('Please enter your selection')
            while not is_valid_selection(response):
                print('Please enter a valid response')
                response = input('Please enter your selection')
                return response
        except:
            print("that wasn't a valid selection...")


def show_cpu_usage():
    pass


options = {1: show_all_services,
           2: show_running_services,
           3: show_os_version(),
           4: list_specific_processes,
           5: show_cpu_usage()
           }


def init():
    show_menu()
    response = get_response()
    options[int(response)]()


# run this shit dawg
init()
