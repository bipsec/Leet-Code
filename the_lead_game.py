def game():
    n = int(input())
    player1_sum = 0
    player2_sum = 0
    cu_sum = 0
    cu_sum2 = 0
    for i in range(n):

        p1, p2 = map(int, input().split())
        player1_sum += p1
        player2_sum += p2

        if player1_sum > player2_sum:
            diff = player1_sum - player2_sum
            cu_sum = max(cu_sum, diff)
        else:
            diff = player2_sum - player1_sum
            cu_sum2 = max(cu_sum2, diff)
    if cu_sum > cu_sum2:
        print(1, cu_sum)
    else:
        print(2, cu_sum2)


game()

