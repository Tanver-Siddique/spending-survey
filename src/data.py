start_text = {
    "en": {
        "welcome": "Welcome",
        "request": "Request for Your Opinion",
        "description": (
            "We're conducting a brief survey to understand how people spend their money "
            "once their essential needs are met. Your insights are incredibly important "
            "as they help us understand evolving consumer priorities and lifestyle trends. "
            "This information can guide businesses in developing products and services that "
            "truly align with what people want beyond their basic needs."
        ),
        "time": "5-7 Minutes",
        "anonymous": "Anonymous",
        "button": "Start Survey",
    },
    "bn": {
        "welcome": "স্বাগতম",
        "request": "আপনার মতামত প্রার্থনা করছি",
        "description": (
            "আমরা একটি সংক্ষিপ্ত জরিপ পরিচালনা করছি, যাতে বোঝা যায় মানুষ তাদের মৌলিক "
            "প্রয়োজন মেটানোর পর কীভাবে টাকা ব্যয় করে। আপনার মতামত আমাদের জন্য অত্যন্ত "
            "গুরুত্বপূর্ণ কারণ এটি পরিবর্তিত ভোক্তা অগ্রাধিকার ও জীবনযাপনের প্রবণতা বুঝতে সাহায্য করে। "
            "এই তথ্য ব্যবসাকে এমন পণ্য ও সেবা উন্নয়নে সহায়তা করবে যা মানুষের প্রকৃত চাহিদার সাথে সামঞ্জস্যপূর্ণ।"
        ),
        "time": "৫-৭ মিনিট",
        "anonymous": "গোপনীয়",
        "button": "জরিপ শুরু করুন",
    }
}
####### general info questionaries test###########

general_info = {
    "en":{
        "1GI": {
            "type": "radio",
            "question": r'''What is your **age**?''',
            "options": {1: "18-24", 2: "25-34", 3: "35-44", 4: "45+"}
        },
        "2GI": {
            "type": "radio",
            "question": r'''What is your **gender**?''',
            "options": {1: "Male", 2: "Female", 3: "Prefer not to say"}
        },
        "3GI": {
            "type": "radio",
            "question": r'''Which **division** do you currently live in?''',
            "options": {1: "Barishal", 2: "Chattogram", 3: "Dhaka", 4: "Khulna", 5: "Mymensingh", 6: "Rajshahi", 7: "Rangpur", 8: "Sylhet"}
        },
        "4GI": {
            "type": "checkbox",
            "question": r'''What is your current **employment** status? (Select all that apply)''',
            "options": {
                1: "Student",
                2: "Private job holder",
                3: "Government job holder",
                4: "Business/Entrepreneur",
                5: "Freelancer",
                6: "Part-time job holder",
                7: "Homemaker",
                8: "Others:"
            }
        }
    },
    "bn":{
        "1GI": {
            "type": "radio",
            "question": r'''আপনার **বয়স** কত?''',
            "options": {1: "১৮-২৪", 2: "২৫-৩৪", 3: "৩৫-৪৪", 4: "৪৫+"}
        },
        "2GI": {
            "type": "radio",
            "question": r'''আপনার **লিঙ্গ** কী?''',
            "options": {1: "পুরুষ", 2: "মহিলা", 3: "বলতে ইচ্ছুক নই"}
        },
        "3GI": {
            "type": "radio",
            "question": r'''আপনি বর্তমানে কোন **বিভাগে** বসবাস করছেন?''',
            "options": {1: "বরিশাল", 2: "চট্টগ্রাম", 3: "ঢাকা", 4: "খুলনা", 5: "ময়মনসিংহ", 6: "রাজশাহী", 7: "রংপুর", 8: "সিলেট"}
        },
        "4GI": {
            "type": "checkbox",
            "question": r'''আপনার বর্তমান **পেশা** কী? (প্রযোজ্য সবগুলি নির্বাচন করুন)''',
            "options": {
                1: "ছাত্র",
                2: "বেসরকারী চাকরিজীবী",
                3: "সরকারি চাকরিজীবী",
                4: "ব্যবসায়ী/উদ্যোক্তা",
                5: "ফ্রি-লেন্সার",
                6: "পার্ট-টাইম চাকরি",
                7: "গৃহিণী",
                8: "অন্যান্য:"
            }
        }
    }
}

spending = {
    "en":{
        "SML3":{
            "type":"checkbox",
            "question":r'''Thinking about the last 3 months, which of the following categories have you spent money? (Select all that apply)''',
            "options":{
                1: "Fashion (Stylish clothes, shoes)",
                2: "Accessories (Bags, watches, jewelry)",
                3: "Beauty & Skincare (Makeup, perfumes)",
                4: "Dry / Packaged Food Items",
                5: "Hobbies (Books, art supplies, crafts, etc.)",
                6: "Home Decor",
                7: "Home & Kitchen Essentials",
                8: "Electronics & Gadgets",
                9: "Baby & Kids Essentials",
                10: "Not purchase anything"
            }
        }
        
    },
    "bn":{
        "SML3":{
            "type":"checkbox",
            "question":r'''গত ৩ মাসে আপনি কোন কোন খাতে টাকা খরচ করেছেন? (প্রযোজ্য সকলগুলো নির্বাচন করুন)''',
            "options":{
                1: "ফ্যাশন (স্টাইলিশ পোশাক, জুতা)",
                2: "অ্যাকসেসরিজ (ব্যাগ, ঘড়ি, গহনা)",
                3: "বিউটি ও স্কিনকেয়ার (মেকআপ, সুগন্ধি)",
                4: "শুকনো / প্যাকেটযুক্ত খাবারের সামগ্রী",
                5: "শখ (বই, আর্ট সরঞ্জাম, ক্রাফ্ট সামগ্রী, ইত্যাদি)",
                6: "হোম ডেকর (বাড়ি সাজানোর জিনিস)",
                7: "গৃহস্থালি ও রান্নাঘরের প্রয়োজনীয় জিনিসপত্র",
                8: "ইলেকট্রনিক্স ও গ্যাজেট",
                9: "শিশু ও বাচ্চাদের প্রয়োজনীয় জিনিসপত্র",
                10: "কিছু কেনা হয়নি"
            }
        }
    }
}

assume = {
    "en":{
        "AE5T":{
            "type":"radio",
            "question":"If you had an extra 5,000 BDT this month to treat yourself, what would you be MOST likely to spend it on? (Select only one)",
            "options":{
                1: "Fashion (Stylish clothes, shoes)",
                2: "Accessories (Bags, watches, jewelry)",
                3: "Beauty & Skincare (Makeup, perfumes)",
                4: "Dry / Packaged Food Items",
                5: "Hobbies (Books, art supplies, crafts, etc.)",
                6: "Home Decor",
                7: "Home & Kitchen Essentials",
                8: "Electronics & Gadgets",
                9: "Baby & Kids Essentials"
            }
        }
    },
    "bn":{
        "AE5T":{
            "type":"radio",
            "question":"এই মাসে আপনার কাছে অতিরিক্ত ৫,০০০ টাকা থাকলে, আপনি সেগুলো সবচেয়ে বেশি কী জন্য ব্যয় করবেন? (শুধুমাত্র একটি নির্বাচন করুন)",
            "options":{
                1: "ফ্যাশন (স্টাইলিশ পোশাক, জুতা)",
                2: "অ্যাকসেসরিজ (ব্যাগ, ঘড়ি, গহনা)",
                3: "বিউটি ও স্কিনকেয়ার (মেকআপ, সুগন্ধি)",
                4: "শুকনো / প্যাকেটযুক্ত খাবারের সামগ্রী",
                5: "শখ (বই, আর্ট সরঞ্জাম, ক্রাফ্ট সামগ্রী, ইত্যাদি)",
                6: "হোম ডেকর (বাড়ি সাজানোর জিনিস)",
                7: "গৃহস্থালি ও রান্নাঘরের প্রয়োজনীয় জিনিসপত্র",
                8: "ইলেকট্রনিক্স ও গ্যাজেট",
                9: "শিশু ও বাচ্চাদের প্রয়োজনীয় জিনিসপত্র"
            }
        }
    }
}


