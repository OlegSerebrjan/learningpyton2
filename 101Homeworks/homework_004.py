while True:
    try:
        id_code = input('Please enter ID code: ')
        int(id_code)
        if len(id_code) != 11:
            raise UserWarning
    except ValueError:
        print('Code you\'ve entered is not numeric')
        continue
    except UserWarning:
        if len(id_code) > 11:
            print('Too long')
        else:
            print('Too short')
        continue
    while True:
        user_choice = input('Please choose:\n'
                            '1.Print gender\n'
                            '2.Print date of birth\n'
                            '3.Print region of birth\n'
                            '4.Validate\n'
                            '5.Change ID\n'
                            '0.Exit\n'
                            '--->')
        if user_choice == '1':
            if id_code[0] not in ['0', '9']:
                if int(id_code[0]) % 2 == 0:
                    print('Code owner is a Female.')
                else:
                    print('Code owner is a Male. ')
            else:
                print('Code is not correct!')
                break
        elif user_choice == '2':
            if id_code[0] in ('1', '2'):
                bcent = '18'
            elif id_code[0] in ('3', '4'):
                bcent = '19'
            elif id_code[0] in ('5', '6'):
                bcent = '20'
            elif id_code[0] in ('7', '8'):
                bcent = '21'
            else:
                print('Code is not correct!')
                break
            print(f'You were born {id_code[5:7]}.{id_code[3:5]}.{bcent}{id_code[1:3]}')

        elif user_choice == '3':
            if int(id_code[7:10]) in range(0, 10):
                print('Your region of birth is Kuressaare')
            elif int(id_code[7:10]) in range(11, 20):
                print('Your region of birth is Tartu')
            elif int(id_code[7:10]) in range(21, 151):
                print('Your region of birth is Tallinn')
            elif int(id_code[7:10]) in range(151, 161):
                print('Your region of birth is Keila')
            elif int(id_code[7:10]) in range(161, 221):
                print('Your region of birth is Kardla')
            elif int(id_code[7:10]) in range(221, 271):
                print('Your region of birth is Kohtla-Jarve, endine Johvi')
            elif int(id_code[7:10]) in range(271, 371):
                print('Your region of birth is Tartu')
            elif int(id_code[7:10]) in range(371, 421):
                print('Your region of birth is Narva')
            elif int(id_code[7:10]) in range(421, 471):
                print('Your region of birth is Parnu')
            elif int(id_code[7:10]) in range(471, 491):
                print('Your region of birth is Haapsalu')
            elif int(id_code[7:10]) in range(491, 521):
                print('Your region of birth is Paide')
            elif int(id_code[7:10]) in range(521, 571):
                print('Your region of birth is Rakvere, Tapa')
            elif int(id_code[7:10]) in range(571, 601):
                print('Your region of birth is Valga')
            elif int(id_code[7:10]) in range(601, 651):
                print('Your region of birth is Viljandi')
            elif int(id_code[7:10]) in range(651, 701):
                print('Your region of birth is Voru')
            else:
                print('Code is not correct!')
                break
        elif user_choice == '4':
            if(((int(id_code[0]) * 1) + (int(id_code[1]) * 2) + (int(id_code[2]) * 3) + (int(id_code[3]) * 4) + (int(id_code[4]) * 5) + (int(id_code[5]) * 6) + (int(id_code[6]) * 7) + (int(id_code[7]) * 8) + (int(id_code[8]) * 9) + (int(id_code[9]) * 1)) % 11) == int(id_code[10]):
                print('Your code is validated')
            elif(((int(id_code[0]) * 3) + (int(id_code[1]) * 4) + (int(id_code[2]) * 5) + (int(id_code[3]) * 6) + (int(id_code[4]) * 7) + (int(id_code[5]) * 8) + (int(id_code[6]) * 9) + (int(id_code[7]) * 1) + (int(id_code[8]) * 2) + (int(id_code[9]) * 3)) % 11) == int(id_code[10]):
                print('Your code is validated')
            else:
                print('Your code is not validated')
        elif user_choice == '5':
            break
        elif user_choice == '0':
            print('Good bye!')
            quit()
        else:
            print('Choice is out of range!')

