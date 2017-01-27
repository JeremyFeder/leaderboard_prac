from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.urlresolvers import reverse
import random
from .models import Leaderboard

# Create your views here.
def index(request):
    #gold counter initialization
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        pass

    #activity display
    if 'action' not in request.session:
        request.session['action'] = []

    context = {
        'count': request.session['count'],
        'action': request.session['action']
    }

    return render(request, 'ninjagold/index.html', context)

def process(request):
    request.session['building'] = request.POST['building']
    building = request.session['building']

    if building == 'reset':
        request.session['count'] = 0
        request.session['action'] = []

    if building == 'farm':
        farm_gold = int(random.randrange(10,21))
        request.session['count'] += farm_gold
        addAction(request, farm_gold, 'earned', 'farm')
        print farm_gold

    if building == 'cave':
        cave_gold = int(random.randrange(5,11))
        request.session['count'] += cave_gold
        addAction(request, cave_gold, 'earned', 'cave')
        print cave_gold

    if building == 'house':
        house_gold = int(random.randrange(2,6))
        request.session['count'] += house_gold
        addAction(request, house_gold, 'earned', 'house')
        print house_gold

    if building == 'casino':
        casino_gold = int(random.randrange(-50,51))
        request.session['count'] += casino_gold
        if casino_gold >= 0:
            addAction(request, casino_gold, 'earned', 'casino')
        else:
            addAction(request, casino_gold, 'lost', 'casino')

        print casino_gold

    return redirect(reverse('ninjagold:index'))

def addAction(request, num, action, place):
    now = timezone.now()

    if place == 'farm':
        request.session['action'].insert(0,['earn', 'Earned %d from the %s! %s' % (num, place, now)])

    if place == 'cave':
        request.session['action'].insert(0,['earn', 'Earned %d from the %s! %s' % (num, place, now)])

    if place == 'house':
        request.session['action'].insert(0,['earn', 'Earned %d from the %s! %s' % (num, place, now)])

    if place == 'casino':
        if action == 'earned':
            earned = 'Earned %d from the casino! %s' % (num, now)
            request.session['action'].insert(0, ['earn', earned])
        else:
            lost = 'Entered the casino and lost %d gold... Ouch! %s' % (num, now)
            request.session['action'].insert(0, ['lost', lost])

    return redirect(reverse('ninjagold:index'))

# def save(request):
#     if not 'id' in request.session:
#         print "i failed"
#         return redirect('ninjagold:index')
#
#     print request.session['id'], "user id"
#     print request.session['email'], "user email"
#     print request.session['count'], "gold count (count)"
#
#     data = {
#         'id': request.session['id'],
#         'score': request.session['count'],
#     }
#
#     ## need to remove print statement once operational
#     print Leaderboard.objects.update_score(data)
#
#     return redirect('ninjagold:index')

def save(request):
    if request.method == "POST" and request.session['user_id']:

        data = {
            'score': request.session['count'],
            'user_id': request.session['user_id'],
        }
        



def logout(request):
    request.session.clear()
    return redirect(reverse('users:index'))
