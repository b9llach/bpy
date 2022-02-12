import configparser
from datetime import datetime
import requests

class btime():
    def __init__(self):
        pass

    def time(self, military:str=None) -> str:
        now = datetime.now()
        time = now.strftime("%H:%M")

        if military:
            if military.lower() == 'true':
                if int(time.split(":")[0]) > 12:
                    return time + " PM"

                else:
                    if int(time.split(":")[0]) == 12:
                        return time + " PM"
                    else:
                        return time + " AM"

            elif military.lower() == 'false':
                if int(time.split(":")[0]) > 12:
                    nonmilitaryhour = int(time.split(":")[0]) - 12
                    militime = str(nonmilitaryhour) + ":" + str(time.split(":")[1])
                    return militime + " PM"

                else:
                    if int(time.split(":")[0]) == 12:
                        return time + " PM"
                    else:
                        return time + " AM"

            else:
                raise Exception("Unexpected parameter, military must either be 'True' or 'False'")

        elif not military:
            if int(time.split(":")[0]) > 12:
                return time + " PM"

            else:
                if int(time.split(":")[0]) == 12:
                    return time + " PM"
                else:
                    return time + " AM"

    def date(self, format=None, names=None, seperator=None) -> str:
        monthFromNum = {'01':"January",'02':"February",'03':"March",'04':"April",'05':"May",
                        '06':"June",'07':"July",'08':"August",'09':"September",'10':"October",
                        '11':"November",'12':"December"}

        suffix = {'1':'st','2':'nd','3':'rd'}
        from datetime import date
        today = date.today()
        year = str(today).split("-")[0]
        month = str(today).split("-")[1]
        day = str(today).split("-")[2]

        if format.lower() == 'dmy':
            today = f'{day}-{month}-{year}'
            if names:
                if names.lower() == 'true':
                    today = f'{day}-{monthFromNum[str(month)]}-{year}'

            if seperator:
                today = today.replace("-",seperator)

            return today

        elif format.lower() == 'mdy':
            today = f'{month}-{day}-{year}'
            if names:
                if names.lower() == 'true':
                    today = f'{monthFromNum[str(month)]}-{day}-{year}'

            if seperator:
                today = today.replace("-",seperator)

            return today

        elif format.lower() == 'ymd':
            today = f'{year}-{month}-{day}'
            if names:
                if names.lower() == 'true':
                    today = f'{year}-{monthFromNum[str(month)]}-{day}'

            if seperator:
                today = today.replace("-",seperator)

            return today

        elif format.lower() == 'formal':
            endingDigit = day[-1]
            suffixForNum = 'th'
            for key in suffix.keys():
                if key == endingDigit:
                    suffixForNum = suffix[key]
                    if key == '1':
                        if int(day) > 10 and int(day) < 21:
                            suffixForNum = 'th'

                        elif int(day) > 20:
                            suffixForNum = 'st'



            return f'{monthFromNum[str(month)]} {day}{suffixForNum}, {year}'

        elif format == None:
            today = f'{year}-{month}-{day}'
            if names:
                if names.lower() == 'true':
                    today = f'{year}-{monthFromNum[str(month)]}-{day}'

            if seperator:
                today = today.replace("-",seperator)

            return today

    def secondsToMinutes(self, seconds) -> str:
        secondsLeftOver = seconds % 60
        if secondsLeftOver < 10:
            secondsLeftOver = '0' + str(secondsLeftOver)

        minutesDecimal = seconds / 60
        minutesNonDecimal = str(minutesDecimal).split('.')[0]

        return f'{minutesNonDecimal}:{str(secondsLeftOver).split(".")[0]}'

    def minutesToHours(self, minutes):
        minutesLeftOver = minutes % 60
        hoursDecimal = minutes / 60
        if hoursDecimal > 0:
            hours = str(hoursDecimal).split(".")[0]
        else:
            hours = 0

        return f'{hours}h {minutesLeftOver}m'

class bjson:
    def fetchResponse(self, url: str) -> int:
        try:
            response = requests.get(url)
            return response.status_code
        except:
            return -1

    def fetchJson(self, url: str) -> int:
        try:
            response = requests.get(url)
            data = response.json()
            return data
        except:
            return -1

    def fetchHeaders(self, url: str):
        try:
            response = requests.get(url)
            data = response.headers
            return data
        except:
            return -1

class bconfig:

    def read_config(self, path: str, delim: str = None) -> dict:
        output = {}
        if not delim:
            delim = "="
        with open(path, 'r') as cfg:
            for line in cfg:
                output[line.split(delim)[0].replace("\n", "")] = line.split(delim)[1].replace("\n", "")
        return output

    def save_config(self, settings: dict, path: str, delim: str = None) -> bool:
        if not delim:
            delim = "="
        with open(path, 'w+') as cfg:
            for key in settings:
                cfg.write(f"{key}{delim}{settings[key]}\n")
        return True

