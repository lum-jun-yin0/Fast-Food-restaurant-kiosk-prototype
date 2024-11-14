import speech_recognition as sr
import pyaudio
from gtts import gTTS
from time import sleep
import os
import pyglet
from wit import Wit
from deep_translator import GoogleTranslator
from collections import Counter
import streamlit as st
init_rec = sr.Recognizer()
client = Wit('WA3HQBZ3B3HWDJ77X5WOCKVW7JM5MF3S') #Token for Wit
placeholder = st.empty()
placeholderlan = st.empty()
placeholder_speech = st.empty()
placeholder_tts= st.empty()
placeholder_stt = st.empty()
placeholderbutton = st.empty()
placeholder_speech1 = st.empty()
placeholder_speech2 = st.empty()
st.title("Fast Food restaurant kiosk prototype")
count=0
count1=0
count2=0
count4=0
count5=0
costs=0.0
burger=0
burgwfries=0
fries=0
drinks=0
order=0
duration1=0
price=[]
food=[]
yes=True
card=False
paynow=False
error=False
filename = './temp.mp3'
text=''
lan=''
burg=''
drink_append=''
drink_size=''
drink_type=''
fries_food=''
fries_size=''
bottlecup='cup'
dinein_out=''
speech=''
resp=''
say=''
langua='en'
yousaid='You said: '

def empty_placeholder():
    placeholder.empty()
    placeholderlan.empty()
    placeholder_speech.empty()
    placeholder_speech1.empty()
    placeholder_speech2.empty()
    placeholder_tts.empty()
    placeholder_stt.empty()
    placeholderbutton.empty()

def yes_no():
    global say
    say="Please say yes or no."
    speeching()
    Textts()

def speechtthello():
    global speech
    global say
    global count
    global placeholder_stt
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=5)
        try:
            speech = init_rec.recognize_google(audio_data, language=langua)
        except sr.UnknownValueError:
            count=1
    
    if count == 0:
        placeholder_stt.markdown(yousaid + speech)
        sleep(2)
        empty_placeholder()

def speechtt():
    global speech
    global say
    global placeholder_stt
    global count
    with placeholder_stt.container():
        st.markdown("Let's speak!!")
        with sr.Microphone() as source:
            audio_data = init_rec.record(source, duration=5)
            st.markdown("Recognizing your text.............")
            try:
                speech = init_rec.recognize_google(audio_data, language=langua)
            except sr.UnknownValueError:
                say = 'sorry could you please repeat?'
                st.markdown(say)
                Textts()
                sleep(2)
                count = 1
    if count == 0:
        placeholder_stt.empty()
        
        if langua != 'en':
            translatespeechtolang()
        else:
            yes=True
        
        speeching_stt()
        sleep(2)
    else:
        placeholder_stt.empty()

def speechtt1():
    global speech
    global error
    global placeholder_stt
    global count5
    global yes
    global langua

    with placeholder_stt.container():
        st.markdown("Let's speak!!")
        with sr.Microphone() as source:
            audio_data = init_rec.record(source, duration=5)
            st.markdown("Recognizing your text.............")
            try:
                speech = init_rec.recognize_google(audio_data, language=langua)
            except sr.UnknownValueError:
                error=True
                sleep(2)
                count5 = 1
    if count5 == 0:
        placeholder_stt.empty()
        error=False

        if 'english' or 'English' in speech:
            langua='en'
        elif 'malay' or 'Malay' in speech:
            langua='ms'
        else:
            yes=True

        if langua != 'en':
            translatespeechtolang()
        else:
            yes=True

        speeching_stt()
        sleep(2)
    else:
        placeholder_stt.empty()

def speechttstart():
    global langua
    global count1
    global speech
    langua='zh-CN'
    speechtt1()

    if 'English' or 'english' or 'one' or 'One' or '1' in speech:
        langua='en'
    elif 'Malay' or 'malay' or 'two' or 'Two' or '2' in speech:
        langua='ms'

    if error!=True:
        count1=0
    else:
        langua='en'
        speechtt1()
        if error!=True:
            count1=0
        else:
            count1=1

def Textts():
    global music
    global filename
    global count4
    global placeholder_tts
    global duration1
    
    try:
        os.remove(filename)
    except:
        yes=True

    if langua != 'en':
        translatetolang()

    tts = gTTS(text=say, lang=langua)
    tts.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration)

    try:
        os.remove(filename)
    except:
        yes=True

