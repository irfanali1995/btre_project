from django.shortcuts import render, redirect
from .models import Contact
from django.contrib  import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Checking Inquery already exist
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You already made an inquery for this property')
                return redirect('/listings/'+listing_id)
        
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Email 
        # send_mail(
        #     'Property Inquery',
        #     'There was inqury for ' + listing + '. Sign into admin for more details.',
        #     'irfan.ali1995@gmail.com',
        #     [realtor_email, 'irfan.ali1995@gmail.com'],
        #     fail_silently=False
        # )
        


        messages.success(request, 'Your query has been submitted, a realtor will get in touch soon')
 
        return redirect('/listings/'+listing_id)