num1 = "12"
num2 = "1"

ans = [0]*(len(num1)+len(num2))
#num1 = reversed(num1)
#num2 = reversed(num2)
num1 = num1[::-1]
num2 = num2[::-1]

for i in range(len(num1)):
    for j in range(len(num2)):
        ans[i+j] += int(num1[i])*int(num2[j])
        ans[i+j+1] += ans[i+j]/10
        ans[i+j] = ans[i+j]%10
        print(i)
print(ans)
while len(ans) > 1 and ans[-1] == 0: ans.pop()
 ##### a.pop() remove and return the last item in the list
print("".join(map(str,ans[::-1])))