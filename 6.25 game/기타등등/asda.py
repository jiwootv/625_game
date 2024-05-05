import math
import matplotlib.pyplot as plt

s16='아래2자리: {0:0.2f}, 아래 5자리 : {1:0.5f}'.format(123.1234567,3.14)
print(s16)

sin = []
cos = []
tan = []
#출처: https://blockdmask.tistory.com/424 [개발자 지망생:티스토리]
for i in range(1, 91):
	print("sin {0}: {1:0.3f}".format(i, math.sin(i)*100), end=" | ")
	sin.append(math.sin(i))
	tan.append(math.tan(i))
	cos.append(math.cos(i))
	print("cos {0}: {1:0.3f}".format(i, math.cos(i) * 100), end=" | ")
	print("tan {0}: {1:0.3f}".format(i, math.tan(i) * 100))
#tan[89] = 2000
print(sin.__len__())
plt.xlim(0,90)
plt.ylim(-400, 400)

plt.plot(sin, "r")
plt.plot(cos, "b")
plt.plot(tan, "g")

plt.legend(['Sin','Cos','Tan'], fontsize=15, loc='lower right', ncol=3)
plt.grid()
plt.show()

