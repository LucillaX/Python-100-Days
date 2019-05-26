'''
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
n 赌注
'''
from random import randint

money = 1000
def yao():
	a=randint(1,6)
	b=randint(1,6)
	s=a+b
	return s

print('''游戏规则：Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束''')
while money>0:
	print('目前您的资产为:',money)
	n=int(input('请下注:'))
	if n>money:
		continue
	input('请按回车键摇骰子')
	su=yao()
	print('两个骰子点数之和为：',su)
	if su== 7 or su == 11:
		money = money+n
		print('您赢了，您的资产变为：',money)
	elif su == 2 or su ==3 or su==12:
		money= money-n
		print('您输了，您的资产变为：',money)
	else:
		while  1:
			print('游戏继续')
			input('请按回车键摇骰子')
			um=yao()
			print('两个骰子点数之和为：',um)
			if um==7:
				money= money-n
				print('您输了，您的资产变为：',money)
				break
			elif um == su:
				money = money+n
				print('您赢了，您的资产变为：',money)
				break
			else:
				continue
print('您破产了，游戏结束')

