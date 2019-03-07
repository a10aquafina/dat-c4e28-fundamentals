answer1={
    "1.":35,
    "2.":36,
    "3.":40,
    "4.":44,
}
print("if x=8,what is the value of 4(x+3)")
for i,j in answer1.items():
     print(i,j)
while True:
     dap_an=int(input("Your answer:"))


     if dap_an==4 or dap_an==44:
        print("haru")
        break
     else:
        print(":(")