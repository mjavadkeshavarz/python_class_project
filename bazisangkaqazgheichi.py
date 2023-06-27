username = input("lotfan shomare daneshjoie khod ra vared konid:") 
 while username != ("1401123071"): 
     print("shomare daneshjoie eshtebah ast") 
     username = input("lotfan shomare daneshjoie khod ra vared konid:") 
 print("shomare daneshjooe dorost mibashad") 
 password = input("lotfan password khod ra vared konid:") 
 while password != ("9999999999"): 
     print("password eshtebah ast") 
     password = input("lotfan password khod ra vared konid") 
 print("password dorost mibashad") 
 print("be bazi khosh amadid") 
 emtiaz_player1 = 0 
 emtiaz_player2 = 0 
 while True : 
     player_1 = input("lotfan entekhab khod ra anjam dahid: sang , kaghaz , gheichi ?") 
     player_1 = str.lower(player_1) 
     if player_1 == "sang": 
         print("player_1 : SANG") 
     elif player_1 == "kaghaz": 
         print("player_1 : KAGHAZ") 
     elif player_1 == "gheichi": 
         print("player_1 : GHEICHI") 
     else: 
         print("entekhab shoma eshtebah ast") 
         player_1 = input("lotfan entekhab khod ra anjam dahid : sang , kaghaz , gheichi ?") 
     import random as rn 
     randint = rn.randint(1 , 4) 
     player_2 = randint 
     if player_2 == 1: 
         print("player_2 : sang") 
     elif player_2 == 2: 
         print("player_2 : kaghaz") 
     elif player_2 == 3: 
         print("player_2 : gheichi") 
     if player_1 == "sang" and player_2 == 1: 
         print("mosavy : mosavy") 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "sang" and player_2 == 2: 
         print("barande : player_2") 
         emtiaz_player2 +=1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "sang" and player_2 == 3: 
         print("barande : player_1") 
         emtiaz_player1 += 1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "kaghaz" and player_2 == 1: 
         print("barande : player_1") 
         emtiaz_player1 += 1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "kaghaz" and player_2 == 2: 
         print("mosavy") 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "kaghaz" and player_2 == 3: 
         print("barande : player_2") 
         emtiaz_player2 += 1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "gheichi" and player_2 == 1: 
         print("barande : player_2") 
         emtiaz_player2 += 1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "gheichi" and player_2 == 2: 
         print("barande : player_1") 
         emtiaz_player1 += 1 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     elif player_1 == "gheichi" and player_2 == 3: 
         print("mosavy") 
         print("emtiaz_player1 =",emtiaz_player1) 
         print("emtiaz_player2 =",emtiaz_player2) 
     if emtiaz_player1 == 3 : 
         print("shoma barande shodid") 
         break 
     if emtiaz_player2 == 3 : 
         print("shoma bakhtid") 
         break