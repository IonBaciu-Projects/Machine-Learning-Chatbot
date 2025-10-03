import pickle
import difflib
from datetime import datetime, timezone
from pathlib import Path
from data import responses, training_data
import numpy as np

with open("model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

LOG_PATH = Path("chat_log.txt")

context = {"pending": None, "subtopic": None}

def normalize(user_input):
    return user_input.lower().strip()

def predict_category(user_input):
    X = vectorizer.transform([user_input])
    probs = model.predict_proba(X)[0]
    max_prob = np.max(probs)
    category = model.classes_[np.argmax(probs)]
    return category, max_prob

def handle_subtopic_answer(pending, user_input):
    ui = user_input.lower().strip()
    if pending == "malware-types":
        if ui in ["virus", "viruses"]:
            return responses["virus"], True
        if ui in ["worm", "worms"]:
            return responses["worm"], True
        if ui in ["trojan", "trojans", "trojan horse"]:
            return responses["trojan"], True
        if ui in ["ransomware", "crypto malware", "locker ransomware"]:
            return responses["ransomware"], True
        if ui in ["spyware", "keylogger"]:
            return responses["spyware"], True
        if ui in ["backdoor"]:
            return responses["backdoor"], True
        return "Please choose one of: virus, worm, trojan, ransomware, spyware, backdoor or type no.", False

    if pending == "linux-commands":
        if ui == "ls": return responses["ls"], True
        if ui == "chmod": return responses["chmod"], True
        if ui == "ps": return responses["ps"], True
        if ui == "grep": return responses["grep"], True
        if ui == "iptables": return responses["iptables"], True
        return "Please choose one of: ls, chmod, ps, grep, iptables, or type no.", False

    if pending == "programming-languages":
        if ui == "python": return responses["python"], True
        if ui in ["c"]: return responses["c"], True
        if ui in ["c++", "cpp"]: return responses["c++"], True
        if ui in ["c#", "csharp"]: return responses["c#"], True
        if ui == "java": return responses["java"], True
        if ui == "html": return responses["html"], True
        if ui == "css": return responses["css"], True
        return "Please choose one of: Python, C, C++, C#, Java, HTML, CSS or type no.", False

    if pending == "siem-tools":
        if ui == "splunk": return responses["splunk"], True
        if ui in ["elk", "elk stack"]: return responses["elk"], True
        if ui in ["qradar", "ibm qradar"]: return responses["qradar"], True
        return "Please choose one of: Splunk, ELK, QRadar or type no.", False

    return None, False


def chatbot_response(raw_input):
    user_input = normalize(raw_input)

    if context["pending"]:
        pending = context["pending"]

        if pending == "sql":
            if user_input in ["yes", "y"]:
                context["pending"] = None
                return responses.get("sql injection")
            elif user_input in ["no", "n"]:
                context["pending"] = None
                return "Okay. What else would you like to know?"

        elif pending == "linux":
            if user_input in ["yes", "y"]:
                context["pending"] = "linux-commands"
                return "Common Linux security commands: ls, chmod, ps, grep, iptables. Which one would you like me to explain?"
            elif user_input in ["no", "n"]:
                context["pending"] = None
                return "Okay. What else would you like to know?"

        elif pending == "programming":
            if user_input in ["yes", "y"]:
                context["pending"] = "programming-languages"
                return "Which language would you like to know about? (Python, C, C++, C#, Java, HTML, CSS)"
            elif user_input in ["no", "n"]:
                context["pending"] = None
                return "Okay. What else would you like to know?"

        elif pending == "siem":
            if user_input in ["yes", "y"]:
                context["pending"] = "siem-tools"
                return "Popular SIEM tools: Splunk, ELK Stack, QRadar. Which one would you like me to explain?"
            elif user_input in ["no", "n"]:
                context["pending"] = None
                return "Okay. What else would you like to know?"

        elif pending == "malware":
            if user_input in ["yes", "y"]:
                context["pending"] = "malware-types"
                return "Which malware would you like to know more about? (virus, worm, trojan, ransomware, spyware, backdoor)"
            elif user_input in ["no", "n"]:
                context["pending"] = None
                return "Okay. What else would you like to know?"

        elif pending == "database":
            if user_input in ["yes", "y"]:
                context["pending"] = "database-sub"
                return "Databases rely on authentication, encryption, and vulnerability assessments. Which would you like to hear about?"
            elif user_input in ["no", "n"]:
                context["pending"] = None
                return "Okay. What else would you like to know?"

        elif pending in ["malware-types", "linux-commands", "programming-languages", "siem-tools", "database-sub"]:
            result, matched = handle_subtopic_answer(pending, user_input)
            if matched:
                return f"{result} Would you like to know about another from this category? (yes/no)"
            else:
                if user_input in ["no", "n"]:
                    context["pending"] = None
                    return "Okay. What else would you like to know?"
                if user_input in ["yes", "y"]:
                    if pending == "malware-types":
                        return "Which malware would you like to know more about? (virus, worm, trojan, ransomware, spyware, backdoor)"
                    if pending == "linux-commands":
                        return "Which Linux command? (ls, chmod, ps, grep, iptables)"
                    if pending == "programming-languages":
                        return "Which language? (Python, C, C++, C#, Java, HTML, CSS)"
                    if pending == "siem-tools":
                        return "Which tool? (Splunk, ELK, QRadar)"
                    if pending == "database-sub":
                        return "Choose one: authentication, encryption, vulnerability assessments."
                return result

    try:
        category, confidence = predict_category(user_input)
    except:
        return "Work in progress, still learning. Please try asking in another way."

    if confidence < 0.2:
        close_matches = difflib.get_close_matches(user_input, [w for w, _ in training_data], n=1, cutoff=0.7)
        if close_matches:
            mapped = dict(training_data).get(close_matches[0])
            if mapped and mapped in responses:
                return responses[mapped]
        return "Work in progress, still learning. Please try asking in another way."

    if category in responses:
        if "Would you like" in responses[category] or "Which" in responses[category]:
            context["pending"] = category
        return responses[category]

    close_matches = difflib.get_close_matches(user_input, [w for w, _ in training_data], n=1, cutoff=0.8)
    if close_matches:
        mapped = dict(training_data).get(close_matches[0])
        if mapped and mapped in responses:
            return responses[mapped]
        return f"Did you mean '{close_matches[0]}'?"

    return "Work in progress, still learning. Please try asking in another way."


def log_chat(user_msg, bot_msg):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"[{now}] You: {user_msg}\n")
        f.write(f"[{now}] Chatbot: {bot_msg}\n")


def main():
    print("Cybersecurity ML Chatbot")
    print("This conversation is being recorded.")
    print("Type 'quit' to exit.\n")
    print("You can start by asking things like:")
    print("- What is SQL?")
    print("- What is Linux?")
    print("- What is Malware?")
    print("- What is SIEM?")
    print("- Tell me about Programming\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            farewell = "This conversation has been recorded. Goodbye!"
            print("Chatbot:", farewell)
            log_chat(user_input, farewell)
            break
        bot_reply = chatbot_response(user_input)
        print("Chatbot:", bot_reply)
        log_chat(user_input, bot_reply)


if __name__ == "__main__":
    main()