#Q.3
fruit_list = ['manga', 'melancia', 'banana', 'uva', 'seriguela']
candy_list = ['queijadinha', 'brownie', 'churros', 'beijinho', 'brigadeiro']
feijoada_list = ['feijao', 'carne', 'arroz', 'farofa', 'calabresa', 'bacon']

listona = [fruit_list, candy_list, feijoada_list]

print(listona[1][4])

listona[1].append('brigadeiro')
print(listona[1])

listona.append('bebidas')
print(listona)

#Q.4
del listona[:]
print(listona)