fashion ={
    "en":{
        "1FA": {
            "type": "radio",
            "question": "How often do you buy fashion items online?",
            "options": {
                "1": "Frequently (monthly or more)",
                "2": "Sometimes (every 2–3 months)",
                "3": "Rarely (1–2 times/year)",
                "4": "Never"
            }
        },
        "2FA": {
            "type": "radio",
            "question": "Which platform do you mostly use to buy fashion products?",
            "options": {
                "1": "Social media shops (Facebook/Instagram)",
                "2": "Online platforms (Daraz, etc.)",
                "3": "Shopping malls/brand outlets",
                "4": "Local markets"
            }
        },
        "3FA": {
            "type": "checkbox",
            "question": "What types of fashion items do you buy most often online? (Please select up to 3)",
            "options": {
                "1": "Casual wear (t-shirts, tops, jeans)",
                "2": "Traditional wear (saree, salwar kameez, panjabi)",
                "3": "Western wear (dresses, formal shirts, suits)",
                "4": "Modest wear (abayas/borka, hijabs, long dresses)",
                "5": "Footwear (sneakers, sandals, heels, shoes, etc.)"
            }
        },
        "4FA": {
            "type": "radio",
            "question": "How much do you usually spend on one online fashion purchase?",
            "options": {
                "1": "Under 1000",
                "2": "1000-1500",
                "3": "1500-2000",
                "4": "Above 2000"
            }
        },
        "5FA": {
            "type": "radio",
            "question": "When buying a fashion item online, what is the most important factor for you?",
            "options": {
                "1": "Uniqueness & Style",
                "2": "Quality & fabric",
                "3": "Comfort & Fit",
                "4": "Price/discount",
                "5": "Trustworthy seller reviews/Brand Reputation"
            }
        },
        "6FA": {
            "type": "checkbox",
            "question": "What problems do you face when buying fashion items online? (Select all that apply)",
            "options": {
                "1": "Product not same as shown",
                "2": "Poor quality/fabric",
                "3": "Price too high compared to quality",
                "4": "Limited sizes/fittings",
                "5": "Lack of trendy/unique designs",
                "6": "Unresponsive/unprofessional sellers",
                "7": "Difficult return/refund",
                "8": "Delivery takes too long",
                "9": "Others:"
            }
        },
        "7FA": {
            "type": "radio",
            "question": "Which fashion product do you WISH were more easily available online in Bangladesh?",
            "options": {
                "1": "Well-fitting pants/trousers",
                "2": "Affordable but stylish formal wear",
                "3": "Unique/trendy sarees or salwar kameez",
                "4": "Plus-size or custom-size fashion",
                "5": "Quality footwear under 2,000 BDT",
                "6": "Others:"
            }
        }
    },
    "bn":{
        "1FA":{
            "type":"radio",
            "question":"আপনি কত ঘন ঘন অনলাইনে ফ্যাশন আইটেম কেনেন?",
            "options":{
                "1": "প্রায়শই (মাসিক বা তার বেশি)",
                "2": "মাঝে মাঝে (প্রতি ২-৩ মাস পর)",
                "3": "কদাচিৎ (বছরে ১-২ বার)",
                "4": "কখনোই না"
            }
        },
        "2FA":{
            "type":"radio",
            "question":"ফ্যাশন পণ্য কেনার জন্য আপনি প্রধানত কোন প্ল্যাটফর্ম ব্যবহার করেন?",
            "options":{
                "1": "সোশ্যাল মিডিয়া শপ (ফেসবুক/ইনস্টাগ্রাম)",
                "2": "অনলাইন প্ল্যাটফর্ম (দারাজ, ইত্যাদি)",
                "3": "শপিং মল/ব্র্যান্ড আউটলেট",
                "4": "স্থানীয় বাজার"
            }
        },
        "3FA":{
            "type":"checkbox",
            "question":"আপনি অনলাইনে সবচেয়ে বেশি কোন ধরনের ফ্যাশন আইটেম কেনেন? (অনুগ্রহ করে সর্বোচ্চ ৩টি নির্বাচন করুন)",
            "options":{
                "1": "ক্যাজুয়াল পোশাক (টি-শার্ট, টপ, জিন্স)",
                "2": "ঐতিহ্যবাহী পোশাক (শাড়ি, সালোয়ার কামিজ, পাঞ্জাবি)",
                "3": "ওয়েস্টার্ন পোশাক (ড্রেস, ফরমাল শার্ট, স্যুট)",
                "4": "শালীন পোশাক (আবায়া/বোরকা, হিজাব, লম্বা ড্রেস)",
                "5": "জুতো (স্নিপার, স্যান্ডেল, হিল, সু, ইত্যাদি)"
            }
        },
        "4FA":{
            "type":"radio",
            "question":"অনলাইনে একটি ফ্যাশন পণ্য কেনার জন্য আপনি সাধারণত কত টাকা খরচ করেন?",
            "options":{
                "1": "১০০০ টাকার নিচে",
                "2": "১০০০-১৫০০ টাকা",
                "3": "১৫০০-২০০০ টাকা",
                "4": "২০০০ টাকার উপরে"
            }
        },
        "5FA":{
            "type":"radio",
            "question":"অনলাইনে ফ্যাশন আইটেম কেনার সময় আপনার কাছে সবচেয়ে গুরুত্বপূর্ণ বিষয় কোনটি?",
            "options":{
                "1": "অনন্যতা ও স্টাইল",
                "2": "গুণমান ও কাপড়",
                "3": "আরাম ও ফিট",
                "4": "দাম/ডিসকাউন্ট",
                "5": "বিশ্বস্ত বিক্রেতার রিভিউ/ব্র্যান্ডের সুনাম"
            }
        },
        "6FA":{
            "type":"checkbox",
            "question":"অনলাইনে ফ্যাশন আইটেম কেনার সময় আপনি কী কী সমস্যার সম্মুখীন হন? (সবগুলি নির্বাচন করুন)",
            "options":{
                "1": "পণ্যের ছবি ও আসল পণ্যের মধ্যে মিল না থাকা",
                "2": "খারাপ গুণমান/কাপড়",
                "3": "গুণমানের তুলনায় দাম বেশি",
                "4": "সীমিত সাইজ/ফিটিং",
                "5": "আধুনিক/অনন্য ডিজাইনের অভাব",
                "6": "অপ্রতিক্রিয়াশীল/অপেশাদার বিক্রেতা",
                "7": "ফেরত/রিফান্ডে অসুবিধা",
                "8": "ডেলিভারিতে অনেক বেশি সময় লাগে",
                "9": "অন্যান্য:"
            }
        },
        "7FA":{
            "type":"radio",
            "question":"বাংলাদেশের অনলাইনে কোন ফ্যাশন পণ্যটি আপনি আরো সহজে পেতে চান?",
            "options":{
                "1": "ভালো ফিটিং প্যান্ট/ট্রাউজার",
                "2": "সাশ্রয়ী কিন্তু স্টাইলিশ ফরমাল পোশাক",
                "3": "অনন্য/আধুনিক শাড়ি বা সালোয়ার কামিজ",
                "4": "প্লাস-সাইজ বা কাস্টম-সাইজ ফ্যাশন",
                "5": "২,০০০ টাকার নিচে মানসম্মত জুতো",
                "6": "অন্যান্য:"
            }
        }
    }
}

