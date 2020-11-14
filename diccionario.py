def count_words(lyric):
  
    lyric = lyric.replace(',','').lower()
    lyric = lyric.replace('!','')
    lyric = lyric.replace("'",'')
    lyric=lyric.split()
    
    my_dict = {}
    
    for id in lyric:
       if id in my_dict:
         my_dict[id]= my_dict.get(id) + 1
       else: 
         my_dict[id]=1
    
    print(my_dict)
    dict2={}
    words_count=my_dict
    i=0
    while i<3:
          more_repeat_word='none'
          more_repeat=0
          for words, counts in words_count.items() :
            if more_repeat<counts:
              more_repeat_word=words
              more_repeat=counts
            dict2[more_repeat_word]=words_count.get(more_repeat_word)
          i=i+1
    print(dict2)
lyric = '''
  Go, go, go, go
  Go, go, go, go
  Go, go, go, go
  Go!
  Baby shark, doo doo doo doo doo doo
  Baby shark, doo doo doo doo doo doo
  Baby shark, doo doo doo doo doo doo
  Baby shark!
  Mommy shark, doo doo doo doo doo doo
  Mommy shark, doo doo doo doo doo doo
  Mommy shark, doo doo doo doo doo doo
  Mommy shark!
  Daddy shark, doo doo doo doo doo doo
  Daddy shark, doo doo doo doo doo doo
  Daddy shark, doo doo doo doo doo doo
  Daddy shark!
  Grandma shark, doo doo doo doo doo doo
  Grandma shark, doo doo doo doo doo doo
  Grandma shark, doo doo doo doo doo doo
  Grandma shark!
  Grandpa shark, doo doo doo doo doo doo
  Grandpa shark, doo doo doo doo doo doo
  Grandpa shark, doo doo doo doo doo doo
  Grandpa shark!
  Let's go hunt, doo doo doo doo doo doo
  Let's go hunt, doo doo doo doo doo doo
  Let's go
'''

count_words(lyric)