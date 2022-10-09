def timeConversion(s):
    if s[-2:] == 'AM':
        s = s.replace("AM", "")
        if s[:2] == "12":
            return s.replace(s[:2], "00")
        return s
    elif s[-2:] == 'PM':
        s = s.replace("PM", "")
        if s[:1] == "0":
            return s.replace(s[:2], str(int(s[1:2]) + 12))
        elif s[:2] == "00":
            return s.replace(s[:2], str(int(s[:2]) + 12)) 
        elif s[:2] == "12":
            return s.replace(s[:2], "12")           
        else:
            return s.replace(s[:2], str(int(s[:2]) + 12))
            


if __name__ == '__main__':


    s = input()

    result = timeConversion(s)


