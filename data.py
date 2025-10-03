responses = {
    "sql": (
        "SQL (Structured Query Language) is used to manage and manipulate relational databases. "
        "In cybersecurity, poor SQL coding practices can lead to vulnerabilities such as SQL Injection. "
        "Would you like me to explain SQL Injection? (yes/no)"
    ),
    "sql injection": (
        "SQL Injection is a web attack where malicious SQL queries are inserted into inputs, "
        "allowing attackers to read, modify, or delete database contents. "
        "It can bypass authentication and compromise sensitive data."
    ),

    "linux": (
        "Linux is an open-source operating system widely used in cybersecurity, servers, "
        "penetration testing, and tools like Kali Linux. "
        "Would you like me to list common Linux security commands? (yes/no)"
    ),

    "programming": (
        "Programming is the process of creating instructions for computers to perform tasks. "
        "It is essential in cybersecurity for automation, exploit development, and analysis. "
        "Would you like to hear about specific languages such as Python, C++, or Java? (yes/no)"
    ),
    "python": "Python is a versatile programming language widely used in cybersecurity for scripting, automation, and data analysis.",
    "c": "C is a powerful low-level programming language used in system programming, operating systems, and exploit development.",
    "c++": "C++ builds on C with object-oriented features. It's used in performance-critical applications, malware development, and security tools.",
    "c#": "C# is a Microsoft language mainly used in enterprise apps. In security, it's often seen in Windows exploitation or reverse engineering.",
    "java": "Java is a cross-platform language used in enterprise apps. In cybersecurity, it's tied to web security and Android malware.",
    "html": "HTML (HyperText Markup Language) structures web pages. Security issues like XSS often exploit HTML/JavaScript.",
    "css": "CSS (Cascading Style Sheets) styles web pages. Attackers sometimes exploit CSS for obfuscation or clickjacking techniques.",

    "database": (
        "A database is an organized collection of data, typically managed by a database management system (DBMS). "
        "In cybersecurity, databases are prime targets for attacks such as SQL Injection. "
        "Would you like to know about authentication, encryption, or vulnerability assessments in databases? (yes/no)"
    ),
    "authentication": "Authentication verifies user identity, usually with passwords, tokens, or biometrics.",
    "encryption": "Encryption transforms data into unreadable form using algorithms and keys, protecting data at rest and in transit.",
    "vulnerability assessments": "Vulnerability assessments use scanners and reviews to identify security weaknesses before attackers exploit them.",

    "malware": (
        "Malware is malicious software designed to harm or exploit systems. "
        "Examples include viruses, worms, trojans, ransomware, and spyware. "
        "Which malware would you like to know more about? (virus, worm, trojan, ransomware, spyware, backdoor)?"
    ),
    "virus": "A virus attaches itself to files or programs, spreading when the file is executed.",
    "worm": "A worm is self-replicating malware that spreads across networks without user action.",
    "trojan": "A trojan disguises itself as legitimate software but delivers malicious payloads.",
    "ransomware": "Ransomware encrypts files and demands payment for decryption.",
    "spyware": "Spyware secretly monitors user activity, often capturing keystrokes or credentials.",
    "backdoor": "A backdoor is malware that provides unauthorized remote access to a system.",

    "siem": (
        "SIEM (Security Information and Event Management) collects, normalizes, and correlates logs to detect and investigate threats. "
        "Would you like me to list popular SIEM tools? (yes/no)"
    ),
    "splunk": "Splunk is a commercial SIEM platform used for log analysis, real-time monitoring, and security investigations.",
    "elk": "ELK Stack (Elasticsearch, Logstash, Kibana) is an open-source SIEM solution popular for log collection and visualization.",
    "qradar": "IBM QRadar is a SIEM used for threat detection, compliance, and incident response.",

    "detection": "Detection in cybersecurity is identifying malicious activity or anomalies in systems, logs, or networks.",
    "response": "Incident Response involves analyzing, containing, eradicating, and recovering from cybersecurity incidents.",

    "risk management": "Risk management is the process of identifying, assessing, and mitigating risks to systems and data.",
    "vulnerabilities": "Vulnerabilities are flaws or weaknesses in software, hardware, or processes that attackers can exploit."
}

