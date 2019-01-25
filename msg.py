import datetime
dname=['ra','sa','mi','dd','mp']
drate=[12,55,64,78,65]


unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""

def makemsg(names,rates):
    if len(names)==len(rates):
        i=0
        today=datetime.date.today()
        text = '{today.day}/{today.month}/{today.year}'.format(today=today)
        for name in names:
            amount = "%.2f" %(rates[i])
            newmsg = unf_message.format(
                name=name.capitalize(),
                date=text,
                total=amount
                )
            i=i+1
            print(newmsg)
                

makemsg(dname,drate)
