from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Registration, Contact, Newsletter
import json

# Create your views here.
def Index(request):
    News = False
    Con = False

    if request.method == 'POST':
        try:
            response = request.POST['nemail']
            Newsletter.objects.create(Email=response)
            News = True
            Con = False

            send_msg_news(response)

        except:

            Email = request.POST['email']
            Phone = request.POST['phone']
            Topic = request.POST['service']
            Yourmsg = request.POST['yourmsg']
            Con = True
            News = False

            Contact.objects.create(Email=Email, Phone=Phone, Topic=Topic, Yourmessage=Yourmsg)

            send_msg_contact(Email)

    d = {"News": News, "Con": Con}
    return render(request, 'index.html', d)


def Registration_p(request):

    allready = False
    registered = False
    if request.method == 'POST':

        dd = request.POST
        Email = dd['email']
        Name = dd['name']
        About = dd['about']
        Type = dd['type']
        Worth = dd['worth']
        Condition = dd['condition']
        Team = dd['team']
        Hereaboutsarathii = dd['hereaboutsarathii']
        Helpyou = dd['helpyou']
        Yourrecentcustomers = dd['yourrecentcustomers']
        Address = dd['address']
        Streetnumber = dd['streetnumber']
        Zipcode = dd['zipcode']
        Service = dd['service']
        YourName = dd['yourName']
        Phone = dd['phone']
        Other = dd['other']

        data = Registration.objects.filter(Email=Email)

        if data:
            allready = True

        else:
            Registration.objects.create(Email=Email, Name=Name, About=About, Type=Type,
                                        Worth=Worth, Condition=Condition, Team=Team,
                                        Hereaboutsarathii=Hereaboutsarathii, Helpyou=Helpyou,
                                        Yourrecentcustomers=Yourrecentcustomers, Address=Address,
                                        Streetnumber=Streetnumber, Zipcode=Zipcode, Service=Service,
                                        YourName=YourName, Phone=Phone, other=Other)
            registered = True

            send_msg_reg(Email, Service)



    d = {"allready": allready, "registered": registered}
    return render(request, 'registration.html', d)


def send_msg_contact(email):
    subject, from_email, to = 'Sarathii : Query Recieved!!', 'sarathii.co@gmail.com', email
    text_content = ''
    html_content = '<h4>We got your query.</h4><br>' \
                   'Hi,<br><br>' \
                   'Hope you\'re doing well. This is a system generated mail. <br>' \
                   'We hereby inform you that we\'ve successfully received your ' \
                   'query regarding (the topic chosen).<br><br>' \
                   'We\'ll contact you soon on your provided email and no.<br><br><br>' \
                   '<p>Thank You for reaching us out..!!</P>' \
                   '<br><br>With Regards' \
                   '<br>Team Sarathii'

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()




def send_msg_news(email):
    subject, from_email, to = 'Sarathii : Subscribed Successfully!!', 'sarathii.co@gmail.com', email
    text_content = ''
    html_content = '<h3>You\'re on the way…</h3><br>Great job, keep yourself updated with us.' \
                   'Hi,<br><br>' \
                   'Hope you\'re doing well.You\'ve successfully subscribed for our email updates. ' \
                   'Now you\'ll receive the latest information regarding our plans and services.<br><br><br>' \
                   '<p>Thank You for being with us..</P>' \
                   '<br><br>With Regards' \
                   '<br>Team Sarathii'

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_msg_reg(email, service):
    subject, from_email, to = 'Registration Done!!', 'sarathii.co@gmail.com', email
    text_content = ''
    html_content = '<h4>Your Registration is Complete</h4><br>' \
                   '<p>You\'re in the right place to make your dreams come true..!!</p><br><br>' \
                   'Hi,<br><br>' \
                   'Hope you\'re doing well. You\'ve registered successfully for the {}. ' \
                   'We\'ll contact you on your given email and no. ' \
                   'soon after verifying your provided information.<br><br><br>' \
                   '<p>Thank You for reaching us out..!!</P>' \
                   '<br><br>With Regards' \
                   '<br>Team Sarathii'.format(service)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
