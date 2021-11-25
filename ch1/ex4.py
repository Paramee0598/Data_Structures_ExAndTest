def num_grid(lst):

    #Code Here
    print("\n")
    max_X = 0
    max_Y = 0

    list_cal = lst
    """เปลี่ยน - เป็น 0 """
    while max_X != 5:
        ###############
        while max_Y != 5:
         for i in list_cal[max_X][max_Y] :
             if i == '-':
                 list_cal[max_X][max_Y] = int('0')

             else:
                 pass
         max_Y  = max_Y +1

         if max_Y == 5:
            max_Y = 0
            break
         else:
            pass

        max_X = 1 + max_X


    max_X = 0
    max_Y = 0
    """เปลี่ยนรอบ # เป็น 1 """
    while max_X != 5:
        #-------------------
        while max_Y != 5:
            for i in str(list_cal[max_X][max_Y]):
                if i == '#':
                    if (max_X ==  0   and max_Y == 0) :
                      if list_cal[max_X ][max_Y + 1] == '#' :
                          pass
                      else: list_cal[max_X ][max_Y + 1] = int('1') + list_cal[max_X ][max_Y + 1]

                      if list_cal[max_X + 1][max_Y ] == '#' :
                          pass
                      else: list_cal[max_X + 1][max_Y ] = int('1') + list_cal[max_X + 1][max_Y ]

                      if list_cal[max_X + 1][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  0   and max_Y == 2):
                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                        if list_cal[max_X + 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                        if list_cal[max_X + 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  0   and max_Y == 3):
                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                        # list_cal[max_X ][max_Y ] = int('0') + list_cal[max_X ][max_Y ]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                        if list_cal[max_X + 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                        if list_cal[max_X + 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  1   and max_Y == 1) :
                      if list_cal[max_X - 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                      if list_cal[max_X - 1][max_Y ] == '#' :
                          pass
                      else: list_cal[max_X - 1][max_Y ] = int('1') + list_cal[max_X - 1][max_Y ]
                      if list_cal[max_X - 1][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                      if list_cal[max_X ][max_Y - 1] == '#' :
                          pass
                      else: list_cal[max_X ][max_Y - 1] = int('1') + list_cal[max_X ][max_Y - 1]
                      if list_cal[max_X ][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X ][max_Y + 1] = int('1') + list_cal[max_X ][max_Y + 1]
                      if list_cal[max_X + 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                      if list_cal[max_X + 1][max_Y ] == '#' :
                          pass
                      else:list_cal[max_X + 1][max_Y ] = int('1') + list_cal[max_X + 1][max_Y ]
                      if list_cal[max_X + 1][max_Y + 1] == '#' :
                          pass
                      else: list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                      #list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  4   and max_Y == 1) :
                      if list_cal[max_X - 1][max_Y - 1] == '#':
                          pass
                      else: list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                      if list_cal[max_X - 1][max_Y ] == '#':
                          pass
                      else:list_cal[max_X - 1][max_Y ] = int('1') + list_cal[max_X - 1][max_Y ]
                      if list_cal[max_X - 1][max_Y + 1] == '#':
                          pass
                      else:list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]

                      if list_cal[max_X ][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X ][max_Y - 1] = int('1') + list_cal[max_X ][max_Y - 1]
                      if list_cal[max_X ][max_Y + 1] == '#':
                          pass
                      else: list_cal[max_X ][max_Y + 1] = int('1') + list_cal[max_X ][max_Y + 1]
                    if (max_X ==  4   and max_Y == 2):
                        if list_cal[max_X - 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X - 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]

                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                    if (max_X == 4    and max_Y == 3):
                        if list_cal[max_X - 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X - 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]

                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]

                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                    if (max_X ==  2   and max_Y == 2):
                        if list_cal[max_X - 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X - 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                        if list_cal[max_X + 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                        if list_cal[max_X + 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  3   and max_Y == 3) :
                      if list_cal[max_X - 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                      if list_cal[max_X - 1][max_Y ] == '#' :
                          pass
                      else: list_cal[max_X - 1][max_Y ] = int('1') + list_cal[max_X - 1][max_Y ]
                      if list_cal[max_X - 1][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                      if list_cal[max_X ][max_Y - 1] == '#' :
                          pass
                      else: list_cal[max_X ][max_Y - 1] = int('1') + list_cal[max_X ][max_Y - 1]
                      if list_cal[max_X ][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X ][max_Y + 1] = int('1') + list_cal[max_X ][max_Y + 1]
                      if list_cal[max_X + 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                      if list_cal[max_X + 1][max_Y ] == '#' :
                          pass
                      else:list_cal[max_X + 1][max_Y ] = int('1') + list_cal[max_X + 1][max_Y ]
                      if list_cal[max_X + 1][max_Y + 1] == '#' :
                          pass
                      else: list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  1   and max_Y == 2) :
                      if list_cal[max_X - 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                      if list_cal[max_X - 1][max_Y ] == '#' :
                          pass
                      else: list_cal[max_X - 1][max_Y ] = int('1') + list_cal[max_X - 1][max_Y ]
                      if list_cal[max_X - 1][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                      if list_cal[max_X ][max_Y - 1] == '#' :
                          pass
                      else: list_cal[max_X ][max_Y - 1] = int('1') + list_cal[max_X ][max_Y - 1]
                      if list_cal[max_X ][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X ][max_Y + 1] = int('1') + list_cal[max_X ][max_Y + 1]
                      if list_cal[max_X + 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                      if list_cal[max_X + 1][max_Y ] == '#' :
                          pass
                      else:list_cal[max_X + 1][max_Y ] = int('1') + list_cal[max_X + 1][max_Y ]
                      if list_cal[max_X + 1][max_Y + 1] == '#' :
                          pass
                      else: list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  2   and max_Y == 1) :
                      if list_cal[max_X - 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                      if list_cal[max_X - 1][max_Y ] == '#' :
                          pass
                      else: list_cal[max_X - 1][max_Y ] = int('1') + list_cal[max_X - 1][max_Y ]
                      if list_cal[max_X - 1][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                      if list_cal[max_X ][max_Y - 1] == '#' :
                          pass
                      else: list_cal[max_X ][max_Y - 1] = int('1') + list_cal[max_X ][max_Y - 1]
                      if list_cal[max_X ][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X ][max_Y + 1] = int('1') + list_cal[max_X ][max_Y + 1]
                      if list_cal[max_X + 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                      if list_cal[max_X + 1][max_Y ] == '#' :
                          pass
                      else:list_cal[max_X + 1][max_Y ] = int('1') + list_cal[max_X + 1][max_Y ]
                      if list_cal[max_X + 1][max_Y + 1] == '#' :
                          pass
                      else: list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  2   and max_Y == 3) :
                      if list_cal[max_X - 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                      if list_cal[max_X - 1][max_Y ] == '#' :
                          pass
                      else: list_cal[max_X - 1][max_Y ] = int('1') + list_cal[max_X - 1][max_Y ]
                      if list_cal[max_X - 1][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                      if list_cal[max_X ][max_Y - 1] == '#' :
                          pass
                      else: list_cal[max_X ][max_Y - 1] = int('1') + list_cal[max_X ][max_Y - 1]
                      if list_cal[max_X ][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X ][max_Y + 1] = int('1') + list_cal[max_X ][max_Y + 1]
                      if list_cal[max_X + 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                      if list_cal[max_X + 1][max_Y ] == '#' :
                          pass
                      else:list_cal[max_X + 1][max_Y ] = int('1') + list_cal[max_X + 1][max_Y ]
                      if list_cal[max_X + 1][max_Y + 1] == '#' :
                          pass
                      else: list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  3   and max_Y == 1) :
                      if list_cal[max_X - 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                      if list_cal[max_X - 1][max_Y ] == '#' :
                          pass
                      else: list_cal[max_X - 1][max_Y ] = int('1') + list_cal[max_X - 1][max_Y ]
                      if list_cal[max_X - 1][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                      if list_cal[max_X ][max_Y - 1] == '#' :
                          pass
                      else: list_cal[max_X ][max_Y - 1] = int('1') + list_cal[max_X ][max_Y - 1]
                      if list_cal[max_X ][max_Y + 1] == '#' :
                          pass
                      else:list_cal[max_X ][max_Y + 1] = int('1') + list_cal[max_X ][max_Y + 1]
                      if list_cal[max_X + 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                      if list_cal[max_X + 1][max_Y ] == '#' :
                          pass
                      else:list_cal[max_X + 1][max_Y ] = int('1') + list_cal[max_X + 1][max_Y ]
                      if list_cal[max_X + 1][max_Y + 1] == '#' :
                          pass
                      else: list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  4   and max_Y == 4) :
                      if list_cal[max_X - 1][max_Y - 1] == '#':
                          pass
                      else:list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                      if list_cal[max_X - 1][max_Y ] == '#' :
                          pass
                      else: list_cal[max_X - 1][max_Y ] = int('1') + list_cal[max_X - 1][max_Y ]

                      if list_cal[max_X ][max_Y - 1] == '#' :
                          pass
                      else: list_cal[max_X ][max_Y - 1] = int('1') + list_cal[max_X ][max_Y - 1]
                    if (max_X == 3 and max_Y == 2):
                        if list_cal[max_X - 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X - 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                        if list_cal[max_X + 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                        if list_cal[max_X + 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  1   and max_Y == 3):
                        if list_cal[max_X - 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X - 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                        if list_cal[max_X + 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                        if list_cal[max_X + 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  0   and max_Y == 1):
                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                        if list_cal[max_X + 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                        if list_cal[max_X + 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X ==  0   and max_Y == 4):
                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                        if list_cal[max_X + 1][max_Y - 1] == '#':
                            pass
                        else:list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                    if (max_X ==  4   and max_Y == 0):
                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X - 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                    if (max_X ==  2   and max_Y == 0):
                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X - 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                        if list_cal[max_X + 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X == 1 and max_Y == 0):
                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X - 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                        if list_cal[max_X + 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X == 3 and max_Y == 0):

                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X - 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y + 1] = int('1') + list_cal[max_X - 1][max_Y + 1]
                        if list_cal[max_X][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y + 1] = int('1') + list_cal[max_X][max_Y + 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                        if list_cal[max_X + 1][max_Y + 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y + 1] = int('1') + list_cal[max_X + 1][max_Y + 1]
                    if (max_X == 1 and max_Y == 4):
                            if list_cal[max_X - 1][max_Y - 1] == '#':
                                pass
                            else:
                                list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                            if list_cal[max_X - 1][max_Y] == '#':
                                pass
                            else:
                                list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                            if list_cal[max_X][max_Y - 1] == '#':
                                pass
                            else:
                                list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                            if list_cal[max_X + 1][max_Y - 1] == '#':
                                pass
                            else:
                                list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                            if list_cal[max_X + 1][max_Y] == '#':
                                pass
                            else:
                                list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                    if (max_X == 2 and max_Y == 4):
                        if list_cal[max_X - 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                        if list_cal[max_X - 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                        if list_cal[max_X][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                        if list_cal[max_X + 1][max_Y - 1] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                        if list_cal[max_X + 1][max_Y] == '#':
                            pass
                        else:
                            list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
                    if (max_X == 3 and max_Y == 4):
                            if list_cal[max_X - 1][max_Y - 1] == '#':
                                pass
                            else:
                                list_cal[max_X - 1][max_Y - 1] = int('1') + list_cal[max_X - 1][max_Y - 1]
                            if list_cal[max_X - 1][max_Y] == '#':
                                pass
                            else:
                                list_cal[max_X - 1][max_Y] = int('1') + list_cal[max_X - 1][max_Y]
                            if list_cal[max_X][max_Y - 1] == '#':
                                pass
                            else:
                                list_cal[max_X][max_Y - 1] = int('1') + list_cal[max_X][max_Y - 1]
                            if list_cal[max_X + 1][max_Y - 1] == '#':
                                pass
                            else:
                                list_cal[max_X + 1][max_Y - 1] = int('1') + list_cal[max_X + 1][max_Y - 1]
                            if list_cal[max_X + 1][max_Y] == '#':
                                pass
                            else:
                                list_cal[max_X + 1][max_Y] = int('1') + list_cal[max_X + 1][max_Y]
            max_Y = max_Y + 1
            if max_Y == 5:
                max_Y = 0
                break
            else:
                pass
        max_X = 1 + max_X
    max_X = 0
    max_Y = 0
    #print(type(list_cal[1][1]))
    #print(list_cal[1][1])
    """___ทำ ' '___"""
    while max_X != 5:
        ###############
        while max_Y != 5:
         for i in str(list_cal[max_X][max_Y]) :
             if i == '0' :
                 list_cal[max_X][max_Y] = '0'
             if i == '1' :
                 list_cal[max_X][max_Y] = '1'
             if i == '2' :
                 list_cal[max_X][max_Y] = '2'
             if i == '3' :
                 list_cal[max_X][max_Y] = '3'
             if i == '4' :
                 list_cal[max_X][max_Y] = '4'
             if i == '5' :
                 list_cal[max_X][max_Y] = '5'
             if i == '6' :
                 list_cal[max_X][max_Y] = '6'
             if i == '7' :
                 list_cal[max_X][max_Y] = '7'
             if i == '8' :
                 list_cal[max_X][max_Y] = '8'
             if i == '9' :
                 list_cal[max_X][max_Y] = '9'
             else:
                 pass
         max_Y  = max_Y +1
         if max_Y == 5:
            max_Y = 0
            break
         else:
            pass
        max_X = 1 + max_X
    return lst
print("*** Minesweeper ***")
lst_input = []
input_list = input("Enter input(5x5) : ").split(",") #"""""คั่นแยกด้วย , """''#
for e in input_list:
  lst_input.append([i for i in e.split()])
print("\n",*lst_input,sep = "\n")
print(*num_grid(lst_input),sep = "\n",end='')