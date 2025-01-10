def assign_emoji(color):
    b, g, r = color[:]
    if 0<=b<=49 and 0<=g<=49 and 0<=r<=49:
        return 'black'
    elif 0<=b<=49 and 0<=g<=49 and 50<=r<=99:
        return 'brown'
    elif 0<=b<=49 and 0<=g<=49 and 100<=r<=149:
        return 'brown'
    elif 0<=b<=49 and 0<=g<=49 and 150<=r<=199:
        return 'red'
    elif 0<=b<=49 and 0<=g<=49 and 200<=r<=255:
        return 'red'
    elif 0<=b<=49 and 50<=g<=99 and 0<=r<=49:
        return 'green'
    elif 0<=b<=49 and 50<=g<=99 and 50<=r<=99:
        return 'green'
    elif 0<=b<=49 and 50<=g<=99 and 100<=r<=149:
        return 'orange'
    elif 0<=b<=49 and 50<=g<=99 and 150<=r<=199:
        return 'orange'
    elif 0<=b<=49 and 50<=g<=99 and 200<=r<=255:
        return 'orange'
    elif 0<=b<=49 and 100<=g<=149 and 0<=r<=49:
        return 'green'
    elif 0<=b<=49 and 100<=g<=149 and 50<=r<=99:
        return 'green'
    elif 0<=b<=49 and 100<=g<=149 and 100<=r<=149:
        return 'green'
    elif 0<=b<=49 and 100<=g<=149 and 150<=r<=199:
        return 'yellow'
    elif 0<=b<=49 and 100<=g<=149 and 200<=r<=255:
        return 'orange'
    elif 0<=b<=49 and 150<=g<=199 and 0<=r<=49:
        return 'green'
    elif 0<=b<=49 and 150<=g<=199 and 50<=r<=99:
        return 'green'
    elif 0<=b<=49 and 150<=g<=199 and 100<=r<=149:
        return 'green'
    elif 0<=b<=49 and 150<=g<=199 and 150<=r<=199:
        return 'yellow'
    elif 0<=b<=49 and 150<=g<=199 and 200<=r<=255:
        return 'yellow'
    elif 0<=b<=49 and 200<=g<=255 and 0<=r<=49:
        return 'green'
    elif 0<=b<=49 and 200<=g<=255 and 50<=r<=99:
        return 'green'
    elif 0<=b<=49 and 200<=g<=255 and 100<=r<=149:
        return 'green'
    elif 0<=b<=49 and 200<=g<=255 and 150<=r<=199:
        return 'yellow'
    elif 0<=b<=49 and 200<=g<=255 and 200<=r<=255:
        return 'yellow'
    elif 50<=b<=99 and 0<=g<=49 and 0<=r<=49:
        return 'blue'
    elif 50<=b<=99 and 0<=g<=49 and 50<=r<=99:
        return 'purple'
    elif 50<=b<=99 and 0<=g<=49 and 100<=r<=149:
        return 'purple'
    elif 50<=b<=99 and 0<=g<=49 and 150<=r<=199:
        return 'pink'
    elif 50<=b<=99 and 0<=g<=49 and 200<=r<=255:
        return 'pink'
    elif 50<=b<=99 and 50<=g<=99 and 0<=r<=49:
        return 'grey'
    elif 50<=b<=99 and 50<=g<=99 and 50<=r<=99:
        return 'grey'
    elif 50<=b<=99 and 50<=g<=99 and 100<=r<=149:
        return 'pink'
    elif 50<=b<=99 and 50<=g<=99 and 150<=r<=199:
        return 'pink'
    elif 50<=b<=99 and 50<=g<=99 and 200<=r<=255:
        return 'red'
    elif 50<=b<=99 and 100<=g<=149 and 0<=r<=49:
        return 'green'
    elif 50<=b<=99 and 100<=g<=149 and 50<=r<=99:
        return 'green'
    elif 50<=b<=99 and 100<=g<=149 and 100<=r<=149:
        return 'grey'
    elif 50<=b<=99 and 100<=g<=149 and 150<=r<=199:
        return 'brown'
    elif 50<=b<=99 and 100<=g<=149 and 200<=r<=255:
        return 'brown'
    elif 50<=b<=99 and 150<=g<=199 and 0<=r<=49:
        return 'green'
    elif 50<=b<=99 and 150<=g<=199 and 50<=r<=99:
        return 'green'
    elif 50<=b<=99 and 150<=g<=199 and 100<=r<=149:
        return 'green'
    elif 50<=b<=99 and 150<=g<=199 and 150<=r<=199:
        return 'yellow'
    elif 50<=b<=99 and 150<=g<=199 and 200<=r<=255:
        return 'orange'
    elif 50<=b<=99 and 200<=g<=255 and 0<=r<=49:
        return 'green'
    elif 50<=b<=99 and 200<=g<=255 and 50<=r<=99:
        return 'green'
    elif 50<=b<=99 and 200<=g<=255 and 100<=r<=149:
        return 'green'
    elif 50<=b<=99 and 200<=g<=255 and 150<=r<=199:
        return 'yellow'
    elif 50<=b<=99 and 200<=g<=255 and 200<=r<=255:
        return 'yellow'
    elif 100<=b<=149 and 0<=g<=49 and 0<=r<=49:
        return 'blue'
    elif 100<=b<=149 and 0<=g<=49 and 50<=r<=99:
        return 'purple'
    elif 100<=b<=149 and 0<=g<=49 and 100<=r<=149:
        return 'purple'
    elif 100<=b<=149 and 0<=g<=49 and 150<=r<=199:
        return 'pink'
    elif 100<=b<=149 and 0<=g<=49 and 200<=r<=255:
        return 'pink'
    elif 100<=b<=149 and 50<=g<=99 and 0<=r<=49:
        return 'blue'
    elif 100<=b<=149 and 50<=g<=99 and 50<=r<=99:
        return 'blue'
    elif 100<=b<=149 and 50<=g<=99 and 100<=r<=149:
        return 'purple'
    elif 100<=b<=149 and 50<=g<=99 and 150<=r<=199:
        return 'pink'
    elif 100<=b<=149 and 50<=g<=99 and 200<=r<=255:
        return 'pink'
    elif 100<=b<=149 and 100<=g<=149 and 0<=r<=49:
        return 'green'
    elif 100<=b<=149 and 100<=g<=149 and 50<=r<=99:
        return 'grey'
    elif 100<=b<=149 and 100<=g<=149 and 100<=r<=149:
        return 'grey'
    elif 100<=b<=149 and 100<=g<=149 and 150<=r<=199:
        return 'pink'
    elif 100<=b<=149 and 100<=g<=149 and 200<=r<=255:
        return 'brown'
    elif 100<=b<=149 and 150<=g<=199 and 0<=r<=49:
        return 'green'
    elif 100<=b<=149 and 150<=g<=199 and 50<=r<=99:
        return 'green'
    elif 100<=b<=149 and 150<=g<=199 and 100<=r<=149:
        return 'green'
    elif 100<=b<=149 and 150<=g<=199 and 150<=r<=199:
        return 'grey'
    elif 100<=b<=149 and 150<=g<=199 and 200<=r<=255:
        return 'orange'
    elif 100<=b<=149 and 200<=g<=255 and 0<=r<=49:
        return 'green'
    elif 100<=b<=149 and 200<=g<=255 and 50<=r<=99:
        return 'green'
    elif 100<=b<=149 and 200<=g<=255 and 100<=r<=149:
        return 'green'
    elif 100<=b<=149 and 0<=g<=49 and 150<=r<=199:
        return 'purple'
    elif 100<=b<=149 and 0<=g<=49 and 200<=r<=255:
        return 'pink'
    elif 100<=b<=149 and 50<=g<=99 and 150<=r<=199:
        return 'pink'
    elif 100<=b<=149 and 50<=g<=99 and 200<=r<=255:
        return 'pink'
    elif 100<=b<=149 and 100<=g<=149 and 150<=r<=199:
        return 'grey'
    elif 100<=b<=149 and 100<=g<=149 and 200<=r<=255:
        return 'pink'
    elif 100<=b<=149 and 150<=g<=199 and 150<=r<=199:
        return 'green'
    elif 100<=b<=149 and 150<=g<=199 and 200<=r<=255:
        return 'yellow'
    elif 100<=b<=149 and 200<=g<=255 and 150<=r<=199:
        return 'green'
    elif 100<=b<=149 and 200<=g<=255 and 200<=r<=255:
        return 'yellow'
    elif 150<=b<=199 and 0<=g<=49 and 0<=r<=49:
        return 'blue'
    elif 150<=b<=199 and 0<=g<=49 and 50<=r<=99:
        return 'blue'
    elif 150<=b<=199 and 0<=g<=49 and 100<=r<=149:
        return 'purple'
    elif 150<=b<=199 and 0<=g<=49 and 150<=r<=199:
        return 'pink'
    elif 150<=b<=199 and 0<=g<=49 and 200<=r<=255:
        return 'pink'
    elif 150<=b<=199 and 50<=g<=99 and 0<=r<=49:
        return 'blue'
    elif 150<=b<=199 and 50<=g<=99 and 50<=r<=99:
        return 'blue'
    elif 150<=b<=199 and 50<=g<=99 and 100<=r<=149:
        return 'purple'
    elif 150<=b<=199 and 50<=g<=99 and 150<=r<=199:
        return 'pink'
    elif 150<=b<=199 and 50<=g<=99 and 200<=r<=255:
        return 'pink'
    elif 150<=b<=199 and 100<=g<=149 and 0<=r<=49:
        return 'light_blue'
    elif 150<=b<=199 and 100<=g<=149 and 50<=r<=99:
        return 'light_blue'
    elif 150<=b<=199 and 100<=g<=149 and 100<=r<=149:
        return 'light_blue'
    elif 150<=b<=199 and 100<=g<=149 and 150<=r<=199:
        return 'pink'
    elif 150<=b<=199 and 100<=g<=149 and 200<=r<=255:
        return 'pink'
    elif 150<=b<=199 and 150<=g<=199 and 0<=r<=49:
        return 'light_blue'
    elif 150<=b<=199 and 150<=g<=199 and 50<=r<=99:
        return 'light_blue'
    elif 150<=b<=199 and 150<=g<=199 and 100<=r<=149:
        return 'light_blue'
    elif 150<=b<=199 and 150<=g<=199 and 150<=r<=199:
        return 'grey'
    elif 150<=b<=199 and 150<=g<=199 and 200<=r<=255:
        return 'pink'
    elif 150<=b<=199 and 200<=g<=255 and 0<=r<=49:
        return 'green'
    elif 150<=b<=199 and 200<=g<=255 and 50<=r<=99:
        return 'green'
    elif 150<=b<=199 and 200<=g<=255 and 100<=r<=149:
        return 'green'
    elif 150<=b<=199 and 200<=g<=255 and 150<=r<=199:
        return 'green'
    elif 150<=b<=199 and 200<=g<=255 and 200<=r<=255:
        return 'yellow'
    elif 200<=b<=255 and 0<=g<=49 and 0<=r<=49:
        return 'blue'
    elif 200<=b<=255 and 0<=g<=49 and 50<=r<=99:
        return 'blue'
    elif 200<=b<=255 and 0<=g<=49 and 100<=r<=149:
        return 'purple'
    elif 200<=b<=255 and 0<=g<=49 and 150<=r<=199:
        return 'purple'
    elif 200<=b<=255 and 0<=g<=49 and 200<=r<=255:
        return 'pink'
    elif 200<=b<=255 and 50<=g<=99 and 0<=r<=49:
        return 'blue'
    elif 200<=b<=255 and 50<=g<=99 and 50<=r<=99:
        return 'blue'
    elif 200<=b<=255 and 50<=g<=99 and 100<=r<=149:
        return 'purple'
    elif 200<=b<=255 and 50<=g<=99 and 150<=r<=199:
        return 'pink'
    elif 200<=b<=255 and 50<=g<=99 and 200<=r<=255:
        return 'pink'
    elif 200<=b<=255 and 100<=g<=149 and 0<=r<=49:
        return 'blue'
    elif 200<=b<=255 and 100<=g<=149 and 50<=r<=99:
        return 'light_blue'
    elif 200<=b<=255 and 100<=g<=149 and 100<=r<=149:
        return 'light_blue'
    elif 200<=b<=255 and 100<=g<=149 and 150<=r<=199:
        return 'pink'
    elif 200<=b<=255 and 100<=g<=149 and 200<=r<=255:
        return 'pink'
    elif 200<=b<=255 and 150<=g<=199 and 0<=r<=49:
        return 'light_blue'
    elif 200<=b<=255 and 150<=g<=199 and 50<=r<=99:
        return 'light_blue'
    elif 200<=b<=255 and 150<=g<=199 and 100<=r<=149:
        return 'light_blue'
    elif 200<=b<=255 and 150<=g<=199 and 150<=r<=199:
        return 'grey'
    elif 200<=b<=255 and 150<=g<=199 and 200<=r<=255:
        return 'pink'
    elif 200<=b<=255 and 200<=g<=255 and 0<=r<=49:
        return 'light_blue'
    elif 200<=b<=255 and 200<=g<=255 and 50<=r<=99:
        return 'light_blue'
    elif 200<=b<=255 and 200<=g<=255 and 100<=r<=149:
        return 'light_blue'
    elif 200<=b<=255 and 200<=g<=255 and 150<=r<=199:
        return 'white'
    elif 200<=b<=255 and 200<=g<=255 and 200<=r<=255:
        return 'white'
    else:
        print(b, g, r)
        return "novalue"
