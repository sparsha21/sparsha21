1st Q 
                                                                                                                                                                                                                           ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(a)
print(b)
ages.append(a)
print(ages)
ages.append(b)
print(ages)
c = len(ages)
print(c)
s =(c-1)//2
print(s)
median1 = (ages[s] + ages[s+1])/2
print(median1)
sum1 = sum(ages)
print(sum1)
avg = sum1/c
print(avg)
raint(ages)
a = min(ages)
b = max(ages)
prnge1 = b-a
print(range1)


2nd Q
dog = dict()
student["gender"] = "MALE"
dog["name"] = "BROWNIE"
dog["color"] = "BLACK"
student["age"] = "22"
dog["breed"] = "GREAT DANE"
dog["legs"] = "4"
dog["age"] = "9"
print(dog)

student = dict()
student["first_name"] = "BALA"
student["last_name"] = "BASANI"
student["gender"] = "MALE"
student["age"] = "22"
student["hobbies"] = ["CRICKET" , "MUSIC"]
student["achievements"] = "STATE CHAMPION"
student["country"] = "INDIA"
student["city"] = "PDPL"
student["ph no"] = "+91 9247241111"
print(student)
length1 = len(student)
print(length1)
print(student["hobbies"])
print(type(student["hobbies"]))
student["hobbies"].extend(["STATE CHAMPOIN"])
print(student["hobbies"])
print(student.keys())
print(student.values())

3rd Q
brothers = ("SUJITH", "RITHVIK", "RISHITH");
sisters = ("KAVYA", "JANIE", "TREEZA");
siblings = sisters + brothers;
print(siblings);
length1 = (siblings);
print(length1);
family_members = siblings + ("RAVI", "INNU");
print(family_members);

4th Q
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
print(" length:",len(it_companies))  
it_companies.update(['twitter'])
print(it_companies)  
it_companies.remove("IBM")
print(it_companies)
it_companies.update({'Blueberry'})
print(it_companies)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
X=A.union(B)
print(X)
Y=A.intersection(B)  
print(Y)
print(A&B)
print(A.issubset(B))  
print(A.isdisjoint(B)) 
print(A.symmetric_difference(B))   
X.clear()  
print(X)
age_list = [22, 19, 24, 25, 26, 24, 25, 24]
print("Age",len(age_list))
AGE_SET= set(age_in_list) 
print("Age",AGE_SET) 
print("Age",len(AGE_SET))

5th Q
r = 30
pi = 3.14
area_of_circle = pi*r**2  
res = 'The area of circle with {} is {}'.format(str(r), str(area_of_circle))
print(res)
circum_of_circle = 2*3.14*r 
print("circumference of circle:",circum_of_circle)
user_input=float(input()) 
raaadius=20
area_of_circle=pi*raaadius**2
print(area_of_circle)


6thQ
sentence="I am a teacher and I love to inspire and teach people"
unique_letter=set(sentence.split())
print("no.of unique words are ",len(unique_letter))

7th Q
sequence="Name\tAge\tCountry\tCity\tASABNEH\t250\tFINLAND\tHELSINKI";
print(sequence);

8th Q
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with a radius %s is %s meters square." %(radius,area))

9th Q
c=0.45
v=int(input("number of students")) 
list_1=[]
list_2=[]
for v in range(i):
    ele=input()
    l1.append(int(input("enter weight in lbs:"+str(v)+" "))) 
    l2.append(round(list_1[v]*0.453,2))
print("given weights in lbs:",list_1)
print("converted weights in kgs:",list_2)