def speeching():
    global say
    global placeholder_speech

    if langua != 'en':
        translatetolang()
    else:
        yes=True

    with placeholder_speech.container():
        st.markdown(say)
        st.markdown("\n")

def speeching_stt():
    global say
    global placeholder_speech

    if langua != 'en':
        translatetolang()
    else:
        yes=True

    with placeholder_speech.container():
        st.markdown(yousaid + speech)
        st.markdown("\n")

def speechingstart():
    global say
    global langua
    global placeholder_speech
    with placeholder_speech.container():
        st.markdown(say)
        st.markdown("\n")
        langua='zh-CN'
        translatetolang()
        st.markdown(say)
        langua='ms'
        translatetolang()
        st.markdown(say)
        langua='en'

def speechingstart1():
    global say
    global langua
    global placeholder_speech1
    with placeholder_speech1.container():
        st.markdown(say)
        st.markdown("\n")
        langua='zh-CN'
        translatetolang()
        st.markdown(say)
        langua='ms'
        translatetolang()
        st.markdown(say)
        translatebacktoEn()
        langua='en'

def speechingstart2():
    global say
    global langua
    global placeholder_speech2
    with placeholder_speech2.container():
        st.markdown(say)
        st.markdown("\n")
        langua='zh-CN'
        translatetolang()
        st.markdown(say)
        langua='ms'
        translatetolang()
        st.markdown(say)
        translatebacktoEn()
        langua='en'

def detecthello():
    global count
    global placeholder
    if speech != '':
        if 'hello:hello' in resp:
            count=0
            placeholder.markdown("Starting...")
            sleep(2)
        else:
            count=1
    else:
        count=1

def langualoop():
    global placeholder
    while True:
        if count1 != 0:
            languloop()
            langu()
        else:
            empty_placeholder()
            break

def languastart():
    langustart()
    langu()

def langustart():
    global langua
    global say

    langua='en'
    say='Please speak after these instructions.'
    speechingstart()
    say='Please speak after these instructions.'
    Textts()

    langua='zh-CN'
    Textts()

    langua='ms'
    Textts()

    langua='en'
    say='Hello, what is your preferred language? We have, Option 1, English, Option 2, Chinese and Option 3, Malay.'
    speechingstart1()
    say = 'Hello, what is your preferred language? We have, Option 1, English, Option 2, Chinese and Option 3, Malay.'
    Textts()

    langua='zh-CN'
    Textts()
    
    langua='ms'
    Textts()

    langua='en'
    say='Please speak now.'
    speechingstart2()
    say='Please speak now.'
    Textts()

    langua='zh-CN'
    Textts()

    langua='ms'
    Textts()
    sttstart_witt1()

def langu():
    global langua
    global lan
    global say
    global count1
    global count2
    if 'English:English' in resp:
        langua='en'
        lan='English'
        empty_placeholder()
        count1 = 0
        count2=0
    elif 'Chinese:Chinese' in resp:
        langua='zh-CN'
        lan='Chinese'
        empty_placeholder()
        count1 = 0
        count2=0
    elif 'Malay:Malay' in resp:
        langua='ms'
        lan='Malay'
        empty_placeholder()
        count1 = 0
        count2=0
    elif 'one:one' in resp:
        langua='en'
        lan='English'
        empty_placeholder()
        count1 = 0
        count2=0
    elif 'two:two' in resp:
        langua='zh-CN'
        lan='Chinese'
        empty_placeholder()
        count1 = 0
        count2=0
    elif 'three:three' in resp:
        langua='ms'
        lan='Malay'
        empty_placeholder()
        count1 = 0
        count2=0
    else:
        count1=1
    
    if count1 != 0:
        count2=1
    else:
        say='To confirm, you have chosen ' + lan + ' as your preferred language, correct?'
        speeching()
        Textts()
        yes_no()
        stt_witt1()

def languloop():
    global langua
    global count2
    global say
    
    speechingstart.empty()
    speechingstart2.empty()
    langua='en'
    say='Sorry, could you please repeat your answer?'
    speechingstart()
    say='Sorry, could you please repeat your answer?'
    Textts()

    langua='zh-CN'
    Textts()

    langua='ms'
    count2=0
    Textts()

    sttstart_witt1_langu()

def yesno():
    global say
    global count1
    global order
    if 'yes:yes' in resp:
        say='Alright. Moving on,'
        count1=0
        order=0
    else:
        say='Sorry, could you please repeat your answer for the following question:'
        count1=1
        order=1
    speeching()
    Textts()
    sleep(2)
    placeholder.empty()