accessories ={
    "en":{
        "1AC": {
            "type": "radio",
            "question": "How often do you purchase accessories such as bags, watches, or jewelry?",
            "options": {
                "1": "Frequently (monthly or more)",
                "2": "Sometimes (every 2–3 months)",
                "3": "Rarely (1–2 times/year)",
                "4": "Never"
            }
        },
        "2AC": {
            "type": "radio",
            "question": "Which platform do you use to buy accessory products?",
            "options": {
                "1": "Social media shops (Facebook/Instagram)",
                "2": "Online platforms (Daraz, etc.)",
                "3": "Shopping malls/brand outlets",
                "4": "Local markets"
            }
        },
        "3AC":{
            "type": "radio",
            "question": "Which type of accessories do you purchase most often?",
            "options": {
                "1": "Bags",
                "2": "Watches",
                "3": "Jewelry",
                "4": "All equally",
                "5": "I don’t usually buy accessories"
            }
        },
        "4AC":{
            "type": "radio",
            "question": "When buying accessories, what is your usual budget range?",
            "options": {
                "1": "Under 1000",
                "2": "1000-1500",
                "3": "1500-2000",
                "4": "Above 2000"
            }
        },
        "5AC":{
            "type": "radio",
            "question": "What motivates you the most to purchase accessories?",
            "options": {
                "1": "Brand name",
                "2": "Design/style",
                "3": "Quality/durability",
                "4": "trends/influencers",
                "5": "Price/affordability",
                "6": "Recommendations from friends/family"
            }
        },
        "6AC":{
            "type": "radio",
            "question": "How important are accessories to your overall lifestyle/fashion expression?",
            "options": {
                "1": "Very important (must-have)",
                "2": "Important (buy sometimes to look stylish)",
                "3": "Neutral (not a big deal)",
                "4": "Not important (rarely purchase)"
            }
        },
        "7AC":{
            "type":"radio",
            "question":"Do you gift accessories (bags, watches, jewelry) to others?",
            "options":{
                "1": "Often",
                "2": "Occasionally",
                "3": "Rarely",
                "4": "Never"
            }
        },
        "8AC":{
            "type": "checkbox",
            "question": "What is missing in the current accessories market?(Select all that apply)",
            "options": {
                "1": "Affordable trendy designs",
                "2": "Better quality at a fair price",
                "3": "More availability of authentic branded products",
                "4": "Online reliability (trust & return policy)",
                "5": "Others:"
            }
        }
    },
    "bn":{
        "1AC": {
            "type": "radio",
            "question": "আপনি কত ঘন ঘন ব্যাগ, ঘড়ি বা গয়নার মতো অনুষঙ্গ কেনেন?",
            "options": {
                "1": "প্রায়শই (মাসিক বা তার বেশি)",
                "2": "মাঝে মাঝে (প্রতি ২-৩ মাস পর)",
                "3": "কদাচিৎ (বছরে ১-২ বার)",
                "4": "কখনোই না"
            }
        },
        "2AC": {
            "type": "radio",
            "question": "অনুষঙ্গ কেনার জন্য আপনি কোন প্ল্যাটফর্ম ব্যবহার করেন?",
            "options": {
                "1": "সোশ্যাল মিডিয়া শপ (ফেসবুক/ইনস্টাগ্রাম)",
                "2": "অনলাইন প্ল্যাটফর্ম (দারাজ, ইত্যাদি)",
                "3": "শপিং মল/ব্র্যান্ড আউটলেট",
                "4": "স্থানীয় বাজার"
            }
        },
        "3AC": {
            "type": "radio",
            "question": "আপনি কোন ধরনের অনুষঙ্গ সবচেয়ে বেশি কেনেন?",
            "options": {
                "1": "ব্যাগ",
                "2": "ঘড়ি",
                "3": "গয়না",
                "4": "সব সমানভাবে",
                "5": "আমি সাধারণত অনুষঙ্গ কিনি না"
            }
        },
        "4AC": {
            "type": "radio",
            "question": "অনুষঙ্গ কেনার সময় আপনার স্বাভাবিক বাজেট কত থাকে?",
            "options": {
                "1": "১০০০ টাকার নিচে",
                "2": "১০০০-১৫০০ টাকা",
                "3": "১৫০০-২০০০ টাকা",
                "4": "২০০০ টাকার উপরে"
            }
        },
        "5AC": {
            "type": "radio",
            "question": "অনুষঙ্গ কেনার জন্য আপনাকে সবচেয়ে বেশি কী অনুপ্রাণিত করে?",
            "options": {
                "1": "ব্র্যান্ডের নাম",
                "2": "নকশা/স্টাইল",
                "3": "গুণমান/স্থায়িত্ব",
                "4": "প্রবণতা/প্রভাবক",
                "5": "দাম/সাশ্রয়ীতা",
                "6": "বন্ধু/পরিবারের সুপারিশ"
            }
        },
        "6AC": {
            "type": "radio",
            "question": "আপনার সামগ্রিক জীবনধারা/ফ্যাশন এক্সপ্রেশনে অনুষঙ্গ কতটা গুরুত্বপূর্ণ?",
            "options": {
                "1": "খুব গুরুত্বপূর্ণ (অবশ্যই থাকা উচিত)",
                "2": "গুরুত্বপূর্ণ (স্টাইলিশ দেখাতে মাঝে মাঝে কিনি)",
                "3": "নিরপেক্ষ (খুব একটা ব্যাপার না)",
                "4": "গুরুত্বপূর্ণ নয় (খুব কমই কিনি)"
            }
        },
        "7AC": {
            "type": "radio",
            "question": "আপনি কি অন্যদের উপহার হিসেবে অনুষঙ্গ (ব্যাগ, ঘড়ি, গয়না) দেন?",
            "options": {
                "1": "প্রায়শই",
                "2": "মাঝে মাঝে",
                "3": "কদাচিৎ",
                "4": "কখনোই না"
            }
        },
        "8AC": {
            "type": "checkbox",
            "question": "বর্তমান অনুষঙ্গের বাজারে কীসের অভাব রয়েছে? (সবগুলি নির্বাচন করুন)",
            "options": {
                "1": "সাশ্রয়ী আধুনিক ডিজাইন",
                "2": "ন্যায্য মূল্যে আরও ভালো গুণমান",
                "3": "আসল ব্র্যান্ডেড পণ্যের আরও বেশি সহজলভ্যতা",
                "4": "অনলাইনে নির্ভরযোগ্যতা (বিশ্বাস ও ফেরত নীতি)",
                "5": "অন্যান্য:"
            }
        }
    }
}

beauty ={
    "en":{
        "1BS": {
            "type": "radio",
            "question": "How often do you purchase beauty or skincare products?",
            "options": {
                "1": "Frequently (monthly or more)",
                "2": "Sometimes (every 2–3 months)",
                "3": "Rarely (1–2 times/year)",
                "4": "Never"
            }
        },
        "2BS": {
            "type": "radio",
            "question": "Where do you usually shop for beauty & skincare items?",
            "options": {
                "1": "Social media shops (Facebook/Instagram)",
                "2": "Online platforms (Daraz, etc.)",
                "3": "Shopping malls/brand outlets",
                "4": "Local markets"
            }
        },
        "3BS":{
            "type": "radio",
            "question": "Which type of beauty & skincare products do you buy most often?",
            "options": {
                "1": "Makeup (lipstick, foundation, etc.)",
                "2": "Perfume/fragrance",
                "3": "Skincare (cream, serum, lotion, etc.)",
                "4": "Hair care productsy"
            }
        },
        "4BS":{
            "type": "radio",
            "question": "What is your average monthly spending on beauty/skincare products?",
            "options": {
                "1": "Under 1000",
                "2": "1000-1500",
                "3": "1500-2000",
                "4": "Above 2000"
            }
        },
        "5BS":{
            "type": "radio",
            "question": "Do you prefer local brands or international brands for beauty/skincare?",
            "options": {
                "1": "Local brands",
                "2": "International brands",
                "3": "Both"
            }
        },
        "6BS":{
            "type": "radio",
            "question": "What factors influence your purchase decision for beauty/skincare the most?",
            "options": {
                "1": "Brand reputation",
                "2": "Product quality/ingredients",
                "3": "Price/affordability",
                "4": "Packaging & design",
                "5": "Online reviews/recommendations",
                "6": "Discounts/offers"
            }
        },
        "7BS":{
            "type": "radio",
            "question": "When you use beauty or skincare products, what do you feel it adds most to your life?",
            "options": {
                "1": "Boosting my confidence",
                "2": "Attractiveness",
                "3": "Social impression/status",
                "4": "Self-care and relaxation",
                "5": "Following fashion/beauty trends",
                "6": "Just functional use"
            }
        },
        "8BS":{
            "type": "radio",
            "question": "How important is natural/organic ingredients in your skincare/makeup choices?",
            "options": {
                "1": "Very important",
                "2": "Somewhat important",
                "3": "Not important"
            }
        },
        "9BS":{
            "type": "radio",
            "question": "What challenges do you face while buying beauty/skincare products?",
            "options": {
                "1": "High prices",
                "2": "Lack of authentic products",
                "3": "Difficulty in finding suitable shade/type",
                "4": "Risk of skin reactions",
                "5": "Others:"
            }
        },
        "10BS":{
            "type": "radio",
            "question": "Which products do you wish were more easily available in Bangladesh?",
            "options": {
                "1": "Foreign skincare(Korean, France etc)",
                "2": "Luxury perfumes",
                "3": "Affordable organic skincare",
                "4": "Others:"
            }
        }
    },
    "bn":{
        "1BS": {
            "type": "radio",
            "question": "আপনি কত ঘন ঘন বিউটি বা স্কিনকেয়ার পণ্য কেনেন?",
            "options": {
                "1": "প্রায়শই (মাসিক বা তার বেশি)",
                "2": "মাঝে মাঝে (প্রতি ২-৩ মাস পর)",
                "3": "কদাচিৎ (বছরে ১-২ বার)",
                "4": "কখনোই না"
            }
        },
        "2BS": {
            "type": "radio",
            "question": "বিউটি ও স্কিনকেয়ার সামগ্রী কেনার জন্য আপনি সাধারণত কোথায় যান?",
            "options": {
                "1": "সোশ্যাল মিডিয়া শপ (ফেসবুক/ইনস্টাগ্রাম)",
                "2": "অনলাইন প্ল্যাটফর্ম (দারাজ, ইত্যাদি)",
                "3": "শপিং মল/ব্র্যান্ড আউটলেট",
                "4": "স্থানীয় বাজার"
            }
        },
        "3BS": {
            "type": "radio",
            "question": "আপনি কোন ধরনের বিউটি ও স্কিনকেয়ার পণ্য সবচেয়ে বেশি কেনেন?",
            "options": {
                "1": "মেকআপ (লিপস্টিক, ফাউন্ডেশন, ইত্যাদি)",
                "2": "পারফিউম/ফ্র্যাগরেন্স",
                "3": "স্কিনকেয়ার (ক্রিম, সিরাম, লোশন, ইত্যাদি)",
                "4": "চুলের যত্নের পণ্য"
            }
        },
        "4BS": {
            "type": "radio",
            "question": "বিউটি/স্কিনকেয়ার পণ্যের পেছনে আপনার মাসিক গড় খরচ কত?",
            "options": {
                "1": "১০০০ টাকার নিচে",
                "2": "১০০০-১৫০০ টাকা",
                "3": "১৫০০-২০০০ টাকা",
                "4": "২০০০ টাকার উপরে"
            }
        },
        "5BS": {
            "type": "radio",
            "question": "বিউটি/স্কিনকেয়ারের জন্য আপনি কি দেশি নাকি বিদেশি ব্র্যান্ড পছন্দ করেন?",
            "options": {
                "1": "দেশি ব্র্যান্ড",
                "2": "বিদেশি ব্র্যান্ড",
                "3": "উভয়ই"
            }
        },
        "6BS": {
            "type": "radio",
            "question": "বিউটি/স্কিনকেয়ার কেনার সিদ্ধান্তে কোন বিষয়গুলি আপনাকে সবচেয়ে বেশি প্রভাবিত করে?",
            "options": {
                "1": "ব্র্যান্ডের সুনাম",
                "2": "পণ্যের গুণমান/উপাদান",
                "3": "দাম/সাশ্রয়ীতা",
                "4": "প্যাকেজিং ও ডিজাইন",
                "5": "অনলাইন রিভিউ/সুপারিশ",
                "6": "ডিসকাউন্ট/অফার"
            }
        },
        "7BS": {
            "type": "radio",
            "question": "আপনি যখন বিউটি বা স্কিনকেয়ার পণ্য ব্যবহার করেন, তখন আপনার জীবনে এটি সবচেয়ে বেশি কী যোগ করে বলে আপনি মনে করেন?",
            "options": {
                "1": "আমার আত্মবিশ্বাস বাড়ানো",
                "2": "আকর্ষণীয়তা",
                "3": "সামাজিক ভাবমূর্তি/অবস্থান",
                "4": "নিজের যত্ন ও আরাম",
                "5": "ফ্যাশন/বিউটি ট্রেন্ড অনুসরণ করা",
                "6": "শুধু কার্যকরী ব্যবহার"
            }
        },
        "8BS": {
            "type": "radio",
            "question": "আপনার স্কিনকেয়ার/মেকআপ পছন্দের ক্ষেত্রে প্রাকৃতিক/জৈব উপাদান কতটা গুরুত্বপূর্ণ?",
            "options": {
                "1": "খুব গুরুত্বপূর্ণ",
                "2": "মোটামুটি গুরুত্বপূর্ণ",
                "3": "গুরুত্বপূর্ণ নয়"
            }
        },
        "9BS": {
            "type": "radio",
            "question": "বিউটি/স্কিনকেয়ার পণ্য কেনার সময় আপনি কী কী সমস্যার সম্মুখীন হন?",
            "options": {
                "1": "উচ্চ মূল্য",
                "2": "আসল পণ্যের অভাব",
                "3": "উপযুক্ত শেড/ধরণ খুঁজে পেতে অসুবিধা",
                "4": "ত্বকে বিরূপ প্রতিক্রিয়ার ঝুঁকি",
                "5": "অন্যান্য:"
            }
        },
        "10BS": {
            "type": "radio",
            "question": "আপনি কোন পণ্যগুলি বাংলাদেশে আরও সহজে পেতে চান?",
            "options": {
                "1": "বিদেশি স্কিনকেয়ার (কোরিয়ান, ফ্রান্স ইত্যাদি)",
                "2": "লাক্সারি পারফিউম",
                "3": "সাশ্রয়ী জৈব স্কিনকেয়ার",
                "4": "অন্যান্য:"
            }
        }
    }
}

