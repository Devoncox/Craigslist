from tkinter import *
from Craigslist import PostToCraigs
window = Tk()

window.title("Craigslist Posting")
window.geometry('700x700')

posted = [0]

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func



# City Menu
cities = ['Phoenix', 'San Diego', 'Tucson', 'Dallas', 'New York', 'Houston', 'North Jersey', 'Atlanta', 'Miami']
selected_city = StringVar()


selected_city.set("Select City")
city_menu = OptionMenu(window, selected_city, *cities)
city_menu.grid(column=0, row=0)

selected_region = StringVar()
selected_region.set("Select Region")


regions = ['Central', 'East', 'North', 'West', 'South', 'WestChester']
region_menu = OptionMenu(window, selected_region, *regions)
region_menu.grid(column=3, row=0)


# Medium Menu
mediums = ['Job', 'Gig']
selected_medium = StringVar()
selected_medium.set("Select Medium")
medium_menu = OptionMenu(window, selected_medium, *mediums)
medium_menu.grid(column=6, row=0)


# Header Menu
Cook_Header = ['COOKS - WORK WHEN YOU WANT SAME DAY PAY',
                'COOKS - NEED MONEY ASAP? START WORKING TODAY WITH QWICK.',
                 'COOKS - WORK WHEN AND WHERE YOU WANT',
                'COOKS - Be your own boss; work when and where you want',
                'COOKS - Pay for Summer Vacation by picking up extra shifts today!']

Server_Header = ['BANQUET SERVERS - WORK WHEN YOU WANT SAME DAY PAY',
                'BANQUET SERVERS - NEED MONEY ASAP? START WORKING TODAY WITH QWICK.',
                 'SERVERS - WORK WHEN AND WHERE YOU WANT']

Bartender_Header = ['BARTENDERS - WORK WHEN YOU WANT SAME DAY PAY',
                'BARTENDERS - NEED MONEY ASAP? START WORKING TODAY WITH QWICK.',
                 'BARTENDERS - WORK WHEN AND WHERE YOU WANT']

GL_Header = ['Dishwashing - Pick Up Gigs That Work For You',
             'Bussers - Shifts Straight to you',
             'DISHWASHERS - WORK WHEN YOU WANT SAME DAY PAY',
             'BUSSERS - WORKER WHEN YOU WANT SAME DAY PAY']

Concession_headers = ['CONCESSION WORKERS NEEDED: WORK THE MOST TELEVISED EVENT OF THE YEAR']


headers =  Server_Header + Cook_Header + Bartender_Header + GL_Header + Concession_headers

selected_header = StringVar()
selected_header.set("Select Header")
header_menu = OptionMenu(window, selected_header, *headers)
header_menu.grid(column=9, row=0)





def PostValuesToCraigs():
    new_cities = ['New York', 'Atlanta']
    city = selected_city.get()
    region = selected_region.get()
    medium = selected_medium.get()

    header = selected_header.get()
    utm_link = 'https://www.qwick.com/professionals/?utm_source=Craigslist&utm_medium=' + medium + '&utm_term=' + city.replace(" ", "") + '&utm_content=' + header.replace(" ", "")

    html = " "
    if header in Concession_headers:
        html = """ <font face="Helvetica">
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/10/Qwick-LogoLight-1.png"alt="Banner"align="middle"width="25%"></a>
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/11/Craigslist-ad.jpg"alt="Banner"width="65%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       <font size="5"><b>Take control of your schedule and income</b></font>
       <br><br>
       Sign up as a concession worker TODAY and have the chance to work one of the most exciting events of the year at Hard Rock Stadium in February, as well as hundreds of other shifts! Plus, get paid THE SAME DAY!
       <br><br> 
       *All workers MUST pass a background check in order to fill shifts. 
       <br><br>
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/11/Copy-of-Untitled-7.png"alt="Banner"width="55%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       Help us change the future of work."""
    if header in Server_Header:
        html = """ <font face="Helvetica">
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/10/Qwick-LogoLight-1.png"alt="Banner"align="middle"width="25%"></a>
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/09/2.png"alt="Banner"width="65%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       <font size="5"><b>Take control of your schedule and income</b></font>
       <br><br>
       When you join the Qwick Platform, you control your own schedule, allowing you to work how and when you want.
       <br><br>
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/11/Copy-of-Untitled-7.png"alt="Banner"width="55%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       Help us change the future of work."""
    if header in Cook_Header:
        html =  """ <font face="Helvetica">
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/10/Qwick-LogoLight-1.png"alt="Banner"align="middle"width="25%"></a>
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/09/3.png"alt="Banner"width="65%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       <font size="5"><b>Take control of your schedule and income</b></font>
       <br><br>
       When you join the Qwick Platform, you control your own schedule, allowing you to work how and when you want.
       <br><br>
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/11/Copy-of-Untitled-7.png"alt="Banner"width="55%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       Help us change the future of work."""

    if header in Bartender_Header:
        html = """ <font face="Helvetica">
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/10/Qwick-LogoLight-1.png"alt="Banner"align="middle"width="25%"></a>
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/09/1.png"alt="Banner"width="65%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       <font size="5"><b>Take control of your schedule and income</b></font>
       <br><br>
       When you join the Qwick Platform, you control your own schedule, allowing you to work how and when you want.
       <br><br>
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/11/Copy-of-Untitled-7.png"alt="Banner"width="55%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       Help us change the future of work."""
    if header in GL_Header:
        html = """ <font face="Helvetica">
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/10/Qwick-LogoLight-1.png"alt="Banner"align="middle"width="25%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       <font size="5"><b>Take control of your schedule and income</b></font>
       <br><br>
       When you join the Qwick Platform, you control your own schedule, allowing you to work how and when you want.
       <br><br>
       <a href=""" + utm_link + """ rel="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/11/Copy-of-Untitled-7.png"alt="Banner"width="55%"></a>
       <br><br>
       <a href=""" + utm_link + """"="nofollow"><img src="https://www.qwick.com/wp-content/uploads/2019/04/craigslist-btn-sign-up.png" alt="Sign Up Button" width="270" height="80"></a>
       <br><br>
       Help us change the future of work."""


    pay = 'Work when you want, Earn what you need'
    med_value = " "
    if medium == 'Job':
        med_value = str(1)
    if medium == 'Gig':
        med_value = str(2)

    return PostToCraigs(city, region, medium, header, html, pay, med_value)


def DisableButton():
    post_btn.config(state='disabled')


def EnableButton():
    post_btn['state'] = 'normal'


def increment():
    posted[0] += 1
    label.config(text="You've Posted "+str(posted[0])+" times!")


label = Label(window, text="You've not posted yet")
label.grid(column=10, row=10)


def BtnClick():
    DisableButton()
    try:
        PostValuesToCraigs()
        increment()
    finally:
        EnableButton()


post_btn = Button(window, text='Post', command=PostValuesToCraigs)
post_btn.grid(column=9, row=10)








window.mainloop()