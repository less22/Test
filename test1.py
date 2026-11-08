def reverse(x):
    rev = 0
    while x != 0:
        rev = rev*10 + x%10
        x = x//10
    return rev
def main():
    print(reverse(123))
    
if __name__ == "__main__":
    main()