print('''
          .s$P*.s$$$s.`*T$$b T TP$P.d$P .sd$s.                
        .s$P .s$$$$$$$b. T$$b T:P d$$P.d$$$$$$bs.             
       d$$P d$$$$P'`T$$$b $$$;:$bd$$$$$$b`T$$*$$$b.           
      d$$P d$$$P' .+. *$$:$$$;.$$$P^*""*^b.$$b T$$$b          
     d$P .d$$$b.s$$$$$b TP^TP dP',d$$$$$s.`T$$b T$$$b         
    d$P d$$P T$$$P*""*^b.b d,P^*"*^T$$$$$$$b`T$b$$$$$.        
   ,$P d$P .$$$P'       `'*`        `T$$$$$$$b`T$$$$$$         
   :$ d$P d$$$P                       `T$$$$$$b TPT$$$b        
  :$$d$$ d$$$P                          T$$$$$$b T.`T$$;       
  :$$$$$d$$$P                            T$$$$ $b T.T$$:       
  $$$$$P$$$$                              T$$$$T$b T `T$       
  $P$$$;$$$;                               T$^$b Tb b :$       
  $`$$$ $$$;                                T.T$b TY$,:$       
  $:$$$ $$$'                                `$ T$; $$;'$       
  $;$$$;$$$                                  `b T; $$$ $       
  $:T$$;$$$  .d$$s.                    .s$$b..$;:$;$$$.T       
 / __`*:$$$ *'   `*Tb._            _.dP*'   `*$;:$:$P__ \      
..' .`.:$$$         `*Ts'        `sP*'        $$:$$P'. `,,     
;  /   ,$$;   .+s**s.   `.           .s**s+.  T$:PP'  \  :     
: ,   /:$$;   \ *ss* \    ;         / *ss* /    +: \   . ;     
 .`  :  $$;,  .+s$$$s+.            .+s$$$s+.  .* ;  ;  ',      
  \   *.:$$,*d$P*"$$$T$b  ,+**+,  d$P*"$$$T$b*   .*    /       
   \    `$$;:$; +:$$$:$$;*      *:$; +:$$$:$$;  :     /        
         $$; T$b._$$$d$P          T$b._$$$d$P   ;              
     `._.:$$, `*T$$$P*'            `*T$$$P*'    :._.'          
         |$$;             '                     |P$$b.         
         ;`$$,           :.     ,               :b.`T$b        
         ` T$$b._        `*.__.*'               d$$b T$b       
          . *TP*'           ""                 d$$$$b.:$;      
           \                                  dP T$$$$$$$      
            \          .+*"*--*"*+.          d$b. T$$^$$$      
             `.       :._.--..--._.;       .'$$$$; $$ $$$      
               ;.      `.        .'      .'  $$$$$ $P $$;      
               : `.      `*----*'      .'    $$$$$ $b $P       
               |   `.                .'      $$$$$Y$$dP        
        [bug]  :     `.            .'        :T$$P$$P,db.      
              /        `-.      .-'          dbT d$Pd$$$$b.    
             /            `****'            d$$$PT$$$b T$$$b   
           .'                              d$$$P db`T$b T$$$b  
        _.'                               :$$$P.d$$b:$$$`$$$$; 
   _.-*' `.                               $$$$:$$$$$;$$$:$$$$$ 
           `-.                            :$$$;$$$$$$$$$;$$$$$ 
              `-.                        .-T$$$$P$$$$$P d$$$$; 
                 `.     `.     .*      .'   T$$$b`T$P.sd$$$$P  
                   `.     `-  '      .'      `T$$b$$$$$$$$P'   
                     `.            .'          `T.T$$$$P$$$b.  
                       `.        .'             :$$$$P'd$$$$$;  
                         `.    .'               $$$$$:d$;$$$$$.
                           `..'                 :$$$$;$$$b`T$$;
                                                 T$$$:$$$$; $$$
                                                  T$$$T$$$;d$$;
                                                   `T$b`T$$$$P 
                                                     `*b T$P'
''')

print("Welocome to the new tomb raider")
print("Your mission is to find the treasure")

choice1 = input('You begin in a crossroad. Where do you want to go? Type "left" or "right\n').lower() 

if choice1 == "right":
  choice2 = input('You are now in a lake and you have the options either to swim or to use the boat. Type "swim" or "boat"\n').lower() 
  if choice2 == "boat": 
    choice3 = input('You are now in a room with 3 doors. One red, one green and one blue. Which color do you choose?\n').lower() 
    if choice3 == "green":
      print("Congratulations! You found the treasure! You win! :)") 
    elif choice3 == "red": 
      print("You entered a room full of fire. Game over. :(") 
    else:
      print("You entered a room full of beasts. Game over. :(") 
  else: 
    print("You got eaten by a alligator. Game over :(")
else:
  print("You fell into a deadly trap. Game over :(" )
