def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        # 가능한 경로에 대한 거리를 담을 리스트
        distance = []
        
        # 같은 수직선상에 있을 경우
        if ball[0] == startX:
            # RIGHT 쿠션
            distance.append((2*m-startX-ball[0])**2 + (startY-ball[1])**2)
            # LEFT 쿠션
            distance.append((startY-ball[1])**2 + (startX+ball[0])**2)
            if ball[1] < startY:
                # UP 쿠션
                distance.append((2*n-startY-ball[1])**2)
            else:
                # DOWN 쿠션
                distance.append((startY+ball[1])**2)

        # 같은 수평선상에 있을 경우
        if ball[1] == startY:
            # UP 쿠션
            distance.append((2*n-startY-ball[1])**2 + (ball[0]-startX)**2)
            # DOWN 쿠션
            distance.append((ball[1]+startY)**2 + (ball[0]-startX)**2)
            if ball[0] < startX:
                # RIGHT 쿠션
                distance.append((2*m-ball[0]-startX)**2)
            else:
                # LEFT 쿠션
                distance.append((startX+ball[0])**2)
        
        # 같은 수직선, 수평선상이 아닌 경우
        if ball[0] != startX and ball[1] != startY:
            # UP 쿠션
            distance.append((2*n-startY-ball[1])**2 + (ball[0]-startX)**2)
            # DOWN 쿠션
            distance.append((ball[1]+startY)**2 + (ball[0]-startX)**2)
            # RIGHT 쿠션
            distance.append((2*m-startX-ball[0])**2 + (startY-ball[1])**2)
            # LEFT 쿠션
            distance.append((startY-ball[1])**2 + (startX+ball[0])**2)


        # 왼쪽 아래 모서리
        if startY/startX == ball[1]/ball[0]:
            if ball[0] < startX:
                pass
            else:
                distance.append((ball[1]+startY)**2 + (ball[0]+startX)**2)

        # 왼쪽 위 모서리
        if (startY-n)/startX == (ball[1]-n)/ball[0]:
            if ball[0] < startX:
                pass
            else:
                distance.append((2*n - ball[1] - startY)**2 + (ball[0]+startX)**2)

        # 오른쪽 위
        if (startY-n)/(startX-m) == (ball[1]-n)/(ball[0]-m):
            if startX < ball[0]:
                pass
            else:
                distance.append((2*m-startX-ball[0])**2 + (2*n - startY - ball[1])**2)

        # 오른쪽 아래
        if startY/(startX-m) == ball[1]/(ball[0]-m):
            if startX < ball[0]:
                pass
            else:
                distance.append((startY+ball[1])**2 + (2*m-ball[0]-startX)**2)

        answer.append(int(min(distance)))

    return answer