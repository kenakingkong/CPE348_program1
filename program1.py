#makena kong
#mkong02
#program 1

#string -> list of strings
#recursively generate the subsets of the letters in a string
def get_subsets(astring):
   alist = []
   temp = []
   if len(astring) > 0:
      last = astring[len(astring)-1:]
      temp = get_subsets(astring[:-1])
      for i in temp:
         alist.append(i)
      for j in temp:
         alist.append(j+last)
      return alist
   else:
      alist.append(astring)
      return alist

#string -> list of lists of the subsets and their bitstring
#generates list containing subsets along with bitstring representation
def get_bitstrings(string):
   alist = []
   subsets = get_subsets(string)
   for subset in subsets:
      bits = ['0']*len(string)
      for char in subset:
         index = string.index(char)
         bits[index] = '1'
      alist.append([subset,''.join(bits)])
   return alist

 
#tests  
#print(get_subsets("abc"))
#print(get_bitstrings('abc')) 
#print(get_bitstrings('abcde'))