food ={
    "en":{
       "1PF": {
            "type": "radio",
            "question": "How often do you purchase these dry/packaged food items?",
            "options": {
                "1": "Frequently (monthly or more)",
                "2": "Sometimes (every 2–3 months)",
                "3": "Rarely (1–2 times/year)",
                "4": "Never"
            }
        },
        "2PF": {
            "type": "radio",
            "question": "Where do you usually shop your dry/packeged food items?",
            "options": {
                "1": "Social media shops (Facebook/Instagram)",
                "2": "Online platforms (Daraz, etc.)",
                "3": "Supermarket/Grocery store",
                "4": "Local markets"
            }
        },
        "3PF":{
            "type": "radio",
            "question": "What type of dry/packaged food do you usually buy for yourself or your family?",
            "options": {
                "1": "Dry fruits/Nuts",
                "2": "Chocolate/Sweets",
                "3": "Instant noodles/Ramen",
                "4": "Energy/Protein bars",
                "5": "Others:"
            }
        },
        "4PF":{
            "type": "radio",
            "question": "How much do you usually spend monthly on packaged snacks/dry foods?",
            "options": {
                "1": "Under 1000",
                "2": "1000-1500",
                "3": "1500-2000",
                "4": "Above 2000"
            }
        },
        "5PF":{
            "type":"radio",
            "question":"What influences your purchase the most when choosing packaged snacks/foods?",
            "options":{
                "1": "Price / Affordability",
                "2": "Taste & flavor variety",
                "3": "Brand reputation",
                "4": "Health / Nutrition value",
                "5": "Attractive packaging",
                "6": "Availability / Easy access"
            }
        },
        "6PF":{
            "type":"radio",
            "question":"Do you feel there is any gap in the current market of packaged dry food?",
            "options":{
                "1": "Need more helathier/organic options",
                "2": "More affordable packs needed",
                "3": "More local/traditional snack",
                "4": "Satisfied with existing products",
                "5": "Others:"
            }
        },
        "7PF":{
            "type":"radio",
            "question":"If you think about why you buy snacks/dry food, which reason matches you most?",
            "options":{
                "1": "For quick hunger solution",
                "2": "For sharing with family/friends",
                "3": "For health benefits",
                "4": "For hostipitality",
                "5": "For mantian everyday diets",
                "6": "Not a specific reason"
            }
        } 
    },
    "bn":{
        "1PF": {
            "type": "radio",
            "question": "আপনি কত ঘন ঘন এই শুকনো/প্যাকেটজাত খাবারগুলি কেনেন?",
            "options": {
                "1": "প্রায়শই (মাসিক বা তার বেশি)",
                "2": "মাঝে মাঝে (প্রতি ২-৩ মাস পর)",
                "3": "কদাচিৎ (বছরে ১-২ বার)",
                "4": "কখনোই না"
            }
        },
        "2PF": {
            "type": "radio",
            "question": "শুকনো/প্যাকেটজাত খাবারগুলি আপনি সাধারণত কোথা থেকে কেনেন?",
            "options": {
                "1": "সোশ্যাল মিডিয়া শপ (ফেসবুক/ইনস্টাগ্রাম)",
                "2": "অনলাইন প্ল্যাটফর্ম (দারাজ, ইত্যাদি)",
                "3": "সুপারশপ/মুদি দোকান",
                "4": "স্থানীয় বাজার"
            }
        },
        "3PF": {
            "type": "radio",
            "question": "আপনি সাধারণত নিজের বা পরিবারের জন্য কোন ধরনের শুকনো/প্যাকেটজাত খাবার কেনেন?",
            "options": {
                "1": "শুকনো ফল/বাদাম",
                "2": "চকলেট/মিষ্টি",
                "3": "ইনস্ট্যান্ট নুডুলস/রামেন",
                "4": "এনার্জি/প্রোটিন বার",
                "5": "অন্যান্য:"
            }
        },
        "4PF": {
            "type": "radio",
            "question": "প্যাকেটজাত স্ন্যাকস/শুকনো খাবারের জন্য আপনি সাধারণত মাসিক কত টাকা খরচ করেন?",
            "options": {
                "1": "১০০০ টাকার নিচে",
                "2": "১০০০-১৫০০ টাকা",
                "3": "১৫০০-২০০০ টাকা",
                "4": "২০০০ টাকার উপরে"
            }
        },
        "5PF": {
            "type": "radio",
            "question": "প্যাকেটজাত স্ন্যাকস/খাবার কেনার সময় কোন বিষয়গুলি আপনার সিদ্ধান্তকে সবচেয়ে বেশি প্রভাবিত করে?",
            "options": {
                "1": "দাম/সাশ্রয়ীতা",
                "2": "স্বাদ ও ফ্লেভারের বৈচিত্র্য",
                "3": "ব্র্যান্ডের সুনাম",
                "4": "স্বাস্থ্য/পুষ্টির মান",
                "5": "আকর্ষণীয় প্যাকেজিং",
                "6": "সহজলভ্যতা/সহজ অ্যাক্সেস"
            }
        },
        "6PF": {
            "type": "radio",
            "question": "শুকনো প্যাকেটজাত খাবারের বর্তমান বাজারে কোনো ঘাটতি আছে বলে আপনি মনে করেন?",
            "options": {
                "1": "আরও স্বাস্থ্যকর/জৈব বিকল্প প্রয়োজন",
                "2": "আরও সাশ্রয়ী প্যাকেজ প্রয়োজন",
                "3": "আরও স্থানীয়/ঐতিহ্যবাহী স্ন্যাকস",
                "4": "বর্তমান পণ্য নিয়ে সন্তুষ্ট",
                "5": "অন্যান্য:"
            }
        },
        "7PF": {
            "type": "radio",
            "question": "যদি আপনি স্ন্যাকস/শুকনো খাবার কেনার কারণ নিয়ে ভাবেন, কোন কারণটি আপনার সাথে সবচেয়ে বেশি মেলে?",
            "options": {
                "1": "দ্রুত ক্ষুধা মেটানোর জন্য",
                "2": "পরিবার/বন্ধুদের সাথে ভাগ করে নেওয়ার জন্য",
                "3": "স্বাস্থ্যগত সুবিধার জন্য",
                "4": "আতিথেয়তার জন্য",
                "5": "প্রতিদিনের খাবার বজায় রাখার জন্য",
                "6": "কোনো নির্দিষ্ট কারণ নেই"
            }
        }
    }
}

