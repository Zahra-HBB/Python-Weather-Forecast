from flask import Flask, render_template, request

app = Flask(__name__)
cityDict={}
weatherInfo={"london": "25", "tehran":"30","melbourne":"20"}


@app.route("/",methods=['GET'])
def getWeatherForecast():
    return render_template('index.html')

@app.route("/",methods=['POST'])  
def lookupWeatherForcast():
    cityName = request.form.get('cityName')
    cityWeather = lookupInCache(cityName)
    if cityWeather is None:
        weatherApi = callWeatherApi(cityName)
        if weatherApi is None:
            weather = "There is no data!"
        else:
            weather = weatherApi
            addInCache(cityName,weather)
    else:
        weather = cityWeather

    return render_template('index.html', weather = weather ,cityName=cityName)

def lookupInCache(cityName):
    hashCityName = hash(cityName)
    if (hashCityName in cityDict):
        return cityDict[hashCityName]
    else:
        return None

def addInCache(cityName,cityWeather):
    hashCityName = hash(cityName)
    cityDict[hashCityName] = cityWeather


def callWeatherApi (cityName):
    if (cityName in weatherInfo):
        return weatherInfo[cityName]
    else:
        return None

if __name__ == '__main__':
    app.run()      




