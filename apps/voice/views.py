import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


SUPPORTED_LANGUAGES = [
    ('en', 'English'),
    ('hi', 'हिन्दी'),
    ('bn', 'বাংলা'),
    ('te', 'తెలుగు'),
    ('ta', 'தமிழ்'),
    ('mr', 'मराठी'),
    ('gu', 'ગુજરાતી'),
    ('ur', 'اردو'),
]

REPLIES = {
    'en': {
        'empty': 'Please ask a question about farming, crops, weather, pesticides, or government schemes.',
        'weather': 'For weather updates, use the Weather section and enter your location. You can also ask me about rainfall, temperature, or when to schedule irrigation.',
        'crop': 'Tell me your soil type and region, and I can share crop choices. Use the Crops section for available crop details and growing conditions.',
        'scheme': 'I can explain government schemes, subsidies, and loans for farmers. Ask me about subsidies, loans, or support programs for your farm.',
        'pesticide': 'I can share safe pesticide guidance. Use the Pesticides Guide for product advice and protection tips for common pests and diseases.',
        'default': 'Hello! I am AgriGenie Chat. Ask me a farm-related question about crops, weather, soil health, pesticides, or government schemes. I will give a clear, practical reply.',
        'invalid_method': 'Invalid request method. Please submit your message using the chat interface.',
        'json_error': 'Unable to parse request data. Please try again.',
    },
    'hi': {
        'empty': 'कृपया खेती, फसल, मौसम, कीटनाशक, या सरकारी योजनाओं से संबंधित प्रश्न पूछें।',
        'weather': 'मौसम अपडेट के लिए मौसम सेक्शन का उपयोग करें और अपना स्थान दर्ज करें। आप वर्षा, तापमान, या सिंचाई का समय भी पूछ सकते हैं।',
        'crop': 'मुझे अपनी मिट्टी का प्रकार और क्षेत्र बताएं, मैं फसल विकल्प साझा कर सकता हूँ। उपलब्ध फसल विवरण और बढ़ने की स्थितियों के लिए Crops सेक्शन देखें।',
        'scheme': 'मैं किसानों के लिए सरकारी योजनाओं, सब्सिडी और ऋण की जानकारी दे सकता हूं। मुझसे सब्सिडी, ऋण या सपोर्ट प्रोग्राम पूछें।',
        'pesticide': 'मैं सुरक्षित कीटनाशक सलाह दे सकता हूं। उत्पाद सलाह और सामान्य कीटों एवं रोगों से सुरक्षा के लिए Pesticides Guide का उपयोग करें।',
        'default': 'नमस्ते! मैं AgriGenie चैट हूं। मुझसे खेती, मौसम, मिट्टी की सेहत, कीटनाशकों, या सरकारी योजनाओं के बारे में सवाल पूछें। मैं स्पष्ट, व्यावहारिक उत्तर दूंगा।',
        'invalid_method': 'अमान्य अनुरोध विधि। कृपया चैट इंटरफ़ेस का उपयोग करके अपना संदेश भेजें।',
        'json_error': 'अनुरोध डेटा को पढ़ा नहीं जा सका। कृपया पुन: प्रयास करें।',
    },
    'bn': {
        'empty': 'দয়া করে কৃষি, ফসল, আবহাওয়া, কীটনাশক, বা সরকারি স্কিম সম্পর্কে প্রশ্ন করুন।',
        'weather': 'আবহাওয়া আপডেটের জন্য Weather বিভাগ ব্যবহার করুন এবং আপনার অবস্থান লিখুন। আপনি বৃষ্টিপাত, তাপমাত্রা অথবা সেচের সময়ও জানতে পারেন।',
        'crop': 'আমাকে আপনার মাটির ধরন এবং অঞ্চল বলুন, আমি ফসলের विकल्प বলতে পারি। উপলব্ধ ফসলের তথ্যের জন্য Crops বিভাগ দেখুন।',
        'scheme': 'আমি কৃষকদের জন্য সরকারি স্কিম, ভাতা এবং ঋণের ব্যাখ্যা করতে পারি। ভাতা, ঋণ বা সহায়তা প্রোগ্রামের সম্পর্কে আমাকে জিজ্ঞাসা করুন।',
        'pesticide': 'আমি নিরাপদ কীটনাশক পরামর্শ দিতে পারি। পণ্য পরামর্শ এবং সাধারণ কীটপতঙ্গ এবং রোগ থেকে রক্ষা পেতে Pesticides Guide ব্যবহার করুন।',
        'default': 'হ্যালো! আমি AgriGenie চ্যাট। আমাকে ফসল, আবহাওয়া, মাটি স্বাস্থ্য, কীটনাশক, বা সরকারি স্কিম সম্পর্কে প্রশ্ন করুন। আমি পরিষ্কার, ব্যবহারিক উত্তর দেব।',
        'invalid_method': 'অবৈধ অনুরোধ পদ্ধতি। দয়া করে চ্যাট ইন্টারফেস ব্যবহার করে আপনার বার্তা পাঠান।',
        'json_error': 'অনুরোধের ডেটা পড়া যায়নি। অনুগ্রহ করে আবার চেষ্টা করুন।',
    },
    'ta': {
        'empty': 'தயவுசெய்து விவசாயம், பயிர், வானிலை, பூச்சிக்கொல்லி, அல்லது அரசு திட்டம் பற்றிய கேள்வி கேளுங்கள்.',
        'weather': 'வானிலை புதுப்பிப்புகளுக்கு Weather பகுதியைப் பயன்படுத்தி உங்கள் இடத்தை உள்ளிடவும். மழை, வெப்பநிலை அல்லது நீர் பொங்குதல் நேரம் குறித்து கேட்கவும்.',
        'crop': 'உங்கள் மண் வகை மற்றும் பகுதியை என்னிடம் கூறுங்கள், நான் பயிர் தேர்வுகளை பகிரலாம். கிடைக்கும் பயிர் விவரங்கள் மற்றும் வளர்ச்சி நிலைகளுக்கு Crops பகுதியை பாருங்கள்.',
        'scheme': 'நான் விவசாயிகளுக்கான அரசு திட்டங்கள், உதவித்தொகை மற்றும் கடனுகளை விளக்கமளிக்க могу. உதவித்தொகை, கடன் அல்லது ஆதரவு திட்டங்களை என்னிடம் கேளுங்கள்.',
        'pesticide': 'நான் பாதுகாப்பான பூச்சிக்கொல்லி வழிகாட்டியை வழங்க முடியும். தயாரிப்பு பரிந்துரைகள் மற்றும் பொதுவான பூச்சிகள் மற்றும் நோய்களைப் பாதுகாக்க Pesticides Guide பயன்படுத்தவும்.',
        'default': 'வணக்கம்! நான் AgriGenie சிறந்த உதவியாளர். எனக்கு விவசாயம், வானிலை, மண் ஆரோக்கியம், பூச்சிக்கொல்லி அல்லது அரசு திட்டங்களைப் பற்றி கேளுங்கள். நான் தெளிவான, பயனுள்ள பதிலைத் தருவேன்.',
        'invalid_method': 'தவறான கோரிக்கை முறை. தயவுசெய்துச் சாட் இடைமுகத்தை பயன்படுத்தி உங்கள் செய்தியை அனுப்பவும்.',
        'json_error': 'கோரிக்கை தரவைப் படிக்க முடியவில்லை. தயவுசெய்து மீண்டும் முயற்சிக்கவும்.',
    },
    'te': {
        'empty': 'దయచేసి వ్యవసాయం, పంట, వాతావరణం, పేరిట్, లేదా ప్రభుత్వ కార్యక్రమం గురించి ప్రశ్న అడగండి.',
        'weather': 'వాతావరణ తాజాకరణల కోసం Weather విభాగాన్ని ఉపయోగించి మీ స్థానాన్ని నమోదు చేయండి. వర్షపాతం, ఉష్ణోగ్రత లేదా పంచాయితీ సమయం గురించి మీరు అడగవచ్చు.',
        'crop': 'మీ మట్టి రకం మరియు ప్రాంతం గురించి నాకు చెప్పండి, నేను పంట ఎంపికలను పంచగలను. అందుబాటులో ఉన్న పంట వివరాలకు Crops విభాగాన్ని చూడండి.',
        'scheme': 'నేను రైతుల కోసం ప్రభుత్వ పథకాలు, సబ్సిడీలు మరియు రుణాలను వివరిస్తా. సబ్సిడీ, రుణం లేదా సపోర్ట్ ప్రోగ్రామ్‌ల గురించి నన్ను అడగండి.',
        'pesticide': 'నేను రక్షకవంతమైన పేరిట్ మార్గదర్శకాన్ని సూచించగలను. ఉత్పత్తి సలహా మరియు సాధారణ కీటకాలు మరియు వ్యాధుల నుండి రక్షణ కోసం Pesticides Guide ఉపయోగించండి.',
        'default': 'హలో! నేను AgriGenie చాట్. పంటలు, వాతావరణం, మట్టితో ఆరోగ్యం, పేరిట్‌లు లేదా ప్రభుత్వ పథకాల గురించి నన్ను అడగండి. నేను స్పష్టం, ప్రాయోగికమైన జవాబును ఇస్తాను.',
        'invalid_method': 'అబద్ధమైన అభ్యర్థన పద్ధతి. దయచేసి చాట్ ఇంటరాఫేస్‌ను ఉపయోగించి మీ సందేశాన్ని పంపండి.',
        'json_error': 'అభ్యర్థన డేటాను చదవలేకపోయాం. దయచేసి మళ్లీ ప్రయత్నించండి.',
    },
    'mr': {
        'empty': 'कृपया शेती, पिक, हवामान, कीटकनाशक, किंवा सरकारी योजना याबद्दल प्रश्न विचारा.',
        'weather': 'हवामान अद्यतनांसाठी Weather विभागाचा वापर करा आणि आपले स्थान प्रविष्ट करा. तुम्ही पावसाबाबत, तापमानाबाबत किंवा पिण्याच्या वेळेबाबतही विचारू शकता.',
        'crop': 'मला तुमचा मातीचा प्रकार आणि शेतजमिनीची माहिती द्या, मी पिकांच्या विकल्पांची माहिती देईन. उपलब्ध पिकांच्या तपशीलांसाठी Crops विभाग पहा.',
        'scheme': 'मी शेतकऱ्यांसाठी सरकारी योजना, अनुदान आणि कर्ज याबद्दल माहिती देऊ शकतो. मला अनुदान, कर्ज किंवा मदत कार्यक्रमांबद्दल विचारा.',
        'pesticide': 'मी सुरक्षित कीटकनाशक मार्गदर्शन देऊ शकतो. उत्पादन सल्ला आणि सामान्य कीटक आणि रोगांपासून संरक्षणासाठी Pesticides Guide वापरा.',
        'default': 'नमस्कार! मी AgriGenie चॅट आहे. मला पिके, हवामान, मातीची स्थिती, कीटकनाशके, किंवा सरकारी योजना याबद्दल विचारा. मी स्पष्ट, व्यावहारिक उत्तर देईन.',
        'invalid_method': 'अवैध विनंती पद्धत. कृपया चॅट इंटरफेस वापरून आपल्या संदेशाची नोंद करा.',
        'json_error': 'विनंती डेटा वाचता आला नाही. कृपया पुन्हा प्रयत्न करा.',
    },
    'gu': {
        'empty': 'કૃપા કરીને ખેતી, પાક, હવામાન, જંતુનાશક, અથવા સરકારી યોજનાઓ વિશે પ્રશ્ન પુછો.',
        'weather': 'હવામાન અપડેટ માટે Weather વિભાગનો ઉપયોગ કરો અને તમારો સ્થળ દાખલ કરો. તમે વરસાદ, તાપમાન અથવા સિંચાઈ સમય વિશે પણ પૂછુ શકો છો.',
        'crop': 'તમારી જમીનનો પ્રકાર અને પ્રદેશ મને જણાવો, હું પાક પસંદગીઓ શેર કરી શકું. ઉપલબ્ધ પાક વિગતો માટે Crops વિભાગ જુઓ.',
        'scheme': 'હું ખેડૂતો માટેની સરકારી યોજનાઓ, છૂટછાટો અનેકઢજ અંગે સમજાવી શકું છું. મને છૂટછાટ, લોન અથવા સહાય કાર્યક્રમો વિશે પૂછો.',
        'pesticide': 'હું સુરક્ષિત જંતુનાશક માર્ગદર્શન આપી શકું છું. ઉત્પાદન સલાહ અને સામાન્ય જીવાઓ અને રોગોથી રક્ષણ માટે Pesticides Guide નો ઉપયોગ કરો.',
        'default': 'નમસ્તે! હું AgriGenie ચેટ છું. મને પાક, હવામાન, માટીની આરોગ્ય, જંતુનાશક, અથવા સરકારી યોજનાઓ વિશે પૂછો. હું સ્પષ્ટ, વ્યવહારુ જવાબ આપીશ.',
        'invalid_method': 'અમાન્ય વિનંતી પદ્ધતિ. કૃપા કરીને ચેટ ઇન્ટરફેસનો ઉપયોગ કરીને તમારો સંદેશ મોકલો.',
        'json_error': 'વિનંતી ડેટા વાંચી શકાયો નથી. કૃપા કરીને ફરીથી પ્રયાસ કરો.',
    },
    'ur': {
        'empty': 'براہ کرم زراعت، فصل، موسم، کیڑے مار ادویات، یا حکومتی اسکیم کے بارے میں سوال پوچھیں۔',
        'weather': 'موسم کی تازہ کاریوں کے لیے Weather سیکشن استعمال کریں اور اپنی جگہ درج کریں۔ آپ بارش، درجہ حرارت، یا آبپاشی کے وقت کے بارے میں بھی پوچھ سکتے ہیں۔',
        'crop': 'مجھے اپنی مٹی کی قسم اور علاقہ بتائیں، میں فصل کے انتخاب شئیر کر سکتا ہوں۔ دستیاب فصل کی تفصیلات کے لیے Crops سیکشن دیکھیں۔',
        'scheme': 'میں کسانوں کے لیے حکومتی اسکیمیں، سبسڈیز، اور قرضے سمجھا سکتا ہوں۔ مجھ سے سبسڈی، قرض، یا سپورٹ پروگراموں کے بارے میں پوچھیں۔',
        'pesticide': 'میں محفوظ کیڑے مار ادویات کی رہنمائی فراہم کر سکتا ہوں۔ مصنوعات کی سفارش کے لیے Pesticides Guide استعمال کریں اور عام کیڑے اور بیماریوں سے حفاظت حاصل کریں۔',
        'default': 'ہیلو! میں AgriGenie چیٹ ہوں۔ مجھ سے فصلوں، موسم، مٹی کی صحت، کیڑے مار ادویات، یا حکومتی اسکیموں کے بارے میں سوال پوچھیں۔ میں واضح، عملی جواب دوں گا۔',
        'invalid_method': 'غلط درخواست کا طریقہ۔ براہ کرم چیٹ انٹرفیس استعمال کرکے اپنا پیغام بھیجیں۔',
        'json_error': 'درخواست کے ڈیٹا کو پڑھا نہیں جا سکا۔ براہ کرم دوبارہ کوشش کریں۔',
    },
}


