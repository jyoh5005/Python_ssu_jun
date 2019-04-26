customer = ['Jane','Mark','Tom','Amy','Bob']
def reverseList(aqument):
    result = []
    for i in range(len(aqument)):
        result.append(aqument[-1-i])
    return result

print(reverseList(customer))

customer = ['Jane','Mark','Tom','Amy','Bob']
customer.reverse()
print(customer)
