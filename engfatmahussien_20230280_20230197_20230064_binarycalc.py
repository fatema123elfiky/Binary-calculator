#conversion of bin to ones complement
def bin_to_one_c(number1):
    number1=list(number1)
    one=''
    for i in number1:
        if i=='0':
            add='1'
            one=one+add
        elif i=='1':
            add='0'
            one=one+add
    return one


#addition function
def addition(number1,number2):#accept string only
    number1=list(number1)
    number2=list(number2)
    if len(number1)>len(number2):
        for i in range(len(number1)-len(number2)):
            number2.insert(0,"0")
    if len(number1)<len(number2):
       for i in range(len(number2)-len(number1)):
          number1.insert(0,"0")
        
    number1=[int(i) for i in number1]
    number2=[int(i) for i in number2]
    number1=number1[::-1]
    number2=number2[::-1]
    sum=''
    for i,j in zip(range(len(number1)),range(len(number2))):
        if number1[i]+number2[j]==1 or number1[i]+number2[j]==0:
          sumation=str(number1[i]+number2[j])
          sum=sum+sumation
        if number1[i]+number2[j]==2 and i!=len(number1)-1 and j!=len(number2)-1:
            sumation='0'
            sum=sum+sumation
            number1[i+1]=number1[i+1]+1
            #sum.append(sumation)
        if number1[i]+number2[j]==3 and i!=len(number1)-1 and j!=len(number2)-1:
            sumation='1'
            sum=sum+sumation
            number1[i+1]=number1[i+1]+1
            #sum.append(sumation)
        if i==len(number1)-1 and j==len(number2)-1 and number1[i]+number2[j]==2:
            sumation='0'
            sumation2='1'
            sum=sum+sumation
            sum=sum+sumation2
        if i==len(number1)-1 and j==len(number2)-1 and number1[i]+number2[j]==3:
            sumation="1"
            sumation2="1"
            sum=sum+sumation
            sum=sum+sumation2
    sum=sum[::-1]    
    return(sum)#return string only    


#twos complement
def bin_to_twos_complement(binnumber):#accepts str only
    two_comp=addition(bin_to_one_c(binnumber),'1')
    # the returned value is string
    return two_comp# return string value
#FUNCTION for validtion
def validity(number1):
    i=0
    is_not_binary=True
    while is_not_binary==True:
        #number1=input('please enter the number')
        for i in number1:
            if i!='0' and i!='1':
                number1=input('please enter a valid number')
                is_not_binary=True
                break
            else:
                is_not_binary=False
    return number1 


# subtraction function
def subtraction(number1,number2):#string only is accepted
    number1=list(number1)
    number2=list(number2)
    number1=[int(i) for i in number1]
    number2=[int(i) for i in number2]
    if len(number1)>len(number2):
        for i in range(len(number1)-len(number2)):
            number2.insert(0,0)
    if len(number1)<len(number2):
       for i in range(len(number2)-len(number1)):
          number1.insert(0,0)
    number1=number1[::-1]
    number2=number2[::-1]      
    result=''
    for i,j in zip(range(len(number1)),range(len(number2))):
        if number1[i]-number2[j]==1 or number1[i]-number2[j]==0:
            subtract=number1[i]-number2[j]
            result=result+str(subtract)
        if number1[i]-number2[j]==-1 or number1[i]-number2[j]==-2:
            number1[i]=number1[i]+2
            number1[i+1]=number1[i+1]-1
            subtract=number1[i]-number2[j]
            result=result+str(subtract)
    
    result=result[::-1]
    return result#string is returned

#main program
while True:
  print('**binary calculator**')
  print('A) insert new numbers\nB) exit')
  choice=input()
  #is_not_binary=True
  #i=0
  if choice=='A':
     
         ###the validity of the number
      number1=input('enter the first binary number')
      number1=validity(number1)
      
      
      while True:
             print('** please select the operation **')
             print("A)Compute one's complement")
             print("B)Compute two's complement")
             print('C)addition')
             print('D)subtraction')
             operation=input()
             if operation=="A" or operation=="B" or operation=='D' or operation=='C':
                 ###all calculations are here
                 if operation=="A":
                     print(bin_to_one_c(number1))
                 elif operation=="B":
                    print(bin_to_twos_complement(number1))
                 elif operation=='C':
                     number2=input('enter the second binary number')
                     number2=validity(number2)
                     print(addition(number1,number2))
                 elif operation=='D':
                     number2=input('enter the second binary number')
                     number2=validity(number2)
                     while number1< number2:
                       print('please enter the first number greater than the second number')
                       number1=input('enter the first binary number')
                       number1=validity(number1)      
                       number2=input('enter the second binary number')
                       number2=validity(number2)
                     
                     print(subtraction(number1,number2))
                     
                 break
             else:
                 print('please enter a valid choice')
  elif choice=='B':
      break
  else:
      print('enter a valid choice')

# fatema elzhraa ahmed mohamed elfiky 20230280
# doha fathy refaey khodary mustafa 20230197
# alaa tarek mohamed salah el den ahmed 20230064