def hello():
    global say
    global count
    say="Welcome to ZQJ's fast food restaurant. We humbly welcome your presence. How may we assist you?"
    speeching()
    Textts()
    sleep(3)
    count=1

def dineinout():
    global say
    
    say='Would you like to choose Option 1. Dine In or Option 2. Take Away?'
    speeching()
    tts_stt_witt()

def detectdineinout():
    global count
    global say
    global dinein_out
    
    count = 0
    if 'dinein:dinein' in resp:
        say='you have chosen Dine In, is that correct?'
        dinein_out='dine in'
    elif 'takeout:takeout'  in resp:
        say='you have chosen Take Out, is that correct?'
        dinein_out='take away'
    elif 'one:one' in resp:
        say='you have chosen Dine In, is that correct?'
        dinein_out='dine in'
    elif 'two:two' in resp:
        say='you have chosen Take Out, is that correct?'
        dinein_out='take away'
    else:
        count = 1
    
    if count == 0:
        speeching()
        Textts()
        yes_no()
        stt_witt()
    else:
        yes=True

def yesno1():
    global say
    global count
    global order
    
    if 'yes:yes' in resp:
        say='Alright. Moving on,'
        count=0
    else:
        say='Sorry, could you please repeat your answer the following question:'
        count=1
    speeching()
    Textts()
    sleep(2)
    placeholder.empty()

def speech_ordering():
    global say
    say='Our top 3 recommendations are, sitting at number 1, the Chicken Burger with fries, followed by our famous coke and lastly, the Double Chicken burger. Do Note that you have to say the type of food items u want first.'
    speeching()
    Textts()

def ordering():
    global burger
    global burgwfries
    global fries
    global drinks
    global count
    global order
    global say
    global resp
    global yes
    
    say= 'The options you have are as followed: Option 1. burger, Option 2.burger with fries, Option 3. fries or Option 4. drinks.'
    speeching()
    tts_stt_witt()

    if 'burger:burger' in resp:
        burger=1
        order=1
        count=3
    elif 'burgwfries:burgwfries' in resp:
        say='To confirm, you have ordered one burger with a side of fries correct?'
        speeching()
        burgwfries=1
        order=1
        count=2
    elif 'fries:fries' in resp:
        say='Sure, what kind of fries would you like? We have Option 1. Small, Option 2. Medium or Option 3. Large fries available.'
        speeching()
        fries=1
        order=1
        count=0
    elif "sidedrink:sidedrink" in resp:
        say='Sure, what kind of drinks would you want, we have a few popular options, mainly Option 1. Coca-Cola, Option 2. Sprite, Option 3. Latte or Option 4. Cappuccino.'
        speeching()
        drinks=1
        order=1
        count=0
    elif 'one:one' in resp:
        burger=1
        order=1
        count=3
    elif 'two:two' in resp:
        say='To confirm, you have ordered one burger with a side of fries correct?'
        speeching()
        burgwfries=1
        order=1
        count=2
    elif 'three:three' in resp:
        say='Sure, what kind of fries would you like? We have Option 1. Small, Option 2. Medium or Option 3. Large fries available.'
        speeching()
        fries=1
        order=1
        count=0
    elif 'four:four' in resp:
        say='Sure, what kind of drinks would you want, we have a few popular options, mainly Option 1. Coca-Cola, Option 2. Sprite, Option 3. Latte or Option 4. Cappuccino.'
        speeching()
        drinks=1
        order=1
        count=0
    else:
        say='Sorry, could you repeat your order?'
        speeching()
        count=1
    
    if count == 0:
        tts_stt_witt()
    elif count == 2:
        Textts()
        yes_no()
        stt_witt()
        count=0
    elif count == 3:
        count=0
    else:
        Textts()

def ordering_loop():
    while True:
        if order != 0 and burger != 0:
            orderburger()

        elif order != 0 and fries != 0:
            orderfries()

        elif order != 0 and burgwfries != 0:
            yesno()
            if order==0:
                order_burger()
                burger=0
                yesno_ordering()
            else:
                while True:
                    order_burger()
                    if burger!=0:
                        burger=0
                        break
                    else:
                        order_burger()

            if order == 0:
                orderfries()
                fries=0
                order=0

            else:
                order = 1
                burgwfries = 1
                drinks=0

        elif order != 0 and drinks != 0:
            drinktype()

            if order == 0 and drink_type == 'Coke':
                drinksize()
                break

            elif order == 0 and drink_type == 'Sprite':
                drinksize()
                break

            elif order == 0 and drink_type == 'Latte':
                break

            elif order == 0 and drink_type == 'Cappuccino':
                break

            else:
                order = 1
                drinks = 1

        else:
            ordering()

        if order == 0:
            break