hobbies={
    "en":{
        "1HO":{
            "type":"radio",
            "question":"Which type of hobby-related products interest you the most?",
            "options":{
                "1": "Books & novels",
                "2": "Art supplies (paints, brushes, sketchbooks)",
                "3": "Craft/DIY kits (jewelry making, woodcraft, puzzles)",
                "4": "Collectibles (figures, models, posters)",
                "5": "Others:"
            }
        },
        "2HO": {
            "type": "radio",
            "question": "How often do you buy hobby-related products online?",
            "options": {
                "1": "Frequently (monthly or more)",
                "2": "Sometimes (every 2–3 months)",
                "3": "Rarely (1–2 times/year)",
                "4": "Never"
            }
        },
        "3HO": {
            "type": "radio",
            "question": "Where do you usually buy hobby-related products?",
            "options": {
                "1": "Social media shops (Facebook/Instagram)",
                "2": "Online platforms (Daraz, etc.)",
                "3": "Shopping Mall",
                "4": "Local markets"
            }
        },
        "4HO":{
            "type": "radio",
            "question": "What is the average amount you are willing to spend on hobby-related purchases per month?",
            "options": {
                "1": "Under 1000",
                "2": "1000-1500",
                "3": "1500-2000",
                "4": "Above 2000"
            }
        },
        "5HO":{
            "type": "radio",
            "question": "What factors influence your decision most when buying hobby-related products online?",
            "options": {
                "1": "Unique/rare availability",
                "2": "Product quality",
                "3": "Price",
                "4": "Brand or seller trust",
                "5": "Reviews from others"
            }
        },
        "6HO":{
            "type": "radio",
            "question": "Do you usually buy hobby products for yourself or as gifts for others?",
            "options": {
                "1": "For myself",
                "2": "For gifting",
                "3": "Both"
            }
        },
        "7HO":{
            "type": "checkbox",
            "question": "What is the biggest problem you face while shopping for hobby-related products?",
            "options": {
                "1": "Limited variety",
                "2": "High price compared to offline",
                "3": "Product quality not matching description",
                "4": "Delivery issues",
                "5": "Lack of trustworthy sellers",
                "6": "Others:"
            }
        }
    },
    "bn":{
        "1HO": {
            "type": "radio",
            "question": "কোন ধরনের শখ-সম্পর্কিত পণ্যে আপনি সবচেয়ে বেশি আগ্রহী?",
            "options": {
                "1": "বই ও উপন্যাস",
                "2": "আর্ট সামগ্রী (রঙ, তুলি, স্কেচবুক)",
                "3": "হস্তশিল্প/DIY কিট (গহনা তৈরি, কাঠের কাজ, পাজল)",
                "4": "সংগ্রহযোগ্য জিনিস (মূর্তি, মডেল, পোস্টার)",
                "5": "অন্যান্য:"
            }
        },
        "2HO": {
            "type": "radio",
            "question": "আপনি কত ঘন ঘন অনলাইনে শখ-সম্পর্কিত পণ্য কেনেন?",
            "options": {
                "1": "প্রায়শই (মাসিক বা তার বেশি)",
                "2": "মাঝে মাঝে (প্রতি ২-৩ মাস পর)",
                "3": "কদাচিৎ (বছরে ১-২ বার)",
                "4": "কখনোই না"
            }
        },
        "3HO": {
            "type": "radio",
            "question": "আপনি সাধারণত শখ-সম্পর্কিত পণ্য কোথা থেকে কেনেন?",
            "options": {
                "1": "সোশ্যাল মিডিয়া শপ (ফেসবুক/ইনস্টাগ্রাম)",
                "2": "অনলাইন প্ল্যাটফর্ম (দারাজ, ইত্যাদি)",
                "3": "শপিং মল",
                "4": "স্থানীয় বাজার"
            }
        },
        "4HO": {
            "type": "radio",
            "question": "প্রতি মাসে শখ-সম্পর্কিত কেনাকাটায় আপনি সাধারণত কত টাকা খরচ করতে ইচ্ছুক?",
            "options": {
                "1": "১০০০ টাকার নিচে",
                "2": "১০০০-১৫০০ টাকা",
                "3": "১৫০০-২০০০ টাকা",
                "4": "২০০০ টাকার উপরে"
            }
        },
        "5HO": {
            "type": "radio",
            "question": "অনলাইনে শখ-সম্পর্কিত পণ্য কেনার সময় কোন বিষয়গুলি আপনার সিদ্ধান্তকে সবচেয়ে বেশি প্রভাবিত করে?",
            "options": {
                "1": "অনন্য/বিরল সহজলভ্যতা",
                "2": "পণ্যের গুণমান",
                "3": "দাম",
                "4": "ব্র্যান্ড বা বিক্রেতার বিশ্বাসযোগ্যতা",
                "5": "অন্যদের রিভিউ"
            }
        },
        "6HO": {
            "type": "radio",
            "question": "আপনি সাধারণত নিজের জন্য নাকি অন্যদের উপহার হিসেবে শখের জিনিস কেনেন?",
            "options": {
                "1": "নিজের জন্য",
                "2": "উপহার হিসেবে",
                "3": "উভয়ই"
            }
        },
        "7HO": {
            "type": "checkbox",
            "question": "শখ-সম্পর্কিত পণ্য কেনার সময় আপনি কোন সবচেয়ে বড় সমস্যার মুখোমুখি হন?",
            "options": {
                "1": "সীমিত বৈচিত্র্য",
                "2": "অফলাইনের তুলনায় উচ্চ মূল্য",
                "3": "পণ্যের গুণমান বর্ণনার সাথে মেলে না",
                "4": "ডেলিভারি সমস্যা",
                "5": "বিশ্বস্ত বিক্রেতার অভাব",
                "6": "অন্যান্য:"
            }
        }
    }
}

