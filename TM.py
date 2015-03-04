""" 
Program:Universal Turing Machine Simulator
Input: XML file with program descrition
Output:Stepwise dispaly of simulation of Turing Machine
tapep=Program tape
tapet=I/O tape
tapeq=Tape containing present state

"""



import xml.etree.ElementTree as etree
ans='y'
while ans=='y' or ans=='Y':
    filename = input('Enter a file name: ')
    tree = etree.parse(filename)
    root = tree.getroot()
    
    print (root.attrib["name"])
    print("Program Starts....")
    a= root[0].attrib["format"]
    print(a)
    inputstr=root[0].text
    inputstr=inputstr.replace(' ','')
    inputstr=inputstr.replace('\t','')
    inputstr=inputstr.replace('\n','')
    
    print(inputstr.strip(' '))
    blank=root[0].attrib["blank"]
    blank=blank.strip(' ')
    head=root[0].attrib["head"]
    head=head.strip(' ')
    formate=root[0].attrib["format"]
    blank1=blank #for display
    
    #program tape attribues
    start=root[1].attrib["start"]
    start=start.strip(' ')
    halt=root[1].attrib["halt"]
    halt=halt.strip(' ')
    left=root[1].attrib["left"]
    left=left.strip(' ')
    right=root[1].attrib["right"]
    right=right.strip(' ')
    blanke=root[1].attrib["blank"]
    blanke=blanke.strip(' ')

   #replace blank with a unique character incase blank != blanke
    blank='...'
    
    #reading the program in tape p
    listt=[]
    tape_p=root[1].text
 
   #Retain only the code character removing any specila character
    for text in tape_p:
        if text=='\t'or text==' 'or text=='\n' or text=='{' or text=='}'or text=='('or text==')' or text=="'":
              pass
        elif text==':':
            listt.append(',')
        else:
            listt.append(text)
    str1=''.join(listt)
    str11=str1.split(',')
    tapep=str11
   #start state in tapeq
    tapeq=start
    
    #making tape t by appending necessary blanks
    lst=[]
    for i in range(100):
     lst.append(blanke)
    inpstart=len(lst) #saving the start position for input  for display
    for txt in inputstr:
        if txt != ' 'and txt!='\n' and txt!='\t':
            lst.append(txt)
    inpend=len(lst)-2  #saving the end position for input  for display     
    tapet=lst # I/O tape
    
    #read present state and input
    ns=ps=tapeq
   
    #find the initial head position and deleting head
    for i in range(len(tapet)):
          if tapet[i]==head:
                hpos=i
    del(tapet[hpos])
    
    #append blank in tapet I/O tape after input
    for i in range(100):
     tapet.append(blanke)
    

    inp=tapet[hpos]# saving present input
        
    
    i=0
    lstout=[]
    flag=0
    flagf=0
    #Start the program until halt
    while ns != halt:
         ps=ns
         inp=tapet[hpos]
         if inp==blank:
             inp=blanke
             
         #search the program for the present state and input  
         if tapep[i]==ps and tapep[i+1]==inp:
             
            # copy next state     
             ns=tapep[i+2]
             tapeq=ns
             
             #copy output
             po=tapep[i+3]
             if po==blanke:
              tapet[hpos]=blank
             else:
                 tapet[hpos]=po
             
             #move head as specified
             mov=tapep[i+4]

             # print the program statement
             print('{(',ps,',',inp,'):(',ns,',',po,',',mov,')}')
             
            
             #printing the I/O tape before head move
             tt=''
             for p in range(inpstart,inpend+50):
                 if p==hpos:
                   tt+=head
                 if tapet[p]==blanke and tapet[p+1]==blanke:
                     break
                    
                 if tapet[p]==blank :
                     tt+=blank1
                     continue
                 tt+=str(tapet[p])
             print(tt)
             

             # adjusting head position according to move
             if mov==left:
                 hpos=hpos-1
                 flag=1
                 
             else:
                  hpos=hpos+1
                  
                  

             #print the I/O tape after head move
             #Decrease the starting position if written on LHS of I/O tape
             if flag == 1 and tapet[hpos]==blanke and tapet[hpos+1]!=blanke and tapet[hpos-1]== blanke and tapet[hpos-2]==blanke :
                 inpstart=inpstart-1
                 flag=0
                 flagf=1
             tt=''
             for p in range(inpstart,inpend+50):
                 if p==hpos:
                   tt+=head
                 if  tapet[p]==blanke  and tapet[p+1]==blanke:
                     tt+=' '
                     break
                 if tapet[p]==blanke and tapet[p-1]==blanke and flagf==1:
                     tt+=' '
                     flagf=0
                     continue
                 if tapet[p]==blank:
                     tt+=blank1
                     continue
                 tt+=str(tapet[p])
             print(tt)
             
             i=i+5  
         else:
             i=i+5
         if i>=len(tapep):
             i=0
    
    print('Program Completed')         
    ans=input('Run another TM file?(y or n)')
print ('Thank You')

         
   







