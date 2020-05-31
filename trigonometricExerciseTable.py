a0 = 0**0.5
a1 = 1**0.5
a2 = 2**0.5
a3 = 3**0.5
a4 = 4**0.5
a = 4**0.5


                                #########sin##########
sin0 = [float("{:.3f}".format(a0/a,"<5")),float("{:.3f}".format(a1/a)),float("{:.3f}".format(a2/a)),
        float("{:.3f}".format(
    a3/a)),float("{:.3f}".format(a4/a))]
# print ("\u221a",sin0)


                                #########cos###########
cos0 = sin0[::-1]

                                    #####tan######
ii = 0
listOfItems = []
for ii in range(0,5):
    # print(ii)
    try:
        tana = sin0[ii]/cos0[ii]
        ii = ii+1
        lst = float("{:.3f}".format(tana))
        # print(lst)
        # s = listOfItems.append(tana)
        # print(tana)
        s = listOfItems.append(lst)

        # print("List",listOfItems)
    except ZeroDivisionError:
        # print("∞")
        listOfItems.append("∞")
# print(listOfItems)


                                #####cot#########
cot = listOfItems[::-1]

                           ##########sec#######

u = 0
sec = 1/cos0[1]
fromList = []
for u in range(0,5):
    try:
        sec0 = 1/cos0[u]
        u = u+1
        # print("lll",sec0)
        sec1 = float("{:.3f}".format(sec0))
        # print("ffff",sec1)
        sc = fromList.append(sec1)
    except ZeroDivisionError:
        fromList.append("∞")

# print(fromList)
                        ##########cosec#############
cosec = fromList[::-1]



print()
print("\t   0     30    45     60     90")
print(f"sin    {sin0}")
print(f"cos    {cos0}")
print(f"tan    {listOfItems}")
print(f"cot    {cot}")
print(f"sec    {fromList}")
print(f"coses  {cosec}")



input()


######OUTPUT_of_the_program#################

# 	   0     30    45     60     90
# sin    [0.0, 0.5, 0.707, 0.866, 1.0]
# cos    [1.0, 0.866, 0.707, 0.5, 0.0]
# tan    [0.0, 0.577, 1.0, 1.732, '∞']
# cot    ['∞', 1.732, 1.0, 0.577, 0.0]
# sec    [1.0, 1.155, 1.414, 2.0, '∞']
# coses  ['∞', 2.0, 1.414, 1.155, 1.0]
 


#######################Practice and mistakes::::::::###################


# float("{:.5f}".format())
#############  practice and mistakes:----##########
#
# # def errorSolver(i,j):
# for i in sin0:
#     for j in cos0:
#         try:
#             tan = i / j
#             print(tan,end=" ")
#             # if i==j:
#             #     s = listOfItems.append(tan)
#                 # print("s",s)
#         except ZeroDivisionError:
#             print("Can't divide!")
#             # print()
#             # print()
#             if i==j:
#                 listOfItems.append(tan)
#                 # print("Tttt",tan)
#             else:
#                 print("")
#         # print()
#         # print("sat",tan)
#         # print ()
#             # print("This is tan theta",tan)
# # s = errorSolver(sin0,cos0)
# # print(s)
#


######3For set the limit of the floating point in float formate
# tan0 = float("{:.5f}".format())
#
# Ex:-
# x = 66.099988898
# g = float("{:.5f}".format(x))
# print (g)


###for find the value in fraction form
# sin0 = Fraction(math.sqrt(a3/a))
