class Game:
    def __init__(self):

        print('                      ____ ')
        print('This game made it by |iheb|')
        print('                      ---- ')
        print(' ==========================================')
        input('|press enter to see the turtoil of the game|\n ==========================================')
        self.turtial()
        print(' ================================================')
        input('|Welcome i wish you enjoy press enter to get start|\n ================================================')
        
        self.OO_game()
        self.enter_players()
        play=True
        while (play==True):
            
            self.enter_scissors_paper_stone()
            self.funtion_of_game()
            print    (' \n==================================================================')        
            c_e=input('|if you want to end the game enter exit else press enter to continue| \n================================================================== \n*==>')
        

            if (c_e=='exit'):
                play=False
                print('End the game')
            
            
        
        
    def turtial (self):
        print('\n=======================')
        print(' --------')
        print('| *\\  /  |')
        print('|   --   |')
        print('| */  \\  |====>this is siccors')
        print(' --------')
        
        print('=======================')
        
        self.l=['|  ----  |','|  ----  |','|  ----  |']
        self.l1=['|   ==   |','|  ===== |','|   ==   |']   
        
        
        print(' --------')
        print(self.l[0])
        print(self.l[1])
        print(self.l[2]+'====>this is paper')
        print(' -------- ')
        
        print('=======================')
        
        print(' -------- ')
        print(self.l1[0])
        print(self.l1[1])
        print(self.l1[2]+'====>this is stone')
        print(' -------- ')
        print('=======================\n')
        


        
        
        
        
        
    
    def OO_game(self):
        
        self.a = '   ?   '
        self.b = '   ?   '
        self.c1='      ?          ?   '
        self.s1=0
        self.s2=0
        self.player1='   ?   '
        self.player2='    ?     '


        print(" __________________________")
        print(str(self.c1))
        print(" --------------------------")
        print(' ========================')
        print('| '+' -------'+'\t -------'+'  |')
        print('| '+'|' +self.a + '|  - '+'\t|' +self.b + '|'+' |')
        print('| '+' -------'+'\t -------'+'  |')
        print('| '+'======================='+' |')
        print('| '+' '+self.player1+'   vs '+self.player2)
        print('| '+'======================='+' |')
        print('| '+'    '+str(self.s1)+'   :score:   '+str(self.s2)+'     |')
        print(' ========================')

                
            

    def enter_players(self):
        print   (            '\n ===================')
        self.player1 = input('|your name player one :)|\n =================== .\n-->')
        print   (            ' ===================')        
        self.player2 = input('|your name player two :)|\n =================== .\n-->')
        


    def enter_scissors_paper_stone(self):
        
        print('===========================')
        print('choose from the table')
        print('\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        print('|'+'   '+self.player1+'       \t'+self.player2)
        print('|'+'-------------|--------------'+'|')
        print('|'+'a-->scissors |  1-->scissors'+'|'+'\n'+'|'+'z--> paper   |  2-->paper'+'   |'+'\n'+'|'+'e--> stone   |  3-->stone'+'   |')
        print( ' ----------------------------' )

        print('-------')
        
        self.entered_player1=input(self.player1+'\n*-->')
        statement=False
        while (statement==False):
            if (self.entered_player1 not in('a','z','e')):self.entered_player1=input(self.entered_player1+'is not defind \nchose from your table'+self.player1+'\n*-->')
            else :statement=True
        print('-------')
        self.entered_player2 = input(self.player2 + '\n*-->')
        print('_-_-__--_-__-_-_-_-___-___-')
        statement=False
        while (statement==False):
            if (self.entered_player2 not in('1','2','3')):self.entered_player2=input(self.entered_player2+'is not defind \nchose from your table'+self.player2+'\n*-->')
            else :statement=True
            
         
    def funtion_of_game(self): 
      #player1
        if (self.entered_player1=='a'):
            self.a='Scisors'
        elif(self.entered_player1=='z'):
            self.a=' paper '
        elif(self.entered_player1=='e'):
            self.a=' stone '
        else :
            print('error')
            
      #player2
      
        if (self.entered_player2=='1'):
            self.b='Scisors'            
        elif(self.entered_player2=='2'):
            self.b=' paper '
        elif(self.entered_player2=='3'):
            self.b=' stone '
        else :print('error')
            
        if  (self.a=='Scisors' and self.b=='Scisors'):self.c1=self.scissors_scissors()
        elif(self.a==' paper ' and self.b==' paper '):self.c1=self.paper_paper()
        elif(self.a==' stone ' and self.b==' stone '):self.c1=self.stone_stone()
        elif(self.a=='Scisors' and self.b==' paper '):self.c1=self.scissors_paper();self.s1+=1
        elif(self.a=='Scisors' and self.b==' stone '):self.c1=self.scissors_stone();self.s2+=1
        elif(self.a==' paper ' and self.b==' stone '):self.c1=self.paper_stone();self.s1+=1
        elif(self.a==' paper ' and self.b=='Scisors'):self.c1=self.paper_scissors();self.s2+=1
        elif(self.a==' stone ' and self.b==' paper '):self.c1=self.stone_paper();self.s2+=1
        elif(self.a==' stone ' and self.b=='Scisors'):self.c1=self.stone_scissors();self.s1+=1
        
        
            
        self.print_game()
            
#shema
    def scissors_scissors(self):

        self.l=['|  *\\  /   |','|    --    |','|  */  \\   |'] 
        
        a=self.l[0]+'\t'+self.l[0]
        b=self.l[1]+'\t'+self.l[1]
        c=self.l[2]+'\t'+self.l[2]
        
        return a+'\n'+b+'\n'+c
    
    def paper_paper(self):
        
        
        self.l=['|  ----    |','|  ----    |','|  ----    |'] 
    
        a=self.l[0]+'\t'+self.l[0]
        b=self.l[1]+'\t'+self.l[1]
        c=self.l[2]+'\t'+self.l[2]
        
        return a+'\n'+b+'\n'+c
        
    
    def stone_stone(self):
        global l
        
        self.l=['|    ==    |','|  =====   |','|    ==    |']
    
        a=self.l[0]+'\t'+self.l[0]
        b=self.l[1]+'\t'+self.l[1]
        c=self.l[2]+'\t'+self.l[2]
        
        return a+'\n'+b+'\n'+c
        
        
    def scissors_paper(self):
        

        self.l=['|  *\\  /   |','|    --    |','|  */  \\   |'] 
        self.l1=['|   ----   |','|   ----   |','|   ----   |']
        
        a=self.l[0]+'\t'+self.l1[0]
        b=self.l[1]+'\t'+self.l1[1]
        c=self.l[2]+'\t'+self.l1[2]
        return a+'\n'+b+'\n'+c
        
    def scissors_stone(self):

        self.l=['|  *\\  /   |','|    --    |','|  */  \\   |'] 
        self.l1=['|    ==    |','|  =====   |','|    ==    |']
        a=self.l[0]+'\t'+self.l1[0]
        b=self.l[1]+'\t'+self.l1[1]
        c=self.l[2]+'\t'+self.l1[2]
        return a+'\n'+b+'\n'+c
    
    def paper_scissors(self):

        self.l1=['|  *\\  /   |','|    --    |','|  */  \\   |'] 
        self.l=['|  ----     |','|  ----     |','|  ----     |']
        
        a=self.l[0]+'\t'+self.l1[0]
        b=self.l[1]+'\t'+self.l1[1]
        c=self.l[2]+'\t'+self.l1[2]
        return a+'\n'+b+'\n'+c
        
    def paper_stone(self):
        self.l1=['|  *\\  /   |','|    --    |','|  */  \\   |'] 
        self.l=['|  ----     |','|  ----     |','|  ----     |']
         
        a=self.l[0]+'\t'+self.l1[0]
        b=self.l[1]+'\t'+self.l1[1]
        c=self.l[2]+'\t'+self.l1[2]
        return a+'\n'+b+'\n'+c
                
    def stone_paper(self):

        self.l=['|  ----     |','|  ----     |','|  ----     |']
        self.l1=['|    ==    |','|  =====   |','|    ==    |']
        
        a=self.l[0]+'\t'+self.l1[0]
        b=self.l[1]+'\t'+self.l1[1]
        c=self.l[2]+'\t'+self.l1[2]
        return a+'\n'+b+'\n'+c
    
    def stone_scissors(self):

        self.l1=['|  *\\  /   |','|    --    |','|  */  \\   |'] 
        self.l=['|    ==    |','|  =====   |','|    ==    |']
        a=self.l[0]+'\t'+self.l1[0]
        b=self.l[1]+'\t'+self.l1[1]
        c=self.l[2]+'\t'+self.l1[2]
        return a+'\n'+b+'\n'+c
        
                
        

    
    def print_game(self):
        print(" __________________________")
        print(str(self.c1))
        print(" --------------------------")
        print(' ========================')
        print('| '+' -------'+'\t -------'+'  |')
        print('| '+'|' +self.a + '|  - '+'\t|' +self.b + '|'+' |')
        print('| '+' -------'+'\t -------'+'  |')
        print('| '+'======================='+' |')
        print('| '+' '+self.player1+'   vs '+self.player2)
        print('| '+'======================='+' |')
        print('| '+'    '+str(self.s1)+'   :score:   '+str(self.s2)+'     |')
        print(' ========================')

                
            
            
        
#scissors,paper,stone

g=Game()

