#!/usr/bin/env python3
"""
The fictional clinic the demo answers for.

A prospect pressing "Start call" on our healthcare page needs to hear the agent
handle a clinic call. So the demo has its own clinic, its own fee schedule, its
own insurers and its own triage rules, and the knowledge base is built from this
file alone.

Everything here is invented and says so. The clinic does not exist, the phone
number is one of Ofcom's reserved drama numbers so it cannot ring anybody, and
the consultants are made up. In healthcare that matters more than anywhere: a
demo that quotes a real clinic's prices or names a real consultant is a problem,
and one that gives clinical advice is a bigger one. The agent is built so it
cannot.
"""

TENANT = "demo-healthcare"

BIZ = dict(
    name="Brookfield Clinic",
    short="Brookfield",
    kind="private outpatient clinic",
    town="Rayleigh",
    area="Rayleigh, Hockley, Hullbridge and south Essex",
    phone="01702 960 228",          # Ofcom reserved range for drama
    email="reception@brookfieldclinic.example",
    hours="Monday to Friday eight to six, Saturday nine to one",
    founded="2014",
    branches="one clinic on London Hill",
    agent_name="Ruth",
)

# Clinics and who runs them. The agent books against these, by name.
CLINICS = [
    ("Dermatology", "Mr Alvarez", "Tuesday and Friday", 30, 20),
    ("Musculoskeletal and sports injury", "Miss Okafor", "Monday and Thursday", 30, 20),
    ("Physiotherapy", "Nadia Petrov", "Monday to Friday", 45, 30),
    ("Ultrasound and imaging", "Nadia Petrov", "Wednesday and Thursday", 30, 30),
    ("General health review", "Dr Hamid", "Monday, Wednesday, Friday", 45, 30),
]

# The fees the agent is allowed to quote. Nothing else is quotable.
FEES = [
    dict(group="Consultations", name="Initial consultation",
         aliases=['consultation', 'first appointment', 'see a consultant', 'how much to be seen', 'appointment cost', 'initial', 'new patient'], price="£195",
         detail="Thirty minutes with the consultant. Covers dermatology, "
                "musculoskeletal and general review. Self-pay price."),
    dict(group="Consultations", name="Follow-up consultation",
         aliases=['follow up', 'review appointment', 'second appointment'], price="£125",
         detail="Twenty minutes. Within six months of an initial consultation "
                "under the same consultant."),
    dict(group="Consultations", name="Extended health review",
         aliases=['health review', 'health check', 'mot', 'bloods', 'blood test', 'screening'], price="£340",
         detail="Forty five minutes with Doctor Hamid, including bloods taken on "
                "the day. Results discussed at a follow-up."),
    dict(group="Physiotherapy", name="Initial physiotherapy assessment",
         aliases=['physio', 'physiotherapy', 'first physio', 'back pain', 'injury'], price="£85",
         detail="Forty five minutes, including treatment on the day where "
                "appropriate and an exercise plan to take away."),
    dict(group="Physiotherapy", name="Follow-up physiotherapy",
         aliases=['physio follow up', 'more physio sessions'], price="£65",
         detail="Thirty minutes."),
    dict(group="Physiotherapy", name="Block of six follow-ups",
         aliases=['block', 'package of sessions', 'six sessions', 'course of physio'], price="£340",
         detail="Six thirty minute sessions, paid up front. Valid for six months."),
    dict(group="Imaging", name="Diagnostic ultrasound",
         aliases=['ultrasound', 'scan', 'imaging', 'sonographer'], price="£250",
         detail="Thirty minutes with a written report to your referring clinician "
                "within three working days."),
    dict(group="Imaging", name="Ultrasound guided injection",
         aliases=['injection', 'steroid injection', 'guided injection'], price="£395",
         detail="Thirty minutes. Requires a consultant referral first."),
]

INSURERS = ["Bupa", "AXA Health", "Aviva", "Vitality", "WPA", "Cigna"]

