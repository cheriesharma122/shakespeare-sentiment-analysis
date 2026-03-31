import string
# Shakespeare sentiment analysis project

# Shakespeare Text Sample 
texts = [
    "To be, or not to be, that is the question: Whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune.",
    "Love looks not with the eyes, but with the mind, and therefore is winged Cupid painted blind. Love is a gentle madness, sweet and divine.",
    "Hell is empty and all the devils are here. The world is a dark and wretched place, full of misery and despair.",
    "What light through yonder window breaks? It is the east, and Juliet is the sun. Arise fair sun and kill the envious moon.",
    "Life is full of sorrow, pain and grief. The cruel fate hath cursed my soul with bitter tears and endless suffering.",
    "We know what we are, but know not what we may be. Hope is the companion of power and the mother of success.",
    "The course of true love never did run smooth, yet love remains the sweetest joy and the purest bliss of all.",
    "Cowardice is the enemy of the soul. Fear, hatred and treachery bring nothing but ruin, darkness and eternal disgrace."
]

# Expanded Sentiment Word Dictionaries 
positive_words = set([
    "love", "happy", "joy", "beautiful", "good", "sweet", "calm",
    "hope", "noble", "fair", "pure", "bliss", "gentle", "divine",
    "light", "arise", "success", "power", "bright", "glory", "grace",
    "sun", "companion", "triumph", "peace", "warmth", "kind", "blessed",
    "true", "sweetest", "purest", "smooth", "mother"
])

negative_words = set([
    "dark", "hate", "sad", "bad", "anger", "pain",
    "suffer", "sorrow", "misery", "despair", "wretched", "cruel",
    "cursed", "bitter", "grief", "ruin", "fear", "hatred", "disgrace",
    "treachery", "cowardice", "enemy", "empty", "outrageous",
    "devils", "tears", "suffering", "darkness", "eternal", "envious",
    "kill", "arrows", "fortune", "blind", "endless"
])

#Sentiment Analysis Function
def analyze_sentiment(text):

    # Step 1:# converting everything to lowercase for easier matching
    cleaned = text.lower()

    # Step 2: Removing punctuation
    cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))

    # Step 3: Tokenizing into words
    words = cleaned.split()

    # Step 4: Initializing counters
    pos_count = 0
    neg_count = 0
    matched_positive = []
    matched_negative = []

    # Step 5: Matching words against sentiment lists 
    seen = set()
    for word in words:
        if word in seen:
            continue
        if word in positive_words:
            pos_count += 1
            matched_positive.append(word)
            seen.add(word)
        elif word in negative_words:
            neg_count += 1
            matched_negative.append(word)
            seen.add(word)

    # Step 6: Calculate sentiment score
    score = pos_count - neg_count

    # Step 7: Classify sentiment
    if pos_count > neg_count:
        sentiment = "Positive 😊"
    elif neg_count > pos_count:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return sentiment, pos_count, neg_count, score, matched_positive, matched_negative


#Main Program
print("=" * 60)
print("     My Sentiment Analysis Project")
print("=" * 60)

positive_total = 0
negative_total = 0
neutral_total = 0

for i, t in enumerate(texts, 1):
    sentiment, pos, neg, score, pos_words, neg_words = analyze_sentiment(t)

    print(f"\n📖 Quote #{i}")
    print(f"   {t}")
    print(f"\n💬 Sentiment  : {sentiment}")
    print(f"✅ Positive   : {pos} word(s) → {pos_words if pos_words else 'None'}")
    print(f"❌ Negative   : {neg} word(s) → {neg_words if neg_words else 'None'}")
    print(f"📊 Score      : {score:+d}")
    print("-" * 60)

    # Track overall counts
    if "Positive" in sentiment:
        positive_total += 1
    elif "Negative" in sentiment:
        negative_total += 1
    else:
        neutral_total += 1

#Final Summary 
print("\n" + "=" * 60)
print("              FINAL SUMMARY")
print("=" * 60)
print(f"  Total Quotes Analyzed : {len(texts)}")
print(f"  😊 Positive Quotes    : {positive_total}")
print(f"  😞 Negative Quotes    : {negative_total}")
print(f"  😐 Neutral Quotes     : {neutral_total}")

#Overall Mood
if positive_total > negative_total:
    overall = "Overall Mood: Mostly Positive 😊"
elif negative_total > positive_total:
    overall = "Overall Mood: Mostly Negative 😞"
else:
    overall = "Overall Mood: Balanced 😐"

print(f"\n  {overall}")
print("=" * 60)