import sys # to use sys.exit(). More on this later.

# Global
secret_n = 2

def guessing_game():
    in_n = int(input("guess an integer: "))
    if in_n == secret_n:
        print("You Win!")
        sys.exit()
    else:
      print("Try again")
    in_n = int(input("guess an integer: "))
    if in_n == secret_n:
        print("You Win!")
        sys.exit()
    else:
      print("Try again")
    in_n = int(input("guess an integer: "))
    if in_n == secret_n:
        print("You Win!")
        sys.exit()
    else:
      print("Try again")

def main():
    guessing_game()
    print("Done")

if __name__ == "__main__":
    main()
