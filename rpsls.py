#coding:gbk
"""
程序目的：完成RPSLS游戏
程序作者：土木四班唐欣
程序日期：2020/11/24
"""
import random #导入random模块
#0 = 石头
#1 = "史波克"
#2 = "纸"
#3 = "蜥蜴"
#4 = "剪刀"
def name_to_number(name):
    if name=="石头":
       name=0
    if name=="史波克":
       name=1
    if name=="纸":
       name=2
    if name=="蜥蜴":
       name=3
    if name=="剪刀":
       name=4
    return name

def number_to_name(number):
    if number==0:
       number="石头"
    if number==1:
       number="史波克"
    if number==2:
       number="纸"
    if number==3:
       number="蜥蜴"
    if number==4:
       number="剪刀"
    return number

def rpsls(player_choice):
    computer_choice=random.randrange(0,4)
    player_choice=choice_name
    player_choice_number=name_to_number(player_choice)
    computer_choice_name=number_to_name(computer_choice)
    print("计算机的选择为："+str(computer_choice_name))
     
    if computer_choice==player_choice_number:
       
       print("您和计算机出的一样呢！")
        
    while computer_choice==0: 
          if player_choice_number==3 or player_choice_number==4:
             print("计算机赢了！")
             break
           
          if player_choice_number==1 or player_choice_number==2:
             print("您赢了！")
             break
    while computer_choice==1 :
          if player_choice_number==2 or player_choice_number==3:
             print("您赢了！")
             break
          if player_choice_number==0 or player_choice_number==4:        
             print("计算机赢了！")
             break
    while computer_choice==2 :
          if player_choice_number==3 or player_choice_number==4:
         
             print("计算机赢了！")
             break
    
          if player_choice_number==0 or player_choice_number==1:
        
             print("您赢了！")
             break
    while computer_choice==3: 
          if player_choice_number==1 or player_choice_number==2:
         
             print("计算机赢了！")
             break
   
          if player_choice_number==3 or player_choice_number==4:
       
             print("您赢了！")
             break
    while computer_choice==4: 
          if player_choice_number==2 or player_choice_number==3:
        
             print("计算机赢了！")
             break
   
          if player_choice_number==1 or player_choice_number==2:
         
             print("您赢了！")
             break
    return player_choice_number
    
    
		

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择：")
choice_name=input()
if choice_name=="石头" or choice_name=="剪刀" or choice_name=="纸" or choice_name=="蜥蜴" or choice_name=="史波克":
   rpsls(choice_name)
else:
    print("Error: No Correct Name")





		
	      
		    
		   
	   
	   
	


