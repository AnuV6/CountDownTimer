import time

def check(password):
    for i in range(len(password)):
        if i >= len(SECRET) or password[i] != SECRET[i]:
            return False
        # Insecure timing: leaks length of correct prefix
        time.sleep(0.2)
    return len(password) == len(SECRET)

if __name__ == "__main__":
    print("This program checks a secret password, but it's not safe.")
    print("Hint: Look at the check() function carefully.")
    print("The flag is:", FLAG)
