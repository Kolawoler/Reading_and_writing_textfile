#!/usr/bin/env python
# coding: utf-8

# In[1]:


#i am reading and writting to the object file, the object file has numerous methods like read, readlines,
#and also close file amng others


# In[94]:


with open('sample3.txt','r') as fr:
    with open('text_2.text','w') as fb:
        
    #fr_conc = fr.readlines()
    #fp = fr_conc[:4]
    #for j in fp:
     #   print(j,end = '')
    #print(type(fp))
    
       """in other words when printing the first few lines , its important we use class object
       method of readlines, as this return each  lines in list 
       and from there, each line corresponding to each first element of a list
       but remember this would return the last character of each line as a \n character, so u have 
       to remove that by looping for each elemt and setting every loop to end = ''"""
    
    """f_con = fr.readlines()
    print(f_con[-1])"""
    
        
    
    """when you are also accessing the first five few xters of the text file,then you use fr.read()
    and loop from then, if you set the same in readlines method,it doesnt accept that"""
    set_me = 10
    """fr_conc = fr.read(set_me)
    print(fr_conc,end = '')
    #for fj in fr_conc:
    #    print(fj,end='')"""
    fr_conc = fr.read(set_me)
    print(fr_conc)
    fr.seek(5)
    fr_conc = fr.read(set_me)
    print(fr_conc)
    #fr_conc = fr.read(set_me)
    #print(fr_conc)
   # print(fr.tell())
    #fr_conc = fr.read(set_me)
   # print(fr.tell())
    
    
    """fr_conc = fr.read(set_me)
    while len(fr_conc) > 0:
        print(fr_conc)
        fr_conc = fr.read(set_me)""" 


# In[4]:


with open('sample3.txt','r') as fb:
    with open('sample3.txt.copy','r') as kt:
        
        
        with open('sample3.txt.copy','w') as gb:
            
           # for line in fb:
                #gb.write(line)
        #print(kt.read())
            set_size = 10
            gimpy = fb.read(set_size)
            while len(gimpy)> 0:
                gb.write(gimpy)
                gimpy = fb.read(set_size)
                
        print(kt.read())            


# In[93]:



      #print(line_copy)
      #count = 0
      #for line in range(len(line_copy)):
       #   if line[i].endswith('at'):
       #       count = count + 1
             
        #  i = i + 1
      #print(line_copy[1].endswith('\n'))
  


# In[35]:


with open('sample3.txt.copy','r') as ft:
       """this helps to search for the a text in the text file and return
       the occurence of the text in the file-Second option"""
       list_3 = []
    
       read_lines_obj = ft.readlines()
       
       for i in range(len(read_lines_obj)):
           count = read_lines_obj[i].count('Quod')
           list_3.append(count)
           
            
   
       print(sum(list_3),list_3)        


# In[189]:


def  hash_display():
    """this helps to print the words in the text file in a formated string"""
    ft = open('sample3.txt.copy','r')
    Fk = ft.read()
    for i in Fk:
        print(i,end = '#')
    


# In[190]:


displaY_harsh = hash_display()


# In[212]:


def countAlpha():
    store_list = []
    ft = open('sample3.txt.copy','r')
    Fk = ft.read()
    fk_list = Fk.split()
    count = 0
    for i in fk_list:
        for j in i:
            if j ==j.upper():
                count = count + 1
                #store_list.append(j)
    print('the count is :', count)


# In[213]:


countAlpha()


# In[149]:


def search_text(search):
    with open('sample3.txt.copy','r') as ft:
        """this helps to search for the a word in the text file and return the total num of
        the occurence of the text in the file--modified"""
         
     
        read_lines_obj = ft.readlines()
        #count  = 0
        list_3 = []
        count = 0
        for i in range(len(read_lines_obj)):
            
            if search in read_lines_obj[i]:
                count = count + 1

                #count = count + 1
                
           
            
             
    
        return count   


# In[ ]:





# In[152]:


