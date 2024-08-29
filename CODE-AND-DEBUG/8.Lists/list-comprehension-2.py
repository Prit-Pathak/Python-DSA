my_lst = [i for i in range(0, 12, 2)]
print(my_lst)

my_lst1 = [i for i in range(12) if i % 2 == 0]
print(my_lst1)


# for prime num
def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
        return True


my_lst2 = [i for i in range(2, 50) if is_prime(i)]
print(my_lst2)
