answer1={
    "1.":35,
    "2.":36,
    "3.":40,
    "4.":44,
}
answer2={
    "1.":35,
    "2.":36,
    "3.":40,
    "4.":44,
}
correct_answer=0
print("if x=8,what is the value of 4(x+3)")

for i,j in answer1.items():
    print(i,j)
dap_an_1=int(input("your answer:"))
if dap_an_1==4 or dap_an_1==44:
    print("haru")
    correct_answer=correct_answer+1
    print(" Next question:if x=7,what is the value of 4(x+3)")
    for i,j in answer2.items():
        print(i,j)
    dap_an_2=int(input("your answer:"))
    if dap_an_2==3 or dap_an_2==40:
        print("haru")
        correct_answer=correct_answer+1
    else:
        print(":(")
else:
    print(":(")
    print(" Next question:if x=7,what is the value of 4(x+3)")
    for i,j in answer2.items():
        print(i,j)
    dap_an_2=int(input("your answer:"))
    if dap_an_2==3 or dap_an_2==40:
        print("haru")
        correct_answer=correct_answer+1
    else:
        print(":(")
print("số câu trả lời đúng",correct_answer)




