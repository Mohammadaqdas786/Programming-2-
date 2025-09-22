def main(password=None):
    """determine if the password is vaild """
    get_password( password )
    while len( password ) < 8:
        print( "password is doesnt have meet minimum length" )
        get_password( password )

    print( "*" * len( password ) )


def get_password(password):
    """get user input"""
    password = input( "Enter password" )
    return password


main()
