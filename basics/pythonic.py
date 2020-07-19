# Idiomatic Python code

# 1. Avoid comparing directly to `True`, `False`, or `None`

a = True
# อย่าหาทำ
if a is True:
    print('a is true')

# หาทำ
if a:
    print('a is true')   

# 2. Avoid repeating variable name in compound if statement

a = 1
# อย่าหาทำ
if a == 1 or a == 2 or a == 3 or a == 4:
    print('a: ', a)

# หาทำ
if a in [1, 2, 3, 4]:
    print('a: ', a)

# 3. 3. Use `in` to iterate over iterable

l = [1, 2, 3, 4]
for item in l:
    print(item)

# 4. Use default parameter of `dict.get`

a = {
    'name': 'toptoppy'
}
print(a['name'])

# อย่าหาทำ
if 'name' in a:
    print(a['name'])

# หาทำ
print(a.get('name', None))

# 5. Use `enumerate` function in loops

count = 1
names = ['a', 'b', 'c', 'd']
# อย่าหาทำ
for name in names:
    print(f'{count}. {name}')
    count += 1

# หาทำ
for name in enumerate(name):
    rint(f'{index + 1}. {name}')

# 6. Use `_` for data that should be ignored

for _, name in enumerate(name):
    rint(f'name: {name}')

# 7. Use (for) `else` after iterator is exhausted!

# อย่าหาทำ
check = False
for name in names:
    if name == 'toptoppy':
        check = True
        break

if check:
    print('Yes')

# หาทำ
for name in name:
    # Do something
    # ถ้าจบ loop ทำ else
else:
    print('Yes')

# 8. List comprehension to create a transformed list

# อย่าหาทำ
for i in range(10):
    name.append(i)

# หาทำ
name = [i for i in range(10)]

# 9. Use context manager to ensure resources are managed

# อย่าหาทำ
f = open('test')
# Do something
f.close()

# หาทำ
with open('test') as f:
    # Do something


# 10. Use generator to lazily load infinite sequences

