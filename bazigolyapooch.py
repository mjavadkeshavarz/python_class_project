username = input("lotfan shomare daneshjoie khod ra vared konid:") 
 while username != ("1401123071"): 
     print("shomare daneshjoie eshtebah ast") 
     username = input("lotfan shomare daneshjoie khod ra vared konid:") 
 print("shomare daneshjoie dorost mibashad") 
 password = input("lotfan password khod ra vared konid:") 
 while password != ("9999999999"): 
     print("password eshtebah ast") 
     password = input("lotfan password khod ra vared konid") 
 print("password dorost mibashad") 
 print("be bazi khosh amadid") 
 emtiaz_player1 = 0 
 emtiaz_player2 = 0 
 while True : 
     player_1 = input("lotfan entekhab khod ra anjam dahid : chap ya rast ?") 
     player_1 = str.lower(player_1) 
     if player_1 == "chap": 
         print("player_1 : chap") 
     elif player_1 == "rast": 
         print("player_1 : rast ") 
     else: 
         print("entekhab shoma eshtebah ast") 
         player_1 = input("lotfan entekhab khod ra anjam dahid : chap ya rast ?") 
  
     import random as rn 
     randint = rn.randint(1 , 3) 
     player_2 = randint 
     if player_2 == 1: 
         print("player_2 : chap") 
     if player_2 ==2: 
         print("player_2 : rast ") 
     if player_1 == "chap" and player_2 == 1: 
         print("barande : player_1") 
         emtiaz_player1 += 1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "chap" and player_2 == 2 : 
         print("barande : player_2") 
         emtiaz_player2 += 1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "rast" and player_2 == 1 : 
         print("barande : player_2") 
         emtiaz_player2 += 1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "rast" and player_2 == 2 : 
         print("barande : player_1") 
         emtiaz_player1 += 1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     if emtiaz_player1 == 3 : 
         print("Shoma barande shodid") 
         break 
     if emtiaz_player2 == 3 : 
         print("shoma bakhtid") 
         break