def searchnotintext(search):
    with open('sample3.txt.copy','r') as ft:
        """this helps to search for the a text in the text file and return
        the number of times a line doesnt start with that strings"""
        line_4 = []
        
     
        read_lines_obj = ft.readlines()
        count = 0
        for i in range(len(read_lines_obj)):
            if not  read_lines_obj[i][0:].startswith(search):
             #   line_4.append(1)
                count = count + 1
            #elif read_lines_obj[i][0:].startswith('Quod') :
             #   line_4.append(0)    
                    
             
        #print(sum(line_4),line_4)
        print(count)
                


# In[156]:


with open('sample3.txt.copy','r') as ft:
       """this helps to search for the a text in the text file and return
       the number of times a line doesnt start with that strings"""
       line_4 = []
       
    
       read_lines_obj = ft.read()
       print(read_lines_obj)


# In[157]:


searchnotintext('Quod')


# In[40]:


def printless4words():
    with open('sample3.txt.copy','r') as ft:
        """this helps to search for the a text in the text file and return
        the number of times a line doesnt start with that strings"""
        line_4 = []
        read_4_me = ft.read()
        read_js = read_4_me.split()
        for i in read_js:
            if len(i) < 4:
                line_4.append(i)
        print(line_4)
     
        
        


# In[136]:


printless4words()


# In[ ]:


#RECAP
#what i need to do today?: updated:this has been done
# i would like to write few lines of strings using writelines and write methods for gb 


# In[ ]:


list_2 = 'Iam id ipsum absurdum, maximum malum neglegi. Quod ea non occurrentia fingunt, vincunt Aristonem; Atqui perspicuum est hominem e corpore animoque constare, cum primae sint animi partes, secundae corporis. Fieri, inquam, Triari, nullo pacto potest, ut non dicas, quid non probes eius, a quo dissentias. Equidem e Cn. An dubium est, quin virtus ita maximam partem optineat in rebus humanis, ut reliquas obruat?'


# In[ ]:


with open('sample3.txt.copy','r') as ft:
    with open('sample3.txt.copy','w') as gb:
        gb.write('the God i served is a strong tower, No one comes to God except through him' 
                 'do you kno him,\n and God said to his disciple, please make sure you are the'
                 ' the emplary of life, /n and never you prophesy fake prophecies,cos God would'
                 'and his grace will be upon you always')
        #gb.write(line_1)
        #gb.write(Line_2)
        
    ft_conc = ft.readlines()
    print(ft_conc[0])


# In[ ]:


print('where are you \n give me more food')


# In[ ]:


list_4 = [1,2,3,4,5,6]


# In[ ]:


list_3 = []
list_2 = []
for i in range(len(list_4)):
    if i%2==0:
        list_3.append(list_4[i])
    elif i%2==1:
        list_2.append(list_4[i])


# In[ ]:


[i+j for i,j in zip(list_2,list_3)]#this is a code that helps to sum the number x and x+1 
#for any two numbers in the list


# In[33]:


list_storage = []
for _ in range(int(input())):
    new_name = input('input your name by putting space in in between: ')
    list_storage.append(new_name)


# In[34]:


list_storage


# In[87]:


def countAlpha(*args):
    """This is a function that returns the no of times two words occur , 
    in this case we non and esse, using the args argument"""
   
    ft = open('sample3.txt.copy','r')
    Fk = ft.read()
    fk_list = Fk.split()
    count = 0
    second_count = 0
    
    
 
    for i in range(len(fk_list)):
        if fk_list[i]==args[0]:
                count+=1
        elif fk_list[i]==args[1]:
            second_count +=1
                #store_list.append(j)
    print(f'the count for the {args[0]} is :{count} \nthe count for {args[1]} is : {second_count}')
    ft.close()


# In[86]:


countAlpha('quod','a')


# In[76]:


def func_hold(*args):
    for i in range(len(args)):
        print(args[0],end = '\n')


# In[ ]:





# In[77]:


func_hold('peter','segun','honoray')


# In[ ]:


from collections import Counter


# In[90]:


#this returns the no of times each word occurs in the text file, the times it occured is sorted from 
# highest to the smallest
with open('sample3.txt.copy','r') as ft:
    jim = ft.read().split()
    seconf_j = Counter(jim)
    print(seconf_j)
    


# In[ ]:




