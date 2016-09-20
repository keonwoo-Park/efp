#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

dic = {1:["열쇠를 꽃고 돌렸을 때 차가 조용한가?",2,3], \
        2:["배터리 단자가 부식되었는가?",4,5],\
        3:["차에서 달깍거리는 소리가 나는가?",6,7], \
        4:["단자를 깨끗하게 하고 다시 시도하라.",0,0], \
        5:["케이블을 교체하고 다시 시도하라.",0,0], \
        6:["배터리를 교체하고 다시 시도하라.",0,0], \
        7:["시동이 완전히 걸리지 않는가?",8,9], \
        8:["점화플러그 연결 상태를 점거하라.",0,0], \
        9:["엔진이 동작한 후 바로 꺼지는가?",10,0], \
        10:["차에 연료 분사 장치가 있는가?",11,12],\
        11:["초크가 제대로 여닫히는지 확인하라.",0,0], \
        12:["서비스센터에 의뢰하라.",0,0] }


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


if __name__ == "__main__":
    direction = 1

    while True:
        try:
            info = dic.get(direction)
            message = info[0]
        except:
            print("Don't exits sentence!")
            break

        if info[1] == 0 and info[2] == 0:         
            print(message)
            break
 
        ans = version_input(message)
        if ans == 'y':
            direction = info[1]
        elif ans == 'n' :
            direction = info[2]