def get_reply_key(message):
    text = message.lower()
    if any(word in text for word in ['weather', 'rain', 'temperature', 'climate']):
        return 'weather'
    if any(word in text for word in ['crop', 'plant', 'seed', 'harvest']):
        return 'crop'
    if any(word in text for word in ['scheme', 'loan', 'subsidy', 'support']):
        return 'scheme'
    if any(word in text for word in ['pesticide', 'pest', 'disease', 'spray']):
        return 'pesticide'
    return 'default'


def get_reply(message, lang='en'):
    lang = lang if lang in REPLIES else 'en'
    replies = REPLIES.get(lang, REPLIES['en'])
    if not message:
        return replies['empty']
    key = get_reply_key(message)
    return replies.get(key, replies['default'])


@login_required
def unified_assistant(request):
    return render(request, 'voice/unified_assistant.html', {
        'supported_languages': SUPPORTED_LANGUAGES,
    })


@login_required
def chat_with_ai(request):
    if request.method != 'POST':
        return JsonResponse({'error': REPLIES['en']['invalid_method']}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8') or '{}')
        user_message = data.get('message', '').strip()
        lang = data.get('lang', request.session.get('site_lang', 'en'))
        if lang not in dict(SUPPORTED_LANGUAGES):
            lang = 'en'

        if not user_message:
            return JsonResponse({'reply': REPLIES[lang]['empty']})

        reply = get_reply(user_message, lang)
        return JsonResponse({'reply': reply})
    except json.JSONDecodeError:
        return JsonResponse({'error': REPLIES['en']['json_error']}, status=400)
    except Exception as exc:
        return JsonResponse({'error': str(exc)}, status=500)