homeDecor = {
    "en":{
        "1HD":{
            "type":"checkbox",
            "question":"Which types of home décor products attract you the most? (Select multiple if needed)",
            "options":{
                "1": "Wall art/paintings/posters",
                "2": "Decorative lights/lamps",
                "3": "Small furniture (shelves, stands, etc.)",
                "4": "Plants/artificial greenery",
                "5": "Showpieces/statues/crafts",
                "6": "Others:"
            }
        },
        "2HD": {
            "type": "radio",
            "question": "How often do you buy home décor items?",
            "options": {
                "1": "Frequently (monthly or more)",
                "2": "Sometimes (every 2–3 months)",
                "3": "Rarely (1–2 times/year)",
                "4": "Never"
            }
        },
        "3HD": {
            "type": "radio",
            "question": "Where do you usually buy home décor items from?",
            "options": {
                "1": "Social media shops (Facebook/Instagram)",
                "2": "Online platforms (Daraz, etc.)",
                "3": "Shopping Mall",
                "4": "Local markets"
            }
        },
        "4HD":{
            "type": "radio",
            "question": "What price range do you usually spend on home décor items?",
            "options": {
                "1": "Under 1000",
                "2": "1000-1500",
                "3": "1500-2000",
                "4": "Above 2000"
            }
        },
        "5HD":{
            "type": "radio",
            "question": "When buying home décor items online, which factor matters most to you?",
            "options": {
                "1": "Price affordability",
                "2": "Product design/uniqueness",
                "3": "Quality & durability",
                "4": "Delivery speed",
                "5": "Return/Exchange policy"
            }
        },
        "6HD":{
            "type": "radio",
            "question": "Do you buy home décor items for personal use or mainly as gifts?",
            "options": {
                "1": "For Persornal user",
                "2": "For gifting",
                "3": "Both"
            }
        },
        "7HD":{
            "type": "radio",
            "question": "Do you prefer modern/minimalist designs or traditional/cultural designs in home décor?",
            "options": {
                "1": "Modern designs",
                "2": "Traditional designs",
                "3": "Both"
            }
        },
        "8HD":{
            "type": "checkbox",
            "question": "What challenges do you face when buying home décor online?",
            "options": {
                "1": "Lack of trust in product quality",
                "2": "High price compared to physical shops",
                "3": "Limited product variety",
                "4": "Delivery issues",
                "5": "Lack of varient designs",
                "6": "Others:"
            }
        },
        "9HD":{
            "type": "radio",
            "question": "When decorating your home, which statement best describes you?",
            "options": {
                "1": "I want my home to feel cozy and comfortable",
                "2": "I want my home to look stylish and trendy.",
                "3": "I prefer traditional/cultural vibes in my home.",
                "4": "I don’t invest much in décor; I keep it simple."
            }
        }    
    },
    "bn":{
        "1HD": {
            "type": "checkbox",
            "question": "কোন ধরনের ঘরের সাজসজ্জার পণ্য আপনাকে সবচেয়ে বেশি আকর্ষণ করে? (প্রয়োজনে একাধিক নির্বাচন করুন)",
            "options": {
                "1": "দেয়ালের শিল্পকর্ম/পেইন্টিং/পোস্টার",
                "2": "সাজানোর আলো/ল্যাম্প",
                "3": "ছোট আসবাবপত্র (সেলফ, স্ট্যান্ড, ইত্যাদি)",
                "4": "গাছপালা/কৃত্রিম সবুজ",
                "5": "শোপিস/ভাস্কর্য/হস্তশিল্প",
                "6": "অন্যান্য:"
            }
        },
        "2HD": {
            "type": "radio",
            "question": "আপনি কত ঘন ঘন ঘরের সাজসজ্জার জিনিস কেনেন?",
            "options": {
                "1": "প্রায়শই (মাসিক বা তার বেশি)",
                "2": "মাঝে মাঝে (প্রতি ২-৩ মাস পর)",
                "3": "কদাচিৎ (বছরে ১-২ বার)",
                "4": "কখনোই না"
            }
        },
        "3HD": {
            "type": "radio",
            "question": "আপনি সাধারণত কোথা থেকে ঘরের সাজসজ্জার জিনিস কেনেন?",
            "options": {
                "1": "সোশ্যাল মিডিয়া শপ (ফেসবুক/ইনস্টাগ্রাম)",
                "2": "অনলাইন প্ল্যাটফর্ম (দারাজ, ইত্যাদি)",
                "3": "শপিং মল",
                "4": "স্থানীয় বাজার"
            }
        },
        "4HD": {
            "type": "radio",
            "question": "ঘরের সাজসজ্জার জিনিস কেনার জন্য আপনার সাধারণত কত টাকা খরচ করেন?",
            "options": {
                "1": "১০০০ টাকার নিচে",
                "2": "১০০০-১৫০০ টাকা",
                "3": "১৫০০-২০০০ টাকা",
                "4": "২০০০ টাকার উপরে"
            }
        },
        "5HD": {
            "type": "radio",
            "question": "অনলাইনে ঘরের সাজসজ্জার জিনিস কেনার সময় কোন বিষয়গুলি আপনার কাছে সবচেয়ে গুরুত্বপূর্ণ?",
            "options": {
                "1": "সাশ্রয়ী মূল্য",
                "2": "পণ্যের ডিজাইন/অনন্যতা",
                "3": "গুণমান ও স্থায়িত্ব",
                "4": "ডেলিভারির গতি",
                "5": "ফেরত/বিনিময় নীতি"
            }
        },
        "6HD": {
            "type": "radio",
            "question": "আপনি কি নিজের ব্যবহারের জন্য নাকি প্রধানত উপহার হিসেবে ঘরের সাজসজ্জার জিনিস কেনেন?",
            "options": {
                "1": "নিজের ব্যবহারের জন্য",
                "2": "উপহার হিসেবে",
                "3": "উভয়ই"
            }
        },
        "7HD": {
            "type": "radio",
            "question": "ঘরের সাজসজ্জায় আপনি কি আধুনিক/মিনিমালিস্ট ডিজাইন নাকি ঐতিহ্যবাহী/সাংস্কৃতিক ডিজাইন পছন্দ করেন?",
            "options": {
                "1": "আধুনিক ডিজাইন",
                "2": "ঐতিহ্যবাহী ডিজাইন",
                "3": "উভয়ই"
            }
        },
        "8HD": {
            "type": "checkbox",
            "question": "অনলাইনে ঘরের সাজসজ্জার জিনিস কেনার সময় আপনি কী কী সমস্যার মুখোমুখি হন?",
            "options": {
                "1": "পণ্যের গুণমানের উপর বিশ্বাসের অভাব",
                "2": "সরাসরি দোকানের তুলনায় উচ্চ মূল্য",
                "3": "পণ্যের সীমিত বৈচিত্র্য",
                "4": "ডেলিভারি সমস্যা",
                "5": "বিভিন্ন ডিজাইনের অভাব",
                "6": "অন্যান্য:"
            }
        },
        "9HD": {
            "type": "radio",
            "question": "আপনার ঘর সাজানোর ক্ষেত্রে, কোন উক্তিটি আপনার সাথে সবচেয়ে বেশি মেলে?",
            "options": {
                "1": "আমি চাই আমার ঘরটি আরামদায়ক এবং স্বাচ্ছন্দ্যময় হোক।",
                "2": "আমি চাই আমার ঘরটি স্টাইলিশ এবং আধুনিক দেখাক।",
                "3": "আমি আমার ঘরে ঐতিহ্যবাহী/সাংস্কৃতিক ভাব পছন্দ করি।",
                "4": "আমি সাজসজ্জায় বেশি বিনিয়োগ করি না; আমি এটাকে সাধারণ রাখি।"
            }
        }
    }
}

homeKitchen = {
    "en":{
        "1HK":{
            "type":"checkbox",
            "question":"What type of kitchen essentials do you prefer to buy most? (Select multiple if needed)",
            "options":{
                "1": "Cookware (pans, pots, non-stick)",
                "2": "Kitchen Gadgets(blender, juicer etc)",
                "3": "Tableware (plates, glasses, cutlery)",
                "4": "Cleaning products (mops, brushes, organizers)",
                "5": "Utensils & tools (spoons, knives, peelers, etc.)",
                "6": "Others:"
            }
        },
        "2HK": {
            "type": "radio",
            "question": "How often do you purchase kitchen/home essentials?",
            "options": {
                "1": "Frequently (monthly or more)",
                "2": "Sometimes (every 2–3 months)",
                "3": "Rarely (1–2 times/year)",
                "4": "Never"
            }
        },
        "3HK": {
            "type": "radio",
            "question": "Where do you usually buy kitchen essentials?",
            "options": {
                "1": "Social media shops (Facebook/Instagram)",
                "2": "Online platforms (Daraz, etc.)",
                "3": "Shopping Mall",
                "4": "Local markets"
            }
        },
        "4HK":{
            "type": "radio",
            "question": "How much are you willing to spend on kitchen essentials in one purchase?",
            "options": {
                "1": "Under 1000",
                "2": "1000-1500",
                "3": "1500-2000",
                "4": "Above 2000"
            }
        },
        "5HK":{
            "type": "radio",
            "question": "When buying kitchen essentials, what do you value most?",
            "options": {
                "1": "Price affordability",
                "2": "Product design/uniqueness",
                "3": "Quality & durability",
                "4": "Brand",
                "5": "Eco-friendliness"
            }
        },
        "6HK":{
            "type": "radio",
            "question": "Would you consider buying kitchen items from a Facebook store?",
            "options": {
                "1": "Yes",
                "2": "No"
            }
        },
        "7HK":{
            "type": "checkbox",
            "question": "What is the main challenge you face when buying home & kitchen products online?",
            "options": {
                "1": "Not sure about product quality",
                "2": "High price compared to physical shops",
                "3": "Limited product variety",
                "4": "High delivery charges",
                "5": "Lack of varient designs",
                "6": "Others:"
            }
        }
    },
    "bn":{
        "1HK": {
            "type": "checkbox",
            "question": "আপনি কোন ধরনের রান্নাঘরের প্রয়োজনীয় জিনিস সবচেয়ে বেশি কিনতে পছন্দ করেন? (প্রয়োজনে একাধিক নির্বাচন করুন)",
            "options": {
                "1": "রান্নার সরঞ্জাম (প্যান, হাঁড়ি, নন-স্টিক)",
                "2": "রান্নাঘরের গ্যাজেট (ব্লেন্ডার, জুসার ইত্যাদি)",
                "3": "খাবারের প্লেট ও কাপ (প্লেট, গ্লাস, চামচ ইত্যাদি)",
                "4": "পরিষ্কার করার পণ্য (মোছা, ব্রাশ, অর্গানাইজার)",
                "5": "ব্যবহারিক সরঞ্জাম ও সরঞ্জাম (চামচ, ছুরি, পিলার, ইত্যাদি)",
                "6": "অন্যান্য:"
            }
        },
        "2HK": {
            "type": "radio",
            "question": "আপনি কত ঘন ঘন রান্নাঘরের/বাসার প্রয়োজনীয় জিনিস কেনেন?",
            "options": {
                "1": "প্রায়শই (মাসিক বা তার বেশি)",
                "2": "মাঝে মাঝে (প্রতি ২-৩ মাস পর)",
                "3": "কদাচিৎ (বছরে ১-২ বার)",
                "4": "কখনোই না"
            }
        },
        "3HK": {
            "type": "radio",
            "question": "আপনি সাধারণত রান্নাঘরের প্রয়োজনীয় জিনিস কোথা থেকে কেনেন?",
            "options": {
                "1": "সোশ্যাল মিডিয়া শপ (ফেসবুক/ইনস্টাগ্রাম)",
                "2": "অনলাইন প্ল্যাটফর্ম (দারাজ, ইত্যাদি)",
                "3": "শপিং মল",
                "4": "স্থানীয় বাজার"
            }
        },
        "4HK": {
            "type": "radio",
            "question": "একবারে রান্নাঘরের প্রয়োজনীয় জিনিস কিনতে আপনি কত টাকা খরচ করতে ইচ্ছুক?",
            "options": {
                "1": "১০০০ টাকার নিচে",
                "2": "১০০০-১৫০০ টাকা",
                "3": "১৫০০-২০০০ টাকা",
                "4": "২০০০ টাকার উপরে"
            }
        },
        "5HK": {
            "type": "radio",
            "question": "রান্নাঘরের প্রয়োজনীয় জিনিস কেনার সময় আপনি কোনটিকে সবচেয়ে বেশি গুরুত্ব দেন?",
            "options": {
                "1": "সাশ্রয়ী মূল্য",
                "2": "পণ্যের ডিজাইন/অনন্যতা",
                "3": "গুণমান ও স্থায়িত্ব",
                "4": "ব্র্যান্ড",
                "5": "পরিবেশ-বান্ধবতা"
            }
        },
        "6HK": {
            "type": "radio",
            "question": "আপনি কি ফেসবুক স্টোর থেকে রান্নাঘরের জিনিস কেনা বিবেচনা করবেন?",
            "options": {
                "1": "হ্যাঁ",
                "2": "না"
            }
        },
        "7HK": {
            "type": "checkbox",
            "question": "অনলাইনে বাসা ও রান্নাঘরের পণ্য কেনার সময় আপনার প্রধান সমস্যা কী?",
            "options": {
                "1": "পণ্যের গুণমান সম্পর্কে নিশ্চিত না",
                "2": "সরাসরি দোকানের তুলনায় উচ্চ মূল্য",
                "3": "পণ্যের সীমিত বৈচিত্র্য",
                "4": "উচ্চ ডেলিভারি চার্জ",
                "5": "বিভিন্ন ডিজাইনের অভাব",
                "6": "অন্যান্য:"
            }
        }
    }
}