FACTS = [
    ("What we do",
     "Brookfield Clinic is a private outpatient clinic on London Hill in Rayleigh, "
     "open since 2014. We run dermatology, musculoskeletal and sports injury, "
     "physiotherapy, diagnostic ultrasound and general health reviews. We are "
     "outpatient only: we do not have beds and we do not do surgery."),
    ("Opening hours",
     "Reception is open Monday to Friday, eight until six, and Saturday nine until "
     "one. We are closed Sundays and bank holidays. Appointments can be booked at "
     "any hour, including when reception is closed."),
    ("Self-pay prices",
     "An initial consultation is £195 for thirty minutes. A follow-up within six "
     "months is £125. An extended health review with Doctor Hamid is £340 for forty "
     "five minutes including bloods. Physiotherapy is £85 for the initial assessment "
     "and £65 for follow-ups, or £340 for a block of six. A diagnostic ultrasound is "
     "£250 and an ultrasound guided injection is £395."),
    ("Insurance",
     "We are recognised by Bupa, AXA Health, Aviva, Vitality, WPA and Cigna. You will "
     "need your membership number and, for most policies, an authorisation code from "
     "your insurer before the appointment. We can book you in without the code and "
     "add it later, but it must be with us before you are seen or the appointment is "
     "charged as self-pay."),
    ("Referrals",
     "Most insurers want a GP referral letter. Self-paying patients can book "
     "dermatology, physiotherapy and general health reviews directly, with no "
     "referral. Ultrasound and any injection needs a referral from a clinician, "
     "either yours or one of ours."),
    ("What to bring",
     "Photo identification, your insurance details if you are using them, a list of "
     "any medication you take, and your referral letter if you have one. The letter "
     "can be uploaded from the link in your confirmation email instead, if that is "
     "easier."),
    ("Preparing for an ultrasound",
     "For an abdominal ultrasound, do not eat for six hours beforehand. Water is "
     "fine, and you should keep taking any prescribed medication. For all other "
     "scans there is no preparation. This is in your confirmation, but people read "
     "it after lunch, so we say it on the phone too."),
    ("Parking",
     "There is parking underneath the building, free for patients for two hours. The "
     "barrier reads your registration, so there is no ticket to validate. There are "
     "two accessible bays by the lift."),
    ("Cancellations",
     "We ask for twenty four hours notice. Inside that we charge half the "
     "appointment fee, because the slot cannot usually be refilled. Cancelled slots "
     "go to our short notice list, so if you are waiting for something sooner, say "
     "so and we will add you."),
    ("Results",
     "Results and reports go to the clinician who ordered them, and they come back "
     "to you. We do not discuss results at reception, and the assistant will not "
     "either. Ultrasound reports reach your referring clinician within three working "
     "days."),
    ("Accessibility",
     "The clinic is on one level with step free access from the car park and a lift "
     "from the street entrance. There is an accessible toilet by reception. Tell us "
     "when you book if you need a longer appointment or a hearing loop."),
]

# What the agent can book. Naming these stops it offering a "free 30 minute
# consultation", which is Online Marketing Help's own language, not this
# business's, and which this business does not sell.
BOOKS = ["an initial consultation with the right consultant",
         "a follow-up appointment",
         "a physiotherapy assessment",
         "an ultrasound or imaging appointment"]

# The hard lines. In healthcare these are the whole point of the demo.
NEVER = [
    "Give no clinical advice of any kind. Not about symptoms, not about medication, "
    "not about whether something is serious, not about whether to worry, and not "
    "about whether to come in. Take the detail and get a clinician to ring back.",
    "Do not discuss, interpret or read out results. Ever. The clinician who ordered "
    "them does that.",
    "Do not diagnose, and do not reassure. 'It's probably nothing' is advice.",
    "Do not quote a price that is not in the fee list above, and do not confirm "
    "whether a specific policy covers a specific treatment. The insurer decides that.",
    "Do not handle a complaint about care. Take the detail and pass it to the "
    "practice manager.",
]

# What counts as urgent, and what the agent does about it.
TRIAGE = [
    ("Chest pain, breathlessness, stroke signs, severe bleeding, anaphylaxis",
     "Tell them to ring 999 now and end the call. Do not take details first."),
    ("Severe pain, a rapidly spreading rash, a wound that looks infected, anything "
     "the caller describes as getting worse quickly",
     "Take name and number, mark it urgent, and get a clinician to ring back within "
     "the hour. Say that is what you are doing."),
    ("Anything else clinical",
     "Take the detail and arrange a call back the same working day."),
]
