######################################
# Base conversion Project CSC 210
# Converts a number from n base, to any requeested base
# Creed McFall
# 09/21/2023
###################################### Constructor
class Number:
    def __init__(self, num, curr_base, new_base, bit_len):
        self._num = num
        self._curr_base = curr_base
        self._new_base = int(new_base)
        self._bit_len = int(bit_len)
 
###################################### Getters
        
    @property
    def num(self):
        return self._num
    @property
    def curr_base(self):
        return self._curr_base
    @property
    def new_base(self):
        return self._new_base

###################################### setters
    
    @num.setter
    def num(self, value):
        self._num = value
    @curr_base.setter
    def curr_base(self, value):
        self._curr_base = value
    @new_base.setter
    def new_base(self, value):
        self._new_base = value
        
###################################### Functions
        
###################################### converts base 10 to any base
        
    def from_10(self,B_10):
        output = ""
        B_10 = int(B_10)
        while B_10 > 0:
            ##Checks to see if remainder is greater than 10 and converts to appropriate Letter i.e 11--->B
            if B_10 % self._new_base > 9:
                output += chr((B_10 % self._new_base) + 55)
            else:
            ##Turns remainder into string and adds it to output
                output += str(B_10 % self._new_base)
            B_10 //= self._new_base
        ##Reverses string to output number correctly
        return output[::-1]
        
############################################################### Converts any base to base10
        
    def to_10(self):
        num = self._num.upper()
        i = 0
        Base10 = 0
        while i < len(num):
            #Checks to see if there are letters in the number i.e hexidecimal and converts appropriatly
            if ord(num[i]) >= 65 and ord(num[i]) <= 90 :   
                Base10 += (ord(num[i]) - 55) *(int(self._curr_base)**(len(num) - (i+1)))
            else:
            #Converts current base into base 10 w power method i.e ---> x*2^1 + x*2^0
                Base10 += (int(num[i])*(int(self._curr_base)**(len(num) - (i+1))))
            i += 1
        return str(Base10)
    
################################################################## Checks the converted number and adds zeros or returns overflow as neccesary
    
    def check_length(self, num):
        if len(num) < self._bit_len:
            #creates string of required amount of zeros make appropriate output
            add = "0"*(self._bit_len-len(num))
            return add + num
        elif len(num) > self._bit_len:
            return "OVERFLOW"
        else:
            return num
            
        
###################################################################################################****MAIN****

## Opens file
        
outputs = []    
everyline = []
filename = "input.txt"
with open("input.txt", "r") as file:
    Input = file.readlines()
    
###################################################### Reads each line in file
    
for line in Input:
    line = line.rstrip("\n")
    everyline.append(line)

######################################################## breaks up each line in file to get needed values

for x in everyline:
    i = 0
    look = []
    while i < len(x):
        if x[i] == " ":
            look.append(i)
        i += 1
    num = x[:look[0]]
    curr_base = x[(look[0]+1):look[1]]
    new_base = x[(look[1]+1):look[2]]
    Maxbit = x[(look[2]+1):]
    
    ### Creates number class instance for each line in file, and then calls reqiured functions to convert to appropriate base
    
    conv = Number(num, curr_base, new_base, Maxbit)
    base10_num = conv.to_10()
    new_number = conv.from_10(base10_num)
    final_num = conv.check_length(new_number)
    
    
    outputs.append(final_num)

########################################################## Puts outputs into .txt file (used python tutorial.net to figure out how to do so)

with open("output.txt", "w") as output:
    for line in outputs:
        output.write(line)
        output.write("\n")
    