li = ('Teclado', 249.99,
      'Mouse', 170.80,
      'Monitor', 949.99,
      'Playstation 5', 3400,
      'Fone', 95.50,
      'Mousepad',120)
i = 0
for i in range(0, len(li),2):
    no = li[i]
    pr = li[i + 1]
    print(f'{no:.<20}..........R${pr:.2f}')