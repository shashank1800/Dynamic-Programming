
def AllPermutaion(string,substr):

	if len(string)==1:
		return [string+substr]

	listOfPermutation = []

	for i in range(len(string)):
		curr = AllPermutaion(string[0:i]+string[i+1:],substr+string[i])
		listOfPermutation.extend(curr)

	return listOfPermutation


string = input()
list_ = AllPermutaion(string,"")
list_.sort()
print(list_, len(list_))