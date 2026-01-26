import os
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_heading(doc, text, level):
    heading = doc.add_heading(text, level=level)
    return heading

def add_paragraph(doc, text):
    p = doc.add_paragraph(text)
    pf = p.paragraph_format
    pf.line_spacing = 1.5
    pf.space_after = Pt(12)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return p

def add_image(doc, image_path, width_inches=4):
    if os.path.exists(image_path):
        doc.add_picture(image_path, width=Inches(width_inches))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        add_paragraph(doc, f"[Image Placeholder: {image_path}]")

def generate_report():
    doc = Document()

    # --- Title Page ---
    title = doc.add_heading('Comprehensive Analysis of Real-World Cybercrime Cases and Global Information Technology Laws', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph('\n' * 5)
    subtitle = doc.add_paragraph('A Multi-Case Study on Financial Heists, Ransomware, and Legal Frameworks')
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.runs[0].font.size = Pt(18)
    subtitle.runs[0].bold = True

    doc.add_paragraph('\n' * 8)
    info = doc.add_paragraph('Prepared for: Information Security Seminar\nPrepared by: AI Research Assistant\nDate: January 2024')
    info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    info.runs[0].font.size = Pt(12)

    doc.add_page_break()

    # --- Table of Contents ---
    add_heading(doc, 'Table of Contents', 1)
    toc_text = [
        "1. Executive Summary",
        "2. Introduction to Cybercrime in the Digital Age",
        "3. Case Study I: The COSMOS Bank Malware Attack (2018)",
        "4. Case Study II: The Bangladesh Bank SWIFT Heist (2016)",
        "5. Case Study III: The WannaCry Ransomware Pandemic (2017)",
        "6. Comparative Technical Analysis of Attack Vectors",
        "7. Global Legal Frameworks for Cybercrime",
        "   7.1 The Information Technology Act, 2000 (India)",
        "   7.2 General Data Protection Regulation (GDPR - EU)",
        "   7.3 The Budapest Convention on Cybercrime",
        "8. How IT Laws Address Modern Cyber Threats",
        "9. Challenges in Cross-Border Investigation",
        "10. Strategic Mitigation and Cybersecurity Best Practices",
        "11. Conclusion",
        "12. References"
    ]
    for item in toc_text:
        p = doc.add_paragraph(item)
        p.paragraph_format.space_after = Pt(6)

    doc.add_page_break()

    # --- 1. Executive Summary ---
    add_heading(doc, '1. Executive Summary', 1)
    summary = (
        "This report provides an in-depth analysis of three major real-world cybercrime cases: the COSMOS Bank heist, the Bangladesh Bank SWIFT attack, and the WannaCry ransomware outbreak. "
        "It explores the technical methodologies employed by attackers, ranging from malware injection to the exploitation of international financial messaging protocols. "
        "Furthermore, the report evaluates the effectiveness of current Information Technology (IT) laws, such as the India's IT Act 2000 and Europe's GDPR, in addressing these threats. "
        "By examining the intersection of technology and law, this document offers strategic recommendations for strengthening global cybersecurity posture."
    )
    add_paragraph(doc, summary)

    # --- 2. Introduction ---
    add_heading(doc, '2. Introduction to Cybercrime in the Digital Age', 1)
    intro = (
        "Cybercrime has evolved from simple hacking for prestige into a multi-billion dollar criminal industry. As organizations migrate their critical infrastructure to the cloud and "
        "interconnect their systems via global networks, the 'attack surface' available to malicious actors has expanded exponentially. Cybercrimes today are often state-sponsored or "
        "coordinated by organized criminal syndicates with resources rivaling those of small nations.\n\n"
        "The fundamental challenge of cybercrime is its asymmetric nature. An attacker needs only to find one vulnerability, whereas a defender must secure every possible entry point. "
        "This report focuses on high-impact crimes that targeted the very foundations of trust in the global financial and health systems, demonstrating why a robust legal framework "
        "is as critical as technical defenses."
    )
    add_paragraph(doc, intro)

    # --- 3. COSMOS Bank ---
    add_heading(doc, '3. Case Study I: The COSMOS Bank Malware Attack (2018)', 1)
    add_image(doc, 'cosmos_bank.png', 2)
    cosmos_text = (
        "In August 2018, hackers targeted the Pune-based COSMOS Cooperative Bank in India. This attack was notable for its use of a 'malware proxy' that bypassed the bank's Core Banking System (CBS). "
        "The attackers infected the ATM switching server, which is responsible for authorizing transactions. By intercepting authorization requests and sending back fake 'approval' messages, "
        "they enabled the withdrawal of over ₹94 crore across 28 countries.\n\n"
        "The technical sophistication involved in coordinating thousands of physical ATM withdrawals (by 'money mules') while simultaneously launching a SWIFT-based transfer "
        "to a bank in Hong Kong made this one of the most complex heists in Indian history. It exposed critical vulnerabilities in the isolation of switching servers and the "
        "monitoring of anomalous transaction volumes."
    )
    add_paragraph(doc, cosmos_text)

    # --- 4. Bangladesh Bank ---
    add_heading(doc, '4. Case Study II: The Bangladesh Bank SWIFT Heist (2016)', 1)
    add_image(doc, 'bangladesh_bank.jpg', 2)
    bb_text = (
        "In February 2016, hackers attempted to steal nearly $1 billion from the Bangladesh Bank's account at the Federal Reserve Bank of New York. "
        "The attackers gained access to the bank's network, likely through a phishing email, and spent months monitoring the system. They eventually obtained credentials for the SWIFT network.\n\n"
        "The hackers sent 35 fraudulent transfer orders. While the Federal Reserve blocked 30 of them due to suspicions (including a spelling error in one of the orders), "
        "five orders totaling $101 million were successful. Of this, $81 million was laundered through casinos in the Philippines. "
        "This case highlighted the danger of compromising trusted messaging systems like SWIFT and the importance of multi-layered authentication for high-value transfers."
    )
    add_paragraph(doc, bb_text)

    # --- 5. WannaCry ---
    add_heading(doc, '5. Case Study III: The WannaCry Ransomware Pandemic (2017)', 1)
    add_image(doc, 'wannacry.png', 4)
    wc_text = (
        "In May 2017, the WannaCry ransomware attack spread to over 200,000 computers in 150 countries. It utilized 'EternalBlue', an exploit allegedly developed by the "
        "U.S. National Security Agency (NSA) and leaked by a group known as the Shadow Brokers. WannaCry targeted vulnerabilities in older versions of the Microsoft Windows "
        "operating system.\n\n"
        "One of the most impacted organizations was the United Kingdom's National Health Service (NHS), where thousands of appointments were cancelled and ambulances were "
        "diverted. The attack was a 'worm', meaning it could spread automatically across networks without human intervention. The incident proved that cybercrime is "
        "not just a financial threat but a direct threat to public safety and critical infrastructure."
    )
    add_paragraph(doc, wc_text)

    # --- 6. Technical Analysis ---
    add_heading(doc, '6. Comparative Technical Analysis of Attack Vectors', 1)
    tech_comp = (
        "Comparing these cases reveals a pattern of attack vectors:\n\n"
        "1. Entry Point: Phishing and social engineering remain the most common entry points (Bangladesh Bank). Exploitation of unpatched software (WannaCry) follows closely.\n"
        "2. Lateral Movement: Once inside, attackers use malware to escalate privileges and move across the network to reach high-value targets like switching servers or SWIFT terminals.\n"
        "3. Evasion: Modern malware often resides in memory (fileless) or uses legitimate system tools (living off the land) to avoid detection by traditional antivirus software.\n"
        "4. Exfiltration/Monetization: Cryptocurrencies are the preferred method for ransomware (WannaCry), while traditional money laundering via casinos or shell companies "
        "is used for banking heists (COSMOS, Bangladesh Bank)."
    )
    add_paragraph(doc, tech_comp)

    # --- 7. Legal Frameworks ---
    add_heading(doc, '7. Global Legal Frameworks for Cybercrime', 1)

    add_heading(doc, '7.1 The Information Technology Act, 2000 (India)', 2)
    it_act = (
        "The IT Act is the cornerstone of India's cyber law. Key provisions include:\n"
        "• Section 66: Punishment for computer-related offenses.\n"
        "• Section 66C: Punishment for identity theft.\n"
        "• Section 66F: Punishment for cyber terrorism (applicable to attacks on critical infrastructure like the NHS or power grids).\n"
        "• Section 70: Identification of 'Protected Systems', providing higher penalties for unauthorized access to critical national infrastructure."
    )
    add_paragraph(doc, it_act)

    add_heading(doc, '7.2 General Data Protection Regulation (GDPR - EU)', 2)
    gdpr = (
        "While primarily a data protection law, GDPR has significant implications for cybercrime. It mandates 'security by design' and 'security by default'. "
        "Organizations that fail to implement adequate security measures and suffer a data breach can face fines up to €20 million or 4% of their global annual turnover. "
        "This legal pressure has forced companies worldwide to treat cybersecurity as a boardroom-level priority."
    )
    add_paragraph(doc, gdpr)

    add_heading(doc, '7.3 The Budapest Convention on Cybercrime', 2)
    budapest = (
        "The Budapest Convention is the only binding international instrument on this issue. It serves as a guideline for any country developing comprehensive national "
        "legislation against cybercrime and as a framework for international cooperation between State Parties. It addresses crimes such as copyright infringement, "
        "computer-related fraud, and child pornography."
    )
    add_paragraph(doc, budapest)

    # --- 8. How Laws Address Crime ---
    add_heading(doc, '8. How IT Laws Address Modern Cyber Threats', 1)
    address_text = (
        "IT laws address cybercrime through several mechanisms:\n\n"
        "• Deterrence: By imposing significant jail time and fines, the law seeks to discourage potential criminals. However, the effectiveness of deterrence is limited "
        "by the low probability of being caught in cross-border crimes.\n"
        "• Legal Admissibility: Laws define the standards for digital forensics, ensuring that log files, encrypted data, and other digital artifacts can be used as evidence in court.\n"
        "• Mandatory Reporting: Laws now increasingly require organizations to report breaches within a specific timeframe (e.g., 72 hours under GDPR), which helps in "
        "containing the spread of attacks and informing the public."
    )
    add_paragraph(doc, address_text)

    # --- 9. Challenges ---
    add_heading(doc, '9. Challenges in Cross-Border Investigation', 1)
    challenges = (
        "Cybercrime investigation faces 'The Triple Challenge':\n\n"
        "1. Jurisdiction: Data and perpetrators are often in different countries. Mutual Legal Assistance Treaties (MLATs) are often too slow for the digital age.\n"
        "2. Technical Sophistication: The use of 'Bulletproof Hosting' providers and decentralized finance (DeFi) makes tracing funds and servers extremely difficult.\n"
        "3. Attribution: Proving 'who' was behind the keyboard is the hardest part. Attackers often use 'false flags' to mislead investigators into blaming a different "
        "group or nation-state."
    )
    add_paragraph(doc, challenges)

    # --- 10. Mitigation ---
    add_heading(doc, '10. Strategic Mitigation and Cybersecurity Best Practices', 1)
    mitigation = (
        "To combat cybercrime, a defense-in-depth strategy is required:\n\n"
        "• Patch Management: Regularly updating software to fix known vulnerabilities (preventing attacks like WannaCry).\n"
        "• Employee Awareness: Training staff to recognize phishing attempts (preventing attacks like Bangladesh Bank).\n"
        "• Network Segmentation: Ensuring that a breach in one department does not allow access to the entire organization.\n"
        "• Incident Response Plans: Having a tested plan to follow once an attack is detected, including communication with law enforcement."
    )
    add_paragraph(doc, mitigation)

    # --- 11. Conclusion ---
    add_heading(doc, '11. Conclusion', 1)
    conclusion = (
        "The case studies of COSMOS Bank, Bangladesh Bank, and WannaCry illustrate the devastating potential of modern cybercrime. They show that no organization, "
        "no matter how large or established, is immune to attack. IT laws have come a long way in defining and penalizing these crimes, but the law will always "
        "be in a race with technological innovation.\n\n"
        "Ultimately, cybersecurity is a shared responsibility. It requires technical excellence, proactive legislation, and international cooperation. As we move "
        "further into an era of Artificial Intelligence and Quantum Computing, our legal and technical frameworks must become even more agile and resilient to "
        "protect the digital world."
    )
    add_paragraph(doc, conclusion)

    # --- 12. References ---
    add_heading(doc, '12. References', 1)
    refs = [
        "1. Anderson, R. (2020). Security Engineering: A Guide to Building Dependable Distributed Systems. Wiley.",
        "2. Information Technology Act, 2000. Government of India.",
        "3. Europol. (2023). Internet Organised Crime Threat Assessment (IOCTA).",
        "4. SWIFT. (2019). Three years on from the Bangladesh Bank heist: Lessons learned.",
        "5. Microsoft. (2017). Customer Guidance for WannaCry attacks."
    ]
    for ref in refs:
        add_paragraph(doc, ref)

    save_path = 'cybercrime_analysis_report.docx'
    doc.save(save_path)
    print(f"Document saved as {save_path}")

if __name__ == "__main__":
    generate_report()
