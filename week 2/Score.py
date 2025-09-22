import random


def main():
    """print user input score result and random score result"""
    score = float( input( "Enter score:" ) )
    print( get_result( score ) )
    random_score = random.randit( 0, 100 )
    print( get_result( random_score ) )


def get_result(score):
    """determine the result based on score"""
    if score < 0 or score > 100:
        return "invaild score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "passable"
        else:
            return "bad"


main()
