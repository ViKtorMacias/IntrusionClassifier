textos=[
 
  ]


# Using readlines() 
file1 = open('intrusion.txt', 'r') 
Lines = file1.readlines() 
  

# Strips the newline character 
for line in Lines: 
    intrusion = [line.strip(), 'Sqlinjection']
    textos.append(intrusion)


# Updated textos list
print('textos list: ', textos)