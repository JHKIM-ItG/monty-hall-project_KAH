# 종화님 – 결과 출력 및 해석 담당
print(f"Not switching allows you to win {not_switching_wins} out of {iterations} times.")
print(f"Switching allows you to win {switching_wins} out of {iterations} times.\n")
print(f"Winning rate without switching: {not_switching_wins / iterations:.2%}")
print(f"Winning rate with switching: {switching_wins / iterations:.2%}")
