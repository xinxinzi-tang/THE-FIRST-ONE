#coding:gbk
"""
����Ŀ�ģ����RPSLS��Ϸ
�������ߣ���ľ�İ�����
�������ڣ�2020/11/24
"""
import random #����randomģ��
#0 = ʯͷ
#1 = "ʷ����"
#2 = "ֽ"
#3 = "����"
#4 = "����"
def name_to_number(name):
    if name=="ʯͷ":
       name=0
    if name=="ʷ����":
       name=1
    if name=="ֽ":
       name=2
    if name=="����":
       name=3
    if name=="����":
       name=4
    return name

def number_to_name(number):
    if number==0:
       number="ʯͷ"
    if number==1:
       number="ʷ����"
    if number==2:
       number="ֽ"
    if number==3:
       number="����"
    if number==4:
       number="����"
    return number

def rpsls(player_choice):
    computer_choice=random.randrange(0,4)
    player_choice=choice_name
    player_choice_number=name_to_number(player_choice)
    computer_choice_name=number_to_name(computer_choice)
    print("�������ѡ��Ϊ��"+str(computer_choice_name))
     
    if computer_choice==player_choice_number:
       
       print("���ͼ��������һ���أ�")
        
    while computer_choice==0: 
          if player_choice_number==3 or player_choice_number==4:
             print("�����Ӯ�ˣ�")
             break
           
          if player_choice_number==1 or player_choice_number==2:
             print("��Ӯ�ˣ�")
             break
    while computer_choice==1 :
          if player_choice_number==2 or player_choice_number==3:
             print("��Ӯ�ˣ�")
             break
          if player_choice_number==0 or player_choice_number==4:        
             print("�����Ӯ�ˣ�")
             break
    while computer_choice==2 :
          if player_choice_number==3 or player_choice_number==4:
         
             print("�����Ӯ�ˣ�")
             break
    
          if player_choice_number==0 or player_choice_number==1:
        
             print("��Ӯ�ˣ�")
             break
    while computer_choice==3: 
          if player_choice_number==1 or player_choice_number==2:
         
             print("�����Ӯ�ˣ�")
             break
   
          if player_choice_number==3 or player_choice_number==4:
       
             print("��Ӯ�ˣ�")
             break
    while computer_choice==4: 
          if player_choice_number==2 or player_choice_number==3:
        
             print("�����Ӯ�ˣ�")
             break
   
          if player_choice_number==1 or player_choice_number==2:
         
             print("��Ӯ�ˣ�")
             break
    return player_choice_number
    
    
		

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��")
choice_name=input()
if choice_name=="ʯͷ" or choice_name=="����" or choice_name=="ֽ" or choice_name=="����" or choice_name=="ʷ����":
   rpsls(choice_name)
else:
    print("Error: No Correct Name")





		
	      
		    
		   
	   
	   
	


