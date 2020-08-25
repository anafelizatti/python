t1 = 0
t2 = 1
t3 = 0
c = 3
n1 = int(input("Digite quantos elementos você quer mostrar:\n->"))
print('{} -> {} ->'.format(t1, t2), end=' ')
while c <= n1:
    t3 = t1 + t2
    print('{} ->'.format(t3), end=' ')
    c += 1
    t1 = t2
    t2 = t3
    # andando com os valores
print("fim")