gadget = {
    "en":{
        "1EG":{
            "type":"checkbox",
            "question":"Which type of electronic gadgets or accessories do you usually buy online? (Select multiple if needed)",
            "options":{
                "1": "Phone accessories (covers, chargers, tempered glass)",
                "2": "Earphones / Headphones / Airpods",
                "3": "Smartwatches / Fitness trackers",
                "4": "Power banks / USB cables",
                "5": "Small appliances (blender, toaster, etc.)",
                "6": "Others:"
            }
        },
        "2EG": {
            "type": "radio",
            "question": "How often do you buy electronic gadgets/accessories online?",
            "options": {
                "1": "Frequently (monthly or more)",
                "2": "Sometimes (every 2–3 months)",
                "3": "Rarely (1–2 times/year)",
                "4": "Never"
            }
        },
        "3EG": {
            "type": "radio",
            "question": "Where do you usually buy electronics?",
            "options": {
                "1": "Social media shops (Facebook/Instagram)",
                "2": "Online platforms (Daraz, etc.)",
                "3": "Shopping Mall",
                "4": "Local markets"
            }
        },
        "4EG":{
            "type": "radio",
            "question": "What price range do you usually consider for small gadgets/accessories",
            "options": {
                "1": "Under 1000",
                "2": "1000-1500",
                "3": "1500-2000",
                "4": "Above 2000"
            }
        },
        "5EG":{
            "type": "radio",
            "question": "When buying electronics online, which factor influences you most?",
            "options": {
                "1": "Price affordability",
                "2": "Reviews & recommendations",
                "3": "Quality & durability",
                "4": "Brand",
                "5": "Warranty / after-sales service"
            }
        },
        "6EG":{
            "type": "radio",
            "question": "Do you prefer popular branded products or high-quality non-popular branded items?",
            "options": {
                "1": "Only Popular branded",
                "2": "Open to non-popular branded if quality is good",
                "3": "Doesn’t matter, price is most important"
            }
        },
        "7EG":{
            "type": "radio",
            "question": "What stops you from buying gadgets online?",
            "options": {
                "1": "Risk of fake products",
                "2": "High price",
                "3": "Limited variety",
                "4": "Delivery delay or damage",
                "5": "Others:"
            }
        },
        "8EG":{
            "type": "radio",
            "question": "Why do you usually buy electronic gadgets/accessories?",
            "options": {
                "1": "Personal use / convenience",
                "2": "For gifting",
                "3": "Trendy / status symbol",
                "4": "Hobby / tech interest"
            }
        }
    },
    "bn":{
        "1EG": {
            "type": "checkbox",
            "question": "আপনি সাধারণত কোন ধরনের ইলেকট্রনিক গ্যাজেট বা অনুষঙ্গ অনলাইনে কেনেন? (প্রয়োজনে একাধিক নির্বাচন করুন)",
            "options": {
                "1": "ফোনের আনুষঙ্গিক (কভার, চার্জার, টেম্পারড গ্লাস)",
                "2": "ইয়ারফোন/হেডফোন/এয়ারপডস",
                "3": "স্মার্টওয়াচ/ফিটনেস ট্র্যাকার",
                "4": "পাওয়ার ব্যাংক/ইউএসবি ক্যাবল",
                "5": "ছোট যন্ত্রপাতি (ব্লেন্ডার, টোস্টার, ইত্যাদি)",
                "6": "অন্যান্য:"
            }
        },
        "2EG": {
            "type": "radio",
            "question": "আপনি কত ঘন ঘন অনলাইনে ইলেকট্রনিক গ্যাজেট/আনুষঙ্গিক কেনেন?",
            "options": {
                "1": "প্রায়শই (মাসিক বা তার বেশি)",
                "2": "মাঝে মাঝে (প্রতি ২-৩ মাস পর)",
                "3": "কদাচিৎ (বছরে ১-২ বার)",
                "4": "কখনোই না"
            }
        },
        "3EG": {
            "type": "radio",
            "question": "আপনি সাধারণত কোথা থেকে ইলেকট্রনিক্স কেনেন?",
            "options": {
                "1": "সোশ্যাল মিডিয়া শপ (ফেসবুক/ইনস্টাগ্রাম)",
                "2": "অনলাইন প্ল্যাটফর্ম (দারাজ, ইত্যাদি)",
                "3": "শপিং মল",
                "4": "স্থানীয় বাজার"
            }
        },
        "4EG": {
            "type": "radio",
            "question": "ছোট গ্যাজেট/আনুষঙ্গিকের জন্য আপনি সাধারণত কত টাকার বাজেট রাখেন?",
            "options": {
                "1": "১০০০ টাকার নিচে",
                "2": "১০০০-১৫০০ টাকা",
                "3": "১৫০০-২০০০ টাকা",
                "4": "২০০০ টাকার উপরে"
            }
        },
        "5EG": {
            "type": "radio",
            "question": "অনলাইনে ইলেকট্রনিক্স কেনার সময় কোন বিষয়টি আপনাকে সবচেয়ে বেশি প্রভাবিত করে?",
            "options": {
                "1": "সাশ্রয়ী মূল্য",
                "2": "রিভিউ ও সুপারিশ",
                "3": "গুণমান ও স্থায়িত্ব",
                "4": "ব্র্যান্ড",
                "5": "ওয়ারেন্টি/বিক্রয়োত্তর সেবা"
            }
        },
        "6EG": {
            "type": "radio",
            "question": "আপনি কি জনপ্রিয় ব্র্যান্ডেড পণ্য নাকি উচ্চ মানের অজনপ্রিয় ব্র্যান্ডের জিনিস পছন্দ করেন?",
            "options": {
                "1": "শুধুমাত্র জনপ্রিয় ব্র্যান্ডেড",
                "2": "গুণমান ভালো হলে অজনপ্রিয় ব্র্যান্ডেও আপত্তি নেই",
                "3": "ব্যাপার না, দামটাই সবচেয়ে গুরুত্বপূর্ণ"
            }
        },
        "7EG": {
            "type": "radio",
            "question": "অনলাইনে গ্যাজেট কেনা থেকে আপনাকে কী বিরত রাখে?",
            "options": {
                "1": "নকল পণ্যের ঝুঁকি",
                "2": "উচ্চ মূল্য",
                "3": "সীমিত বৈচিত্র্য",
                "4": "ডেলিভারি বিলম্ব বা ক্ষতি",
                "5": "অন্যান্য:"
            }
        },
        "8EG": {
            "type": "radio",
            "question": "আপনি সাধারণত কেন ইলেকট্রনিক গ্যাজেট/আনুষঙ্গিক কেনেন?",
            "options": {
                "1": "ব্যক্তিগত ব্যবহার/সুবিধার জন্য",
                "2": "উপহার হিসেবে দেওয়ার জন্য",
                "3": "ফ্যাশন/স্ট্যাটাস সিম্বল হিসেবে",
                "4": "শখ/প্রযুক্তিগত আগ্রহের জন্য"
            }
        }
    }
}

