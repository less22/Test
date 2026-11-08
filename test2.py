def reverse(x):
    return int(str(x)[::-1])
def main():
    x = int(input("Input number: "))
    print(reverse(x))
    
    
if __name__ == "__main__":
    main()