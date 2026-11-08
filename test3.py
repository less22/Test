def reverse(x):
    return x if x < 10 else (x%10) * 10**(len(str(x))-1) + reverse(x // 10)
    
def main():
    print(reverse(123999))
    
    
if __name__ == "__main__":
    main()