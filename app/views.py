from django.shortcuts import render
from darksky import forecast
from datetime import date,timedelta,datetime

# Create your views here.
def home(request):
    nairobi = 1.2921, 36.8219
    weekday=date.today()

    with forecast('ff1ae3f99daa01d19c3a2b4c78868f01',*nairobi) as nairobi:
        for day in nairobi.daily:
            day = dict(day = date.strftime(weekday,'%a'), sum=day.summary,tempMin=day.temperatureMin,tempMax=day.temperatureMax)
            print('{day} ----{tempMin} - {tempMax}'.format(**day))
            weekday += timedelta(days=1)

    hour = datetime.now().hour
    location = forecast('ff1ae3f99daa01d19c3a2b4c78868f01', 1.2921, 36.8219)
    i= 0

    while hour < 24:
        temp = location.hourly[i].temperature

        if hour >12:
            print('{}pm -  {}'.format(hour-12,temp))
        else:
            print('{}am -  {}'.format(hour-12,temp))
        hour+=1
        i+=1
    



    return render(request,'home.html')