babyKids = {
    "en":{
        "1BK":{
            "type":"checkbox",
            "question":"Which baby/kids products do you spend on the most?  (Select multiple if needed)",
            "options":{
                "1": "Baby food/snacks",
                "2": "Baby gear (stroller, carrier, walker)",
                "3": "Baby skincare & healthcare",
                "4": "Educational toys & books",
                "5": "Kids clothing & footwear",
                "6": "Kids furniture & décor",
                "7": "Feeding essentials (bottles, sippers, sterilizers)",
                "8": "Safety items (baby gates, mosquito nets, locks)"
            }
        },
        "2BK": {
            "type": "radio",
            "question": "How often do you buy baby & kids essentials?",
            "options": {
                "1": "Frequently (monthly or more)",
                "2": "Sometimes (every 2–3 months)",
                "3": "Rarely (1–2 times/year)",
                "4": "Never"
            }
        },
        "3BK": {
            "type": "radio",
            "question": "Where do you usually purchase baby/kids essentials?",
            "options": {
                "1": "Social media shops (Facebook/Instagram)",
                "2": "Online platforms (Daraz, etc.)",
                "3": "Supermarket",
                "4": "Local markets"
            }
        },
        "4BK":{
            "type": "radio",
            "question": "What’s your usual spending on baby/kids essentials?",
            "options": {
                "1": "Under 1000",
                "2": "1000-1500",
                "3": "1500-2000",
                "4": "Above 2000"
            }
        },
        "5BK":{
            "type": "radio",
            "question": "What do you value most when purchasing baby/kids products?",
            "options": {
                "1": "Price affordability",
                "2": "Educational value",
                "3": "Brand reputation",
                "4": "Durability/quality",
                "5": "Safety & health standards",
                "6": "Attractive design/style"
            }
        },
        "6BK":{
            "type": "radio",
            "question": "Are you willing to pay more for:",
            "options": {
                "1": "Organic/chemical-free baby products",
                "2": "Educational toys",
                "3": "Imported/foreign brands",
                "4": "Eco-friendly/sustainable items"
            }
        },
        "7BK":{
            "type": "checkbox",
            "question": "Which baby/kids products do you feel are difficult to find in Bangladesh?",
            "options": {
                "1": "High-quality toys & learning kits",
                "2": "Affordable organic baby food",
                "3": "Comfortable and stylish kids’ clothes",
                "4": "Safe baby skincare & hygiene items",
                "5": "Sturdy and durable school supplies",
                "6": "Others:"
            }
        }
    },
    "bn":{
        "1BK": {
            "type": "checkbox",
            "question": "আপনি বাচ্চাদের কোন ধরনের পণ্যের পেছনে সবচেয়ে বেশি খরচ করেন? (প্রয়োজনে একাধিক নির্বাচন করুন)",
            "options": {
                "1": "শিশুদের খাবার/স্ন্যাকস",
                "2": "শিশুদের সরঞ্জাম (স্ট্রলার, ক্যারিয়ার, ওয়াকার)",
                "3": "শিশুদের ত্বক ও স্বাস্থ্য পরিচর্যা",
                "4": "শিক্ষামূলক খেলনা ও বই",
                "5": "বাচ্চাদের পোশাক ও জুতো",
                "6": "বাচ্চাদের আসবাবপত্র ও সাজসজ্জা",
                "7": "খাওয়ানোর প্রয়োজনীয় জিনিস (বোতল, সিপার, স্টেরিলাইজার)",
                "8": "নিরাপত্তার সরঞ্জাম (বেবি গেট, মশারি, তালা)"
            }
        },
        "2BK": {
            "type": "radio",
            "question": "আপনি কত ঘন ঘন শিশু ও বাচ্চাদের প্রয়োজনীয় জিনিস কেনেন?",
            "options": {
                "1": "প্রায়শই (মাসিক বা তার বেশি)",
                "2": "মাঝে মাঝে (প্রতি ২-৩ মাস পর)",
                "3": "কদাচিৎ (বছরে ১-২ বার)",
                "4": "কখনোই না"
            }
        },
        "3BK": {
            "type": "radio",
            "question": "আপনি সাধারণত শিশু/বাচ্চাদের প্রয়োজনীয় জিনিস কোথা থেকে কেনেন?",
            "options": {
                "1": "সোশ্যাল মিডিয়া শপ (ফেসবুক/ইনস্টাগ্রাম)",
                "2": "অনলাইন প্ল্যাটফর্ম (দারাজ, ইত্যাদি)",
                "3": "সুপার শপ",
                "4": "স্থানীয় বাজার"
            }
        },
        "4BK": {
            "type": "radio",
            "question": "শিশু/বাচ্চাদের প্রয়োজনীয় জিনিসের পেছনে আপনার স্বাভাবিক খরচ কত?",
            "options": {
                "1": "১০০০ টাকার নিচে",
                "2": "১০০০-১৫০০ টাকা",
                "3": "১৫০০-২০০০ টাকা",
                "4": "২০০০ টাকার উপরে"
            }
        },
        "5BK": {
            "type": "radio",
            "question": "শিশু/বাচ্চাদের পণ্য কেনার সময় আপনি কোনটিকে সবচেয়ে বেশি গুরুত্ব দেন?",
            "options": {
                "1": "সাশ্রয়ী মূল্য",
                "2": "শিক্ষাগত মূল্য",
                "3": "ব্র্যান্ডের সুনাম",
                "4": "স্থায়িত্ব/গুণমান",
                "5": "নিরাপত্তা ও স্বাস্থ্য মান",
                "6": "আকর্ষণীয় ডিজাইন/স্টাইল"
            }
        },
        "6BK": {
            "type": "radio",
            "question": "আপনি কি এর জন্য বেশি টাকা দিতে ইচ্ছুক?",
            "options": {
                "1": "জৈব/রাসায়নিকমুক্ত শিশুদের পণ্য",
                "2": "শিক্ষামূলক খেলনা",
                "3": "আমদানি করা/বিদেশি ব্র্যান্ড",
                "4": "পরিবেশ-বান্ধব/টেকসই সামগ্রী"
            }
        },
        "7BK": {
            "type": "checkbox",
            "question": "বাংলাদেশের বাজারে কোন ধরনের শিশু/বাচ্চাদের পণ্য খুঁজে পাওয়া কঠিন বলে আপনি মনে করেন?",
            "options": {
                "1": "উচ্চ মানের খেলনা ও শেখার কিট",
                "2": "সাশ্রয়ী জৈব শিশুদের খাবার",
                "3": "আরামদায়ক এবং স্টাইলিশ বাচ্চাদের পোশাক",
                "4": "নিরাপদ শিশুদের ত্বক ও স্বাস্থ্য পরিচর্যার সামগ্রী",
                "5": "শক্ত এবং টেকসই স্কুলের সামগ্রী",
                "6": "অন্যান্য:"
            }
        }
    }
}

end = {
    "en": {
        "END":{
            "type": "radio",
            "question": "When you discover a new online shop on Facebook, what is the MOST important factor for you to trust them?",
            "options": {
                "1": "Likes/Followers",
                "2": "High-quality photos and videos",
                "3": "Good reviews from customers",
                "4": "Recommendation from a friend or influencer",
                "5": "Others:"
            }
        }
    },
    "bn": {
        "END":{
            "type": "radio",
            "question": "ফেসবুকে একটি নতুন অনলাইন শপ খুঁজে পেলে, তাদের বিশ্বাস করার জন্য আপনার কাছে সবচেয়ে গুরুত্বপূর্ণ বিষয় কোনটি?",
            "options": {
                "1": "লাইক/ফলোয়ারের সংখ্যা",
                "2": "উচ্চ মানের ছবি এবং ভিডিও",
                "3": "ক্রেতাদের ভালো রিভিউ",
                "4": "বন্ধু বা কোনো ইনফ্লুয়েন্সারের সুপারিশ",
                "5": "অন্যান্য:"
            }
        }
    }
}

contact_prompts = {
    "en": "Before finishing, please provide your WhatsApp(11 digit) number or Email:",
    "bn": "শেষ করার আগে, অনুগ্রহ করে আপনার WhatsApp(11 digit) নাম্বার বা ইমেইল দিন:"
}