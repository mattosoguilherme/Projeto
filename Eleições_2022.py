def collor_yellow(phrase):
    from sty import fg, bg, ef, rs
    new_phrase=fg.li_yellow + '' + fg.rs


def line():
    print()
    print("-="*40)
    print()

def vote():
    pass

def electoral_age(voter_age):
    if 18 <= voter_age < 70:
        return "Your vote is mandatory, if you do not vote you will pay a fine of R$3.50"
        