def yesno_ordering():
    global order
    global say
    empty_placeholder()

    if 'yes:yes' in resp:
        say='Alright. Moving on,'
        order=0
        cost()
    else:
        order = 1

    if order != 0:
        yes=True
    else:
        speeching()
        Textts()
        sleep(2)
        empty_placeholder()

def order_burger_speech():
    global say
    say='What kind of burger would you like? We have Option 1. Chicken burger, Option 2. Beef burger, Option 3. Double Chicken burger or Option 4. Double Beef burger available.'
    speeching()
    tts_stt_witt()

def order_burger():
    global burg
    global food
    global say
    global burger
    global yes

    if 'chicken:chicken' in resp:
        burg='Chicken Burger'
    elif 'beef:beef' in resp:
        burg='Beef Burger'
    elif 'douchicken:douchicken' in resp:
        burg='Double Chicken Burger'
    elif 'doubeef:doubeef' in resp:
        burg='Double Beef Burger'
    elif 'one:one' in resp:
        burg='Chicken Burger'
    elif 'two:two' in resp:
        burg='Beef Burger'
    elif 'three:three' in resp:
        burg='Double Chicken Burger'
    elif 'four:four' in resp:
        burg='Double Beef Burger'
    
    say='To confirm, you ordered 1 ' +  burg + ' correct?'
    speeching()
    Textts()
    yes_no()
    burger=0
    food.append(burg)
    stt_witt()

def orderburger():
    order_burger_speech()
    order_burger()
    empty_placeholder()
    yesno_order()

def order_fries():
    global burg
    global fries_size
    global fries_food
    global food
    global say
    global order
    global fries

    if burg!='':
        say="What kind of fries would you like? We have Option 1. Small fries, Option 2. Medium fries or Option 3. Large fries available."
        speeching()
        tts_stt_witt()

    if 'small:small' in resp:
        fries_size='Small'
    elif 'medium:medium' in resp:
        fries_size='Medium'
    elif 'large:large' in resp:
        fries_size='Large'
    elif 'one:one' in resp:
        fries_size='Small'
    elif 'two:two' in resp:
        fries_size='Medium'
    elif 'three:three' in resp:
        fries_size='Large'
    else:
        order+=1
        fries+=1
    
    say='To confirm, you ordered a side of' + fries_size + 'fries, correct?'
    speeching()
    Textts()
    yes_no()
    
    fries_food = fries_size + 'fries'
    food.append(fries_food)
    fries_food = ''
    order-=1
    fries-=1
    stt_witt()

def orderfries():
    order_fries()
    yesno_order()
    empty_placeholder()

def order_drink_type():
    global order
    global drink_type
    global drinks
    global say
    global bottlecup
    global food
    if 'coke:coke' in resp:
        drink_type='Coke'
    elif 'sprite:sprite' in resp:
        drink_type='Sprite'
    elif 'latte:latte' in resp:
        drink_type='Latte'
    elif 'cappuccino:cappuccino' in resp:
        drink_type='Cappuccino'
    elif 'one:one' in resp:
        drink_type='Coke'
    elif 'two:two' in resp:
        drink_type='Sprite'
    elif 'three:three' in resp:
        drink_type='Latte'
    elif 'four:four' in resp:
        drink_type='Cappuccino'
    else:
        order+=1
        drinks+=1

    say='To confirm, you ordered a cup of ' + drink_type +', correct?'
    speeching()
    Textts()
    yes_no()
    stt_witt()

def drinktype():
    order_drink_type()
    yesno_order()

def order_drink_size():
    global drink_size
    global drink_type
    global order
    global say

    say='Sure, what size would you like your ' + drink_type + ' to be in? We have Option 1. Small size, Option 2. Medium size or Option 3. Large size.'
    speeching()
    Textts()

    if 'small:small' in resp:
        drink_size='Small '
    elif 'medium:medium' in resp:
        drink_size='Medium '
    elif 'large:large' in resp:
        drink_size='Large '
    elif 'one:one' in resp:
        drink_size='Small '
    elif 'two:two' in resp:
        drink_size='Medium '
    elif 'three:three' in resp:
        drink_size='Large '
    else:
        order+=1
        drinks+=1
    
    say='To confirm, you ordered a cup of ' + drink_size + drink_type + ', correct?'
    speeching()
    Textts()
    yes_no()
    stt_witt()

