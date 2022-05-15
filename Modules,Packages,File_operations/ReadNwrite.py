#%%
text=open('new.txt', 'r+')
text.write('Hello file')
for i in range(0, 11):
    text.write(str(i))
print(text.seek(2))


#%%
#file operations Read & Write
text=open('sampletxt.txt', 'r')
text= text.read()
print(text)
text=text.split(' ')
print(text)
