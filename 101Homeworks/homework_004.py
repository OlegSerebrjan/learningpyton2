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
            pass
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            break
        elif user_choice == '0':
            print('Good bye!')
            quit()
        else:
            print('Choice is out of range!')

