Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #第十章HANGMAN
>>> def hangman (word):
	wrong=0
	stages=["",
	       "_______      ",
	       "|            ",
	       "|      |     ",
	       "|      0     ",
	       "|     /||    ",
	       "|     /|     ",
	       "|____________"
	       ]
	rletters=list(word)
	board=["_"]*len(word)
	win=False
	print("ハングマンへようこそ！")
	while wrong<len(stages)-1:
		print("\n")
		msg="一文字目を予想してね"
		char=input(msg)
		if char in rletters:
			cind=rletters.index(char)
			board[cind]=char
			rletters[cind]="$"
		else:
			wrong+=1
		print(" ".join(board))
		e=wrong+1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print("あなたの勝ち")
			print(" ".join(board))
			win=True
			break
	if not win:
		print("\n".join(stages[0:wrong+1]))
		print("あなたの負け！正解は{}.".format(word))