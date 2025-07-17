# feature.py

def update_run_count():
    try:
        with open("run_count.txt", "r") as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0

    count += 1

    with open("run_count.txt", "w") as file:
        file.write(str(count))

    print(f"This project has been run {count} times.")

if __name__ == "__main__":
    update_run_count()