def drinksize():
    order_drink_size()
    yesno_order()

def drinks_append():
    global drink_append
    global drink_size
    global drink_type
    global bottlecup
    global food
    drink_append= drink_size + bottlecup + ' of ' + drink_type
    food.append(drink_append)

def drink_append_append():
    if drink_type != '':
        drinks_append()
    else:
        yes=True
        drink_type = ''
        drink_size = ''

def yesno_order():
    global order
    global say
    empty_placeholder()

    if 'yes:yes' in resp:
        say='Alright. Moving on,'
        order=0
        cost()
    else:
        say='Sorry, could you please repeat your answer the following question:'
        order = 1

    speeching()
    Textts()
    sleep(2)
    empty_placeholder()

def anyelsebe():
    global count
    global count1
    global say
    count=0
    count1=0
    say='Would you like to order anything else?'
    speeching()
    tts_stt_witt()

def anyelse():
    global price
    global count
    global count1
    global say
    global food
    
    if 'yes:yes' in resp:
        count+=1
    elif'no:no' in resp:
        say = 'Alright, to repeat, your order is: '
        food=Counter(food)
        for item in food.items():
            say = say + str(item[1]) + ' ' + str(item[0])

        say = say + '.'
        say = say + ' And your total is: $' + str('%0.2f' % sum(price))
        speeching()
    else:
        say='Sorry, could you please repeat what you just said?'
        count1+=1
        speeching()

    Textts()
    sleep(2)
    empty_placeholder()

def cost():
    global price
    global burg
    global fries_size
    global drink_size
    global drink_type
    global foodtypes
    global costs
    global order
    global burgwfries
    if burg == 'Chicken Burger':
        costs+=3.25
    elif burg == 'Beef Burger':
        costs+=2.7
    elif burg == 'Double Chicken Burger':
        costs+=4.25
    elif burg == 'Double Beef Burger':
        costs+=3.7
    elif fries_size == 'Small':
        costs+=2.6
    elif fries_size == 'Medium':
        costs+=4.3
    elif fries_size == 'Large':
        costs+=4.6
    elif drink_type == 'Coke':
        costs+=3.5
    elif drink_type == 'Sprite':
        costs+=3.5
    elif drink_type == 'Cappuccino':
        costs+=4.5
    elif drink_type == "Latte":
        costs+=4.5
    
    if drink_size == 'Medium ':
        costs+=0.7
    elif drink_size == 'Large ':
        costs+=1.7

    price.append(costs)

    if burgwfries !=0:
        burgwfries = 0
    else:
        burg = ''

    fries_size = ''
    costs = 0.0

def payment():
    global card
    global paynow
    global count
    global say
    say='Would you like to pay by Option 1. card or Option 2. paynow?'
    speeching()
    tts_stt_witt()
    
    if 'card:card' in resp:
        card = True
        count = 0
    elif 'paynow:paynow' in resp:
        paynow = True
        count = 0
    elif 'one:one' in resp:
        card = True
        count = 0
    elif 'two:two' in resp:
        paynow = True
        count = 0
    else:
        count+=1

def paymentcon():
    global card
    global paynow
    global count
    global say
    
    if card == True:
        say = 'What kind of card would you like to use, we have Option 1. Visa, Option 2. Mastercard or Option 3. American Express as our options.'
        speeching()
        tts_stt_witt()
    if paynow == True:
        say = 'Please scan the QR code shown to you and complete the payment.'
        speeching()
        Textts()

def card_type():
    global say
    if 'visa:visa' in resp:
        say='Please tap your Visa card on the card reader.'
    elif 'mastercard:mastercard' in resp:
        say='Please tap your Mastercard on the card reader.'
    elif 'amerexp:amerexp' in resp:
        say='Please tap your American Express card on the card reader.'
    elif 'one:one' in resp:
        say='Please tap your Visa card on the card reader.'
    elif 'two:two' in resp:
        say='Please tap your Mastercard on the card reader.'
    elif 'three:three' in resp:
        say='Please tap your American Express card on the card reader.'
    speeching()
    Textts()

