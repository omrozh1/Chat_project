import time


def password(a):
    try:
        i = 0
        wait = 30

        while True:
            if i < 3:
                psw = input("Password: ")
                i = i + 1
                if psw == a:
                    break

                elif psw == "Cancel":
                    print("Cancelled")
                    exit(44)
            else:
                print(f"Wait for {wait} seconds")
                time.sleep(wait)
                wait = wait * 2
                i = 0

    except KeyboardInterrupt:
        print("")
        print("Cancelled")
        exit(44)
