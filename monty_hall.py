

def monty_hall(choice, switch=False, doorCount=doors):
    # 문 배열 초기화 (False = 꽝, True = 당첨)
    door = [False] * doorCount
    # 무작위로 하나를 당첨 문으로 설정
    door[randrange(doorCount)] = True
    
    # 참가자가 처음 선택한 문
    chosen = door[choice]
    
    # 선택하지 않은 문들
    unpicked = door.copy()
    del unpicked[choice]
    
    # 남은 문들 중에 당첨이 있으면 alternative=True
    alternative = True in unpicked
    
    if switch:
        return alternative  # 문을 바꾸면 alternative 결과에 따라 당첨 여부 결정
    else:
        return chosen       # 바꾸지 않으면 처음 선택한 값

      
      
      
      
print(f"Not switching allows you to win {not_switching_wins} out of {iterations} times.")
print(f"Switching allows you to win {switching_wins} out of {iterations} times.\n")
print(f"Winning rate without switching: {not_switching_wins / iterations:.2%}")
print(f"Winning rate with switching: {switching_wins / iterations:.2%}")
