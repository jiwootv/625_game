import random, time
def download(type):
	print(f"{type}")
	for i in range(20):
		print("\r진행률 : %s%s ||| %d%% / 100%%" % (("■"*(i)), "□"*(20-i), i*5), end="")
		time.sleep(random.random()/2)
	print(f"\r진행률 : ■■■■■■■■■■■■■■■■■■■■ 100% / 100%")
	print(f"{type} 완료\n")
download("게임 모듈 다운로드")
download("게임 하기")
download("서진이 공부시키기")
print("다운로드가 완료되었습니다.")