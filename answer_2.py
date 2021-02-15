def base10_valueGenerator(input_string,ls):
	if len(input_string)%2==0:
		split1=input_string[:len(input_string)//2]
		split2=input_string[len(input_string)//2:]
		split1.upper()
		split2.upper()
		val=[]
		val1=[]
		for i in split1:
			val.append(list[i])


		for i in split2:
			val1.append(list[i])

		the_base10_split1=0
		the_base10_split2=0
		for i in range(0,len(val)):
			the_base10_split1+=val[i]*26**(len(val)-i-1)

		for i in range(0,len(val1)):
			the_base10_split2+=val1[i]*26**(len(val1)-i-1)
		total_base10=the_base10_split1+the_base10_split2
		return total_base10
	else:
		return 0


list={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'v':21,'W':22,'X':23,'Y':24,'Z':25}
s=str(input("Enter the alphabet\n"))
s=s.upper()
result=base10_valueGenerator(s,list)
print(result)