def dineinoutfinal():
    global say
    global dinein_out
    if dinein_out=='dine in':
        say='Please patiently wait for your number to be called and enjoy your dine in experience. Hope you have a good day!'
    elif dinein_out=='take away':
        say='Please patiently wait for your number to be called to get your take away order.'
    speeching()
    Textts()
    empty_placeholder()

    empty_placeholder()
    say = 'This is the end of the demo.'
    speeching()
    Textts()

def translatetolang():
    global say
    say=GoogleTranslator(source='auto', target=langua).translate(say)

def translatebacktoEn():
    global speech
    speech=GoogleTranslator(source=langua, target='en').translate(speech)

def translatespeechtolang():
    global speech
    speech1=GoogleTranslator(source='auto', target=langua).translate(speech)

def witt():
    global resp
    try:
        if langua != 'en':
            translatebacktoEn()

        resp = str(client.message(speech))

        resp = resp.replace("'confidence':", '').replace("'id':", '').replace('text:', '|').replace('traits:', '|').replace('body:', '|')
        resp = resp.replace('.', '').replace(',', '').replace("'", '').replace('{', '').replace('}', '').replace('[', '').replace(']','')
        resp = resp.replace('0', '')
        resp = resp.replace('1', '')
        resp = resp.replace('2', '')
        resp = resp.replace('3', '')
        resp = resp.replace('4', '')
        resp = resp.replace('5', '')
        resp = resp.replace('6', '')
        resp = resp.replace('7', '')
        resp = resp.replace('8', '')
        resp = resp.replace('9', '')
    except NameError:
        yes=True
    print(resp)

def witt1():
    global resp
    try:
        resp = str(client.message(speech))
        resp = resp.replace("'confidence':", '').replace("'id':", '').replace('text:', '|').replace('traits:', '|').replace('body:', '|')
        resp = resp.replace('.', '').replace(',', '').replace("'", '').replace('{', '').replace('}', '').replace('[', '').replace(']','')
        resp = resp.replace('0', '')
        resp = resp.replace('1', '')
        resp = resp.replace('2', '')
        resp = resp.replace('3', '')
        resp = resp.replace('4', '')
        resp = resp.replace('5', '')
        resp = resp.replace('6', '')
        resp = resp.replace('7', '')
        resp = resp.replace('8', '')
        resp = resp.replace('9', '')
    except NameError:
        print("error")
    print(resp)
    return

def stt_witthello():
    speechtthello()
    if speech != '':
        witt()
    else:
        yes=True

def stt_witt():
    speechtt()
    witt()

def stt_witt1():
    speechtt()
    witt1()

def stt1_witt():
    speechtt1()
    witt()

def tts_witt():
    Textts()
    witt()

def tts_stt_witt():
    Textts()
    speechtt()
    witt()

def tts_stt_witt1():
    Textts()
    speechttstart()
    witt1()

def sttstart_witt1():
    speechttstart()
    if count1==0:
        witt1()
    else:
        langua='ms'
        speechtt1()
        witt1()

def sttstart_witt1_langu():
    speechttstart()
    witt1()
    langu()

while True:
    placeholder.markdown("Say Hello!")
    stt_witthello()
    detecthello()
    if count==0:
        break
    else:
        yes=True

error=False
empty_placeholder()
languastart()
langualoop()

while True:
    yesno()

    if count1 != 0:
        languastart()

    if count2 != 0:
        langualoop()
    
    if count1 == 0 and count2 == 0:
        break

hello()

while True:
    if count != 0:
        dineinout()
        detectdineinout()
    else:
        break

    yesno1()

speech_ordering()
ordering()

while True:
    empty_placeholder()
    if count != 0:
        ordering()
    else:
        break

ordering_loop()

empty_placeholder()
drink_append_append()

while True:
    anyelsebe()
    anyelse()
    if count != 0:
        ordering()
        ordering_loop()
        drink_append_append()
    elif count1 != 0:
        anyelsebe()
        anyelse()
    else:
        break

empty_placeholder()

while True:
    payment()
    if card != True and paynow != True and count != 0:
        payment()
        break
    elif card == True and paynow != True and count == 0:
        paymentcon()
        card_type()
        break
    elif card != True and paynow == True and count == 0:
        paymentcon()
        break
    else:
        say = 'There is a critical system error and you will have to restart the proceedure again.'
        exit()

dineinoutfinal()