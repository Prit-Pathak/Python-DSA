# keyword argument
def marks(m1, m2, m3, m4, m5):
    print(m1, m2, m3, m4, m5)
    total = m1 + m2 + m3 + m4 + m5

    percentage = total / 5

    print(f"total: {total} and percentage: {percentage}")


marks(m2=66, m3=44, m1=90, m4=88, m5=45)

print()
