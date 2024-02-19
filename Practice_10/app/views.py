from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    details = {
            
            "info": [
            {
                'id': '100001', 
                'name': 'Nova Solaris', 
                'courses': ['Math']
            }, 
            {
                'id': '100002', 
                'name': 'Kai Arashi', 
                'courses': ['History', 'Art']
            },
            {
                'id': '100003', 
                'name': 'Elara Whisperwind', 
                'courses': ['Programming', 'Music', 'Dance']
            }, 
            {
                'id': '100004', 
                'name': 'Corvus Blackwood', 
                'courses': ['Art', 'Science']
            }, 
            {
                'id': '100005', 
                'name': 'Amara Nightshade', 
                'courses': ['History', 'Science', 'Music']
            }, 
            {
                'id': '100006', 
                'name': 'Cassian Wynterfell', 
                'courses': ['Music', 'Math', 'Art', 'Science']
            }, 
            {
                'id': '100007', 
                'name': 'Lyra Silverthorne', 
                'courses': ['English', 'Music', 'Math']
            }, 
            {
                'id': '100008', 
                'name': 'Dorian Stormchaser ', 
                'courses': ['Music', 'Math', 'Science', 'Programming', 'History']
            }, 
            {
                'id': '100009', 
                'name': 'Rowan Emberheart', 
                'courses': ['Music', 'Math']
            }, 
            {
                'id': '100010', 
                'name': 'Zephryn Skyrider', 
                'courses': ['Science']
            }, 
            {
                'id': '100011', 
                'name': 'Aisling Moonshadow', 
                'courses': ['Science', 'Programming', 'History']
            }, 
            {
                'id': '100012', 
                'name': 'Cillian Thunderblade', 
                'courses': ['Art', 'History']
            }, 
            {
                'id': '100013', 
                'name': 'Selene Starlight ', 
                'courses': ['Music', 'Math', 'Art', 'Programming', 'History']
            }, 
            {
                'id': '100014', 
                'name': 'Ezra Duskbringer', 
                'courses': ['Science', 'Math']
            }, 
            {
                'id': '100015', 
                'name': 'Amara Sunrider ', 
                'courses': ['Art', 'Programming']
            }     
        ]}

    return render(request, 'app/index.html', details)
