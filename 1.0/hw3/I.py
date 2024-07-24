n =  int(input())
res = []

m = int(input())    
langs = set()
all_langs = set()
for _ in range(m):
    lang = input()
    langs.add(lang)
    all_langs.add(lang)


for _ in range(1, n):
    tmp_langs = set()
    for _ in range(int(input())):
        lang = input()
        tmp_langs.add(lang)
        all_langs.add(lang)
        
    langs = langs.intersection(tmp_langs)
    
print(len(langs))
print(*langs, sep='\n')
print(len(all_langs))
print(*all_langs, sep='\n')