training_data = [

    ("sql", "sql"), ("SQL", "sql"), ("Sql", "sql"),
    ("what is sql", "sql"), ("what’s sql", "sql"),
    ("tell me about sql", "sql"), ("explain sql", "sql"),
    ("structured query language", "sql"), ("sql basics", "sql"),
    ("sql database", "sql"), ("what is sql", "sql"), ("learn sql", "sql"),
    ("sql commands", "sql"), ("sql tutorial", "sql"),
    ("sql usage", "sql"),

    ("sql injection", "sql injection"), ("SQL Injection", "sql injection"),
    ("what is sql injection", "sql injection"), ("what’s sql injection", "sql injection"),
    ("sqli", "sql injection"), ("database injection", "sql injection"),
    ("how does sql injection work", "sql injection"), ("explain sql injection", "sql injection"),
    ("examples of sql injection", "sql injection"), ("sql exploit", "sql injection"),

    ("linux", "linux"), ("Linux", "linux"), ("LINUX", "linux"),
    ("what is linux", "linux"), ("what’s linux", "linux"),
    ("tell me about linux", "linux"), ("explain linux", "linux"),
    ("ubuntu linux", "linux"), ("kali linux", "linux"),
    ("linux os", "linux"), ("linux system", "linux"),
    ("linux kernel", "linux"), ("linux basics", "linux"),
    ("what is kali", "linux"), ("learn linux", "linux"),

    ("programming", "programming"), ("Programming", "programming"),
    ("what is programming", "programming"), ("what’s programming", "programming"),
    ("tell me about programming", "programming"), ("explain programming", "programming"),
    ("coding", "programming"), ("computer programming", "programming"),
    ("software programming", "programming"), ("programming basics", "programming"),

    ("python", "python"), ("Python", "python"),
    ("what is python", "python"), ("explain python", "python"),
    ("python language", "python"), ("python coding", "python"),

    ("c", "c"), ("C", "c"),
    ("c language", "c"), ("what is c", "c"),

    ("c++", "c++"), ("C++", "c++"), ("cpp", "c++"),
    ("what is c++", "c++"), ("explain c++", "c++"),

    ("c#", "c#"), ("C#", "c#"),
    ("what is c#", "c#"), ("explain c#", "c#"),

    ("java", "java"), ("Java", "java"),
    ("what is java", "java"), ("explain java", "java"),
    ("java programming", "java"), ("java language", "java"),

    ("html", "html"), ("HTML", "html"),
    ("what is html", "html"), ("explain html", "html"),
    ("html language", "html"), ("html code", "html"),

    ("css", "css"), ("CSS", "css"),
    ("what is css", "css"), ("explain css", "css"),
    ("css language", "css"), ("css styling", "css"),

    ("database", "database"), ("Database", "database"),
    ("databases", "database"), ("what is database", "database"),
    ("what are databases", "database"), ("tell me about databases", "database"),
    ("dbms", "database"), ("db system", "database"),
    ("sql database", "database"), ("data storage", "database"),

    ("authentication", "authentication"), ("Authentication", "authentication"),
    ("what is authentication", "authentication"), ("auth", "authentication"),
    ("user authentication", "authentication"), ("login authentication", "authentication"),

    ("encryption", "encryption"), ("Encryption", "encryption"),
    ("what is encryption", "encryption"), ("explain encryption", "encryption"),
    ("cryptography", "encryption"), ("data encryption", "encryption"),
    ("encryption methods", "encryption"), ("cipher", "encryption"),

    ("vulnerability assessments", "vulnerability assessments"),
    ("what is vulnerability assessment", "vulnerability assessments"),
    ("security assessment", "vulnerability assessments"),
    ("vulnerability scan", "vulnerability assessments"),
    ("network assessment", "vulnerability assessments"),
    ("system vulnerability", "vulnerability assessments"),

    ("malware", "malware"), ("Malware", "malware"), ("what is malware", "malware"),
    ("what is malware", "malware"), ("what’s malware", "malware"),
    ("types of malware", "malware"), ("malicious software", "malware"),
    ("explain malware", "malware"), ("common malware", "malware"),

    ("virus", "virus"), ("viruses", "virus"),
    ("what is a virus", "virus"), ("computer virus", "virus"),

    ("worm", "worm"), ("worms", "worm"),
    ("what is a worm", "worm"), ("computer worm", "worm"),

    ("trojan", "trojan"), ("trojans", "trojan"),
    ("what is a trojan", "trojan"), ("trojan horse", "trojan"),

    ("ransomware", "ransomware"), ("what is ransomware", "ransomware"),
    ("crypto malware", "ransomware"), ("locker ransomware", "ransomware"),

    ("spyware", "spyware"), ("keylogger", "spyware"),
    ("what is spyware", "spyware"), ("explain spyware", "spyware"),

    ("backdoor", "backdoor"), ("what is a backdoor", "backdoor"),
    ("what is a backdoor", "backdoor"),

    ("siem", "siem"), ("SIEM", "siem"),
    ("what is siem", "siem"), ("tell me about siem", "siem"),
    ("explain siem", "siem"), ("siem system", "siem"),

    ("splunk", "splunk"), ("what is splunk", "splunk"),
    ("explain splunk", "splunk"), ("splunk tool", "splunk"),

    ("elk stack", "elk"), ("ELK Stack", "elk"), ("what is elk", "elk"),
    ("explain elk stack", "elk"), ("elastic stack", "elk"),

    ("qradar", "qradar"), ("QRadar", "qradar"),
    ("what is qradar", "qradar"), ("ibm qradar", "qradar"),

    ("detection", "detection"), ("Detection", "detection"),
    ("what is detection", "detection"), ("incident detection", "detection"),

    ("response", "response"), ("Response", "response"),
    ("incident response", "response"), ("what is response", "response"),
    ("security response", "response"),

    ("risk management", "risk management"), ("Risk Management", "risk management"),
    ("what is risk management", "risk management"), ("explain risk management", "risk management"),

    ("vulnerabilities", "vulnerabilities"), ("Vulnerabilities", "vulnerabilities"),
    ("what are vulnerabilities", "vulnerabilities"),
    ("software vulnerabilities", "vulnerabilities"),
    ("system vulnerabilities", "vulnerabilities"),
    ("explain vulnerabilities", "vulnerabilities